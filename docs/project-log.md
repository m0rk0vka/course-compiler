# Project log

## Direction

Pilot one MIT distributed systems lecture. Use four short English episodes with a diagram or animation where it explains behavior, and an optional pause to predict what happens next. Use original MIT papers and labs. Evaluate whether it feels easy to start after work and helps when opening Lab 1.

## Sources and status

- [MIT 6.824 Lecture 1 recording (Spring 2020)](https://www.youtube.com/watch?v=cQP8WApzIQQ) located. Direct request timed out. Transcript, audio, frames and timestamps are unverified.
- [MIT Lecture 1 notes (Spring 2026)](https://pdos.csail.mit.edu/6.5840/notes/l01.txt) and [Dean and Ghemawat's MapReduce paper (2004)](https://pdos.csail.mit.edu/6.824/papers/mapreduce.pdf) informed the draft. The notes are a different course edition from the recording.
- [MIT Lab 1](https://pdos.csail.mit.edu/6.5840/labs/lab-mr.html) is the practice handoff.
- [Lecture 1 draft](../lessons/01-introduction.md) contains four outlines and prediction questions. No video, narration audio, subtitles or interactive implementation exists yet.

## Tools evaluated

| Tool | Intended use | Status |
| --- | --- | --- |
| [steipete/summarize](https://github.com/steipete/summarize/blob/main/docs/youtube.md) | Caption and frame extraction | Documentation reviewed. Not run on the MIT recording. |
| [youtube-transcript](https://github.com/dedene/skills/blob/main/skills/youtube-transcript/SKILL.md) | Captions via yt-dlp | Alternative identified. Not run. |
| [Remotion Agent Skills](https://www.remotion.dev/docs/ai/skills) | Render animated scenes with narration and captions | Documentation reviewed. Not installed or run. |
| ChatGPT interactive visuals | Step through a timeline with worker failure and retries | Considered. No interactive scene created. |
| ChatGPT quiz widget | Multiple-choice checks if requested | Considered. Current draft uses open-ended questions in prose. |
| [pstack / poteto-mode](https://github.com/cursor/plugins/blob/main/pstack/README.md) | Organize and verify future coding work | Researched. Not installed or run. |

Next step: make and verify one English pilot scene for episode 3. Try to obtain captions and relevant frames from the 2020 recording. If they remain unavailable, label the scene as an original explanation based on the paper and MIT notes. Show which reducer already fetched its partition, then pause before revealing the retry. A later pass can turn the repeatable adaptation and verification steps into dedicated skills.
