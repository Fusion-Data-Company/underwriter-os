#!/usr/bin/env python3
"""
Quarry lookup for Underwriter OS — parcels + skip-trace, against whatever Quarry-compatible
parcel data endpoint the user's firm has set up. Nothing is baked in; this repo ships no
default endpoint and no key.

Reads from environment (the user's own config/.env, not this repo):
  QUARRY_BASE_URL   your firm's Quarry (or compatible) base URL, no trailing slash
  QUARRY_API_KEY    your firm's Quarry API key (qk_...), if the account uses one

Parcel data:
  python quarry_lookup.py --address "123 Main St, Anytown ST"
  python quarry_lookup.py --lat 35.93 --lng -86.84
  python quarry_lookup.py --bbox minLng,minLat,maxLng,maxLat [--limit 100]

Skip-trace (owner phone/email — charges 1 Quarry credit per trace, if your account supports it):
  python quarry_lookup.py --skiptrace --address "123 Main St, Anytown ST"
  python quarry_lookup.py --skiptrace --name "John Smith" --state ST
  python quarry_lookup.py --skiptrace --apn 0123456789
"""
import os, sys, json, time, argparse, urllib.parse, urllib.request

# No default — the firm's own QUARRY_BASE_URL must be set in config/.env.
BASE = (os.environ.get("QUARRY_BASE_URL") or "").rstrip("/")
KEY = os.environ.get("QUARRY_API_KEY") or ""  # optional; only used if present (e.g. for skip-trace)


def _req(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    if KEY:
        headers["Authorization"] = f"Bearer {KEY}"
    req = urllib.request.Request(BASE + path, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        try:
            payload = json.loads(e.read().decode())
        except Exception:
            payload = {"error": f"http_{e.code}"}
        if e.code == 401:
            sys.exit("Quarry auth failed (401): QUARRY_API_KEY invalid or revoked.")
        if e.code == 402:
            sys.exit("Quarry: insufficient credits for skip-trace. Top up the Quarry account.")
        if e.code == 451:
            return 451, payload  # suppressed — surface reasons, no charge
        if e.code == 503:
            sys.exit("Quarry skip-trace engine is unreachable right now (no charge). Try later.")
        if e.code == 404:
            return 404, payload
        sys.exit(f"Quarry error {e.code}: {json.dumps(payload)[:300]}")
    except Exception as e:
        sys.exit(f"Could not reach Quarry at {BASE} ({e}). Is the API public and the URL correct?")


def geocode(address):
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(
        {"q": address, "format": "json", "limit": 1})
    req = urllib.request.Request(url, headers={"User-Agent": "UnderwriterOS/1.0 (parcel lookup)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if not data:
        sys.exit(f"Could not geocode address: {address}")
    return float(data[0]["lat"]), float(data[0]["lon"])


def parcel(args):
    if args.bbox:
        mnLng, mnLat, mxLng, mxLat = [float(x) for x in args.bbox.split(",")]
        q = urllib.parse.urlencode({"minLng": mnLng, "minLat": mnLat, "maxLng": mxLng,
                                    "maxLat": mxLat, "limit": args.limit})
        return _req("GET", f"/api/parcels/bbox?{q}")[1]
    lat, lng = args.lat, args.lng
    if lat is None or lng is None:
        if not args.address:
            sys.exit("Provide --address, --lat/--lng, or --bbox.")
        lat, lng = geocode(args.address)
        print(f"# geocoded '{args.address}' -> {lat},{lng}", file=sys.stderr)
    _, out = _req("GET", f"/api/parcels/at?{urllib.parse.urlencode({'lat': lat, 'lng': lng, 'zoom': args.zoom})}")
    if not out.get("parcel"):
        _, out = _req("GET", f"/api/parcels/point?{urllib.parse.urlencode({'lat': lat, 'lng': lng})}")
    return out


def skiptrace(args):
    body = {}
    for k in ("apn", "name", "company", "city", "state", "address"):
        v = getattr(args, k, None)
        if v:
            body[k] = v
    if args.lat is not None and args.lng is not None:
        body["lat"], body["lng"] = args.lat, args.lng
    if args.address and not (args.lat or args.name or args.apn):
        body["lat"], body["lng"] = geocode(args.address)
        print(f"# geocoded '{args.address}' -> {body['lat']},{body['lng']}", file=sys.stderr)
    if not (body.get("apn") or body.get("name") or body.get("company") or ("lat" in body)):
        sys.exit("Skip-trace needs --apn, --name/--company, --address, or --lat/--lng.")
    status, out = _req("POST", "/api/skiptrace", body)
    if status == 451:
        return {"status": "suppressed", "reasons": out.get("reasons")}
    # async: poll status until done
    job = out.get("jobId") or out.get("job")
    if out.get("status") == "running" and job:
        for _ in range(20):
            time.sleep(3)
            _, st = _req("GET", f"/api/skiptrace/status?{urllib.parse.urlencode({'job': job})}")
            if st.get("status") != "running":
                return st
        return {"status": "running", "jobId": job, "note": "still running; poll later"}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skiptrace", action="store_true", help="owner phone/email (charges 1 credit)")
    ap.add_argument("--address"); ap.add_argument("--apn"); ap.add_argument("--name")
    ap.add_argument("--company"); ap.add_argument("--city"); ap.add_argument("--state")
    ap.add_argument("--lat", type=float); ap.add_argument("--lng", type=float)
    ap.add_argument("--bbox"); ap.add_argument("--limit", type=int, default=100)
    ap.add_argument("--zoom", type=int, default=17)
    a = ap.parse_args()
    if not BASE:
        print(json.dumps({"error": "QUARRY_BASE_URL is not set. Add your firm's Quarry (or compatible) "
                                    "endpoint to config/.env — see config/.env.example and config/CONFIG-GUIDE.md."}))
        sys.exit(1)
    out = skiptrace(a) if a.skiptrace else parcel(a)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
