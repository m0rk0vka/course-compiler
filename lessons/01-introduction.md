# Lecture 1 — Introduction to Distributed Systems

English pilot based on the [MIT 2026 notes](https://pdos.csail.mit.edu/6.5840/notes/l01.txt) and the [2004 MapReduce paper](https://pdos.csail.mit.edu/6.824/papers/mapreduce.pdf). These are original teaching scenes. Their order and wording have not been checked against the 2020 recording.

## 1. Why distribute anything?

Show a single Go program counting words across files. Add a worker to increase throughput. Have one worker stop replying while the other keeps working. Introduce partial failure and the course's focus on reasoning about guarantees, failure and performance through papers and Go labs.

**Pause:** A worker has stopped replying. What do you know, and what are you guessing?

## 2. How does MapReduce count words?

Animate two inputs, `go go` and `go rust`. Each mapper emits one pair per word. A shared partitioning rule routes all three `go` pairs to the same reducer. Different keys can share a partition while being reduced separately. The result is `go: 3` and `rust: 1`.

**Pause:** What breaks if each mapper routes its `go` pairs to a randomly chosen reducer?

## 3. What happens when a worker disappears?

Worker A completes a map task and writes intermediate output locally. R1 fetches its partition. A fails before R2 fetches its partition. Worker B reruns the map task and R2 fetches the replacement partition. R1 can keep the data it already fetched. A deterministic map function produces equivalent intermediate data for the same input. Each reducer uses one copy of its partition per logical map task. See the paper's worker failure and failure semantics sections (§3.3).

**Pause:** What could change if the mapper uses an external service that returns a different value on every attempt?

## 4. Why don’t twice as many workers make it twice as fast?

Show remote input reads, traffic during shuffle, and one slow task keeping the job open. Explain how scheduling work near its input reduces input traffic and how backup attempts can shorten the tail. Treat the paper’s measurements as evidence from a particular cluster.

**Pause:** When most workers are idle near the end, why might a backup copy of one task help more than adding machines?

**Practice:** Open [MIT Lab 1](https://pdos.csail.mit.edu/6.5840/labs/lab-mr.html). Identify what the coordinator tracks and what one worker does before changing any code.
