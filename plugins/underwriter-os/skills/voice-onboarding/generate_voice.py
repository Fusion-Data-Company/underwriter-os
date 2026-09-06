#!/usr/bin/env python3
"""
Underwriter OS voice — ElevenLabs text-to-speech in an approved female voice (Sarah).
Key + voice ID are baked into Underwriter OS (underwriter-os/keys.env). Claude runs this
for the user and then plays/presents the MP3 — the user does nothing.

Usage:
  python generate_voice.py --text "....." --out welcome.mp3
"""
import os, sys, json, argparse, urllib.request

ap = argparse.ArgumentParser()
ap.add_argument("--text", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--voice", default=os.environ.get("ELEVENLABS_VOICE_ID", "EXAVITQu4vr4xnSDxMaL"))  # Sarah
a = ap.parse_args()

key = os.environ.get("ELEVENLABS_API_KEY")
if not key:
    sys.exit("ELEVENLABS_API_KEY not set — load underwriter-os/keys.env first.")

body = json.dumps({
    "text": a.text,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {"stability": 0.5, "similarity_boost": 0.75, "style": 0.0, "use_speaker_boost": True},
}).encode()
req = urllib.request.Request(
    f"https://api.elevenlabs.io/v1/text-to-speech/{a.voice}",
    data=body,
    headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"},
)
try:
    r = urllib.request.urlopen(req, timeout=120)
    open(a.out, "wb").write(r.read())
    print(os.path.abspath(a.out))
except urllib.error.HTTPError as e:
    print("ElevenLabs error", e.code, e.read().decode()[:200]); sys.exit(1)
