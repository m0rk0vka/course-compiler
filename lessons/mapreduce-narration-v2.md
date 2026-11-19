# MapReduce — recording script

Target: about two minutes. Read conversationally, around 125–140 words per minute. Directions in brackets are silent. Leave five seconds after the prediction question. Record each scene as a separate take. The first pilot's Flite voice was rejected. This version is ready for a human read once the recording comparison is resolved.

## Scene 1 · Why use MapReduce?

[Curious, as if asking a colleague.] Say you need to count every word in an archive too large for one machine to process in time. How would you split the work?

[Short beat.] Give different files to different workers. Now they can read and process those files in parallel. But someone still has to bring the results together. And if a machine drops out halfway through, someone has to work out what to run again.

[Emphasize “two functions.”] MapReduce lets you describe the job with two functions. The framework handles scheduling, moving data between machines, and retrying work.

*Visual:* Split the archive across workers, then show one worker going quiet. Keep the original inputs visible.

## Scene 2 · Map, shuffle, reduce

[Slow down on the input.] One file says “go, go.” The other says “go, rust.” Each mapper emits a one for every word it sees.

Here’s the trick. All three “go” records have to meet at the same reducer, even though they came from different files. The shuffle routes them by key. Then reduce adds up the ones. Three for “go.” One for “rust.”

*Visual:* Keep the two input lanes separate through Map. Animate the three identical keys converging during Shuffle. Show both totals only at Reduce.

## Scene 3 · What if a mapper crashes?

[Switch from explanation to a question.] Worker A finishes its map task and saves the intermediate data on its own disk. Reducer one has already fetched its partition. Reducer two is about to fetch the other partition. Then A crashes.

[Let “crashes” land.] Which reducer needs help, and what would you rerun?

[Five seconds of silence. Freeze the data already fetched by reducer one.]

[Even, matter-of-fact.] Reducer two needs its missing partition. The coordinator assigns the same map task to worker B. Reducer two fetches from B. Reducer one keeps what it already has.

[Emphasize “same input.”] If map is deterministic, the same input gives equivalent intermediate data on either worker. Each reducer uses one partition from that logical task.

*Visual:* Preserve R1's fetched data through the crash. Draw the replacement transfer only to R2.

## Recording comparison

- [Target video: MIT Lecture 1, Spring 2020](https://www.youtube.com/watch?v=cQP8WApzIQQ). The page was identified, but direct access timed out and the audio and captions remain unverified. A publicly indexed transcript found during the search points to a different YouTube video ID (WtZ7pcRSkOA), so it cannot establish timing or wording for this recording.
- [Official MIT notes, Spring 2026](https://pdos.csail.mit.edu/6.5840/notes/l01.txt). Cross-check the purpose of the framework and the word-count data flow.
- [Dean and Ghemawat, 2004](https://pdos.csail.mit.edu/6.824/papers/mapreduce.pdf). Sections 2–3 explain the programming model and execution. Section 3.3 covers local intermediate files, rerunning completed Map tasks and using the replacement output when a reducer has yet to fetch its partition.
