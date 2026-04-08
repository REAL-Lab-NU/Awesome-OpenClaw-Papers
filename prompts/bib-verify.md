# Citation Verification Agent (Parallel-Safe)

You are a citation verification agent. You work as part of a team of parallel agents, coordinating through a shared `index.json` to avoid duplicate work.

## Source

Fetch the BibTeX file from:
```
https://raw.githubusercontent.com/REAL-Lab-NU/Awesome-OpenClaw-Papers/main/references.bib
```

## Output Directory

```
./bib-verify/
```

Create this directory if it does not exist.

## Coordination File

```
./bib-verify/index.json
```

This file tracks every entry's status. Structure:

```json
{
  "cite-key-1": { "status": "done", "verdict": "CORRECT", "summary": "" },
  "cite-key-2": { "status": "in_progress", "claimed_at": "2026-04-08T12:00:00Z" },
  "cite-key-3": { "status": "pending" }
}
```

Status values: `pending` | `in_progress` | `done` | `not_found`

---

## Workflow

### STEP 0 — Initialize (first agent only)

If `./bib-verify/index.json` does NOT exist:

1. Fetch the bib file from the GitHub URL above.
2. Parse all cite keys in order of appearance.
3. Create `index.json` with every entry set to `"status": "pending"`.
4. Create the `./bib-verify/` directory.

### STEP 1 — Claim next entry

1. Read `index.json`.
2. Find the first entry with `"status": "pending"`.
3. If no pending entries remain:
   - If any entries are still `"in_progress"`, print "Waiting for other agents" and stop.
   - If ALL entries are `"done"` or `"not_found"`, go to STEP 5 (Final Report).
4. **IMMEDIATELY** update that entry to `"in_progress"` with `"claimed_at": "<current ISO timestamp>"` and write `index.json` back to disk. This is your claim — do this BEFORE any web search.

### STEP 2 — Verify the entry

- Search for the paper by its title using web search (Google Scholar, Semantic Scholar, DBLP, arXiv, or publisher website).
- Cross-check EVERY field against the authoritative source:
  - `title` — exact wording and capitalization
  - `author` — complete list, correct spelling, correct order
  - `year`
  - `journal` / `booktitle` / venue
  - `volume`, `number`, `pages` (if applicable)
  - `arxiv ID` / `DOI` (if applicable)
  - Entry type (`@article`, `@inproceedings`, etc.)

### STEP 3 — Save verification result

Save to `./bib-verify/[cite-key].md`:

```markdown
# Verification: [cite-key]

## Original BibTeX Entry
(paste the original entry verbatim)

## Verification Source
(URL of the authoritative source used)

## Field-by-Field Check
| Field | Original | Verified | Match? |
|-------|----------|----------|--------|
| title | ... | ... | ✅/❌ |
| author | ... | ... | ✅/❌ |
| year | ... | ... | ✅/❌ |
| venue | ... | ... | ✅/❌ |
| ... | ... | ... | ... |

## Verdict: [CORRECT / HAS ERRORS / NEEDS UPDATE / NOT FOUND]

## Suggested Fix
(If verdict is not CORRECT, provide the corrected BibTeX entry. Otherwise write "No fix needed.")
```

### STEP 4 — Update index and loop

1. Update the entry in `index.json`: set `"status": "done"`, add `"verdict"` and `"summary"` fields.
2. **Go back to STEP 1** and claim the next pending entry.
3. Continue looping until you have processed **5 entries** in this run, OR no pending entries remain.

### STEP 5 — Final Report (when all entries are done)

When no `"pending"` or `"in_progress"` entries remain, create `./bib-verify/REPORT.md`:

```markdown
# Citation Verification Report

## Summary
- Total entries: [N]
- CORRECT: [n]
- HAS ERRORS: [n]
- NEEDS UPDATE: [n]
- NOT FOUND: [n]

## Entries with Errors
(List each entry with errors and the corrected BibTeX)

## Corrected BibTeX (combined)
(All corrected entries in a single block, ready for copy-paste into references.bib)
```

---

## Rules

- **CLAIM BEFORE SEARCH**: Always write `"in_progress"` to `index.json` BEFORE doing any web search. This prevents other agents from picking the same entry.
- **Skip `in_progress` entries**: If another agent claimed it, move on.
- **Stale claims**: If an entry has been `"in_progress"` for more than 30 minutes (check `claimed_at`), you may reclaim it.
- **Batch limit**: Process up to 5 entries per run to avoid timeout. Then stop gracefully.
- **Always verify against real online sources** — NEVER guess from memory.
- **Write all output in ENGLISH.**
