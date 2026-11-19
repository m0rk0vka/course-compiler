# MapReduce — recording script

Target: about two minutes. Read conversationally, around 125–140 words per minute. Directions in brackets are silent. Leave five seconds after the prediction question. Record each scene as a separate take. The first pilot's Flite voice was rejected. Try an expressive English voice in ElevenLabs Studio on the audition excerpt before rendering the episode.

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

The [Spring 2021 lecture](https://www.youtube.com/watch?v=WtZ7pcRSkOA) is the reference recording for this adaptation. These entry points come from [transcript-based notes](https://jingzechen.github.io/courses/mit-6824-s21/lectures/001/). Direct download of the English SRT timed out, so timing and wording have not been independently checked against the audio.

- [46:04](https://www.youtube.com/watch?v=WtZ7pcRSkOA&t=2764s) — why Google needed a framework for large batch jobs.
- [50:42](https://www.youtube.com/watch?v=WtZ7pcRSkOA&t=3042s) — word-count walkthrough. MIT uses three files. Our two-file example is an original simplification.
- [53:21](https://www.youtube.com/watch?v=WtZ7pcRSkOA&t=3201s) — grouping by key and summing values.
- [1:09:55](https://www.youtube.com/watch?v=WtZ7pcRSkOA&t=4195s) — retry and duplicate execution discussion. The two-reducer recovery scene illustrates [Dean and Ghemawat (2004), §3.3](https://pdos.csail.mit.edu/6.824/papers/mapreduce.pdf).

## Voice audition

Paste this excerpt into ElevenLabs Studio with a conversational English voice. Try Eleven v3. The tags are delivery cues.

> [curious] How would you count every word in an archive that's too big for one machine to process in time?
>
> [short pause] Give each worker a different set of files. Now they can work in parallel. But someone still has to bring the results together.
>
> [thoughtful] And if a worker disappears halfway through, someone has to decide what to run again. That's the job MapReduce takes off your hands.

Export the audition as audio. For the full pilot, insert the five-second prediction pause in the edit. No ElevenLabs audio was generated in this session.
