---
name: voice-onboarding
description: Speak. Generate and play a short spoken report using ElevenLabs, once the user has connected their own voice key. Use automatically at the START of every Underwriter OS session (a quick spoken status), during first-time onboarding (the welcome), and any time the user says "give me a voice report," "read it to me," or wants something spoken. If no voice key is connected, just speak in text and offer to set it up.
---

# Voice (Underwriter OS spoken reports)

Underwriter OS can talk, once the user connects their own ElevenLabs key. It opens each session with a short spoken status and welcomes new users by voice. If no voice key is connected yet, greet and welcome them in text — never block onboarding on voice.

## HARD LAW reminder
If voice is set up, do it for them: generate the audio and play it. Never tell the user to run anything themselves.

## Setup (once, per user)
Voice needs the user's own ElevenLabs API key in `config/.env` (see `config/.env.example`). If it's not there yet, don't attempt voice — proceed in text, and offer to walk them through connecting it (a free ElevenLabs account is enough to start).

## How to speak (Claude runs this; user does nothing once connected)
1. Load the key: `set -a; . config/.env; set +a`.
2. Write the words to speak, then:
   ```bash
   set -a; . config/.env; set +a
   python underwriter-os/skills/voice-onboarding/generate_voice.py --text "WHAT TO SAY" --out underwriter-os/audio/report-<name>.mp3
   ```
3. **Play it for them:** present the saved MP3 file (it plays inline in chat). Keep spoken text tight — 2–5 sentences.

## When to speak
- **First install (welcome):** use the welcome block in `underwriter-os/templates/onboarding-voice-script.md`, if voice is connected; otherwise say the same welcome in text.
- **Every session open:** a fresh ~3-sentence status — greet them by name, say what's ready, and the one thing they can ask for. Build it from their CLAUDE.md (name/role/active deals) + anything new.
- **On request:** read a summary, a memo's bottom line, or a deal status aloud.

## Style
Warm, confident, concise. Speak like a sharp executive assistant, not a robot. No jargon. Address the person by name when you know it.

## Notes
- Never fetch or expect a voice key from this repo — it isn't there. The key is the user's own, in their local `config/.env`.
- If audio generation ever fails, just continue in text and mention the spoken report is unavailable this time.
