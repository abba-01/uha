# `_ans/` — Attribution Naming Service (canary)

**Concept (Eric, 2026-05-04):** A form of quick DNS for files. One `.txt` pointer per artifact, named the same as the target file, containing:

```
→ <absolute path to artifact>
<one-sentence description of what it's about>
```

**Why l6:** lookup table is read-mostly archive material; it indexes work that lives elsewhere (typically l7 active workspace, occasionally l5 published).

**Status:** canary. If the convention proves out, propagate from `uha/uso/l6/_ans/` per USO carrier-set design pattern.
