# Project log

## Direction

Pilot one MIT distributed systems lecture. Use four short English episodes with a diagram or animation where it explains behavior, and an optional pause to predict what happens next. Use original MIT papers and labs. Evaluate whether it feels easy to start after work and helps when opening Lab 1.

## Sources and status

- [MIT 6.824 Lecture 1 recording (Spring 2020)](https://www.youtube.com/watch?v=cQP8WApzIQQ) located. Direct request timed out. Transcript, audio, frames and timestamps are unverified.
- [MIT Lecture 1 notes (Spring 2026)](https://pdos.csail.mit.edu/6.5840/notes/l01.txt) and [Dean and Ghemawat's MapReduce paper (2004)](https://pdos.csail.mit.edu/6.824/papers/mapreduce.pdf) informed the draft. The notes are a different course edition from the recording.
- [MIT Lab 1](https://pdos.csail.mit.edu/6.5840/labs/lab-mr.html) is the practice handoff.
- [Lecture 1 draft](../lessons/01-introduction.md) contains four outlines and prediction questions. Episode 3 now has a rendered pilot and a standalone interactive scene.

## Tools evaluated

| Tool | Intended use | Status |
| --- | --- | --- |
| [steipete/summarize](https://github.com/steipete/summarize/blob/main/docs/youtube.md) | Caption and frame extraction | Documentation reviewed. Not run on the MIT recording. |
| [youtube-transcript](https://github.com/dedene/skills/blob/main/skills/youtube-transcript/SKILL.md) | Captions via yt-dlp | Alternative identified. Not run. |
| [Remotion Agent Skills](https://www.remotion.dev/docs/ai/skills) | Render animated scenes with narration and captions | Documentation reviewed. Not installed or run. |
| ChatGPT interactive visuals | Step through a timeline with worker failure and retries | Standalone HTML implemented. Predict/reveal, back and replay checked with JavaScript. |
| ChatGPT quiz widget | Multiple-choice checks if requested | Considered. Current draft uses open-ended questions in prose. |
| [pstack / poteto-mode](https://github.com/cursor/plugins/blob/main/pstack/README.md) | Organize and verify future coding work | Researched. Not installed or run. |

## Episode 3 pilot

- [Interactive scene](../lessons/mapreduce-worker-failure.html). Download the HTML and open it locally. The prediction appears before the retry is revealed.
- [Render script](../scripts/render-mapreduce-pilot.py). Run `python scripts/render-mapreduce-pilot.py` with Pillow, DejaVu Sans, and FFmpeg built with Flite and libx264. The script produces a 55-second English MP4 with synthetic narration and on-screen captions.
- Verification: checked event order and deterministic output against §3.3 of Dean and Ghemawat (2004). The MP4 decoded without errors and contains H.264 video and AAC audio. Original recording alignment is still unverified.

Next step: try the episode and answer the prediction in English. Use that feedback to decide whether to render the remaining three episodes.
