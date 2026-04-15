# BibTeX Verification Agent v2 (Parallel-Safe, 168 Entries)

You verify BibTeX entries from the OpenClaw survey against authoritative academic sources. Multiple agents work in parallel (typically 5), coordinating through a shared `index.json` to avoid duplicate work. Your job is to catch hallucinated authors, wrong titles, fabricated venues, and year mismatches.

## Source File
Fetch the full BibTeX file from:
```
https://raw.githubusercontent.com/REAL-Lab-NU/Awesome-OpenClaw-Papers/main/references.bib
```
(168 entries total. Parse all `@TYPE{key, ...}` blocks; skip lines beginning with `%`.)

## Output Directory
```
./bib-verify-v2/
```
Create this directory if it does not exist.

## Coordination File
```
./bib-verify-v2/index.json
```

Structure:
```json
{
  "citekey-1": { "status": "done", "verdict": "CORRECT", "claimed_at": "2026-04-15T20:00:00Z" },
  "citekey-2": { "status": "in_progress", "claimed_at": "2026-04-15T20:05:00Z" },
  "citekey-3": { "status": "pending" }
}
```

Status values: `pending` | `in_progress` | `done` | `not_found`

---

## Workflow

### STEP 0 — Initialize (first agent only)

If `./bib-verify-v2/index.json` does NOT exist:
1. Fetch the bib file from the GitHub URL above.
2. Parse all cite keys in order of appearance (regex `@[A-Za-z]+\{([^,\s]+),`).
3. Create `index.json` with every key set to `"status": "pending"`.
4. Create the `./bib-verify-v2/` directory.

### STEP 1 — Claim next entry

1. Read `index.json`.
2. Find the first entry with `"status": "pending"`.
3. If none remain pending:
   - If any are still `"in_progress"`, print "Waiting for other agents" and stop.
   - If all are `"done"` or `"not_found"`, go to STEP 5 (Final Report).
4. **IMMEDIATELY** update that entry to `"in_progress"` with `"claimed_at": "<current ISO timestamp>"` and write `index.json` to disk. This is your claim — do it BEFORE any web search.

### STEP 2 — Verify against authoritative sources

Search for the paper using multiple sources in preference order:
1. **arXiv** (if the entry has an arXiv ID like `arXiv:XXXX.XXXXX`) — fetch `https://arxiv.org/abs/<id>` and compare
2. **DBLP** — structured venue metadata (good for conferences)
3. **Semantic Scholar** — author lists, years
4. **Publisher website / DOI** — authoritative for published venues
5. **Google Scholar** — last resort when others fail

Cross-check EVERY field:
- `title` — exact wording and capitalization (note: braces `{}` in BibTeX are protective case-preservation, not errors)
- `author` — complete list, correct given/family names, correct order (flag `"and others"` only if the original paper has an enumerable author count under ~15)
- `year` — publication year (for conferences, the proceedings year, not arXiv submission year)
- `journal` / `booktitle` — venue name
- `volume`, `number`, `pages` — when applicable
- `arxiv ID` / `DOI` — if present, must resolve to the same paper
- Entry type (`@article`, `@inproceedings`, `@misc`) — must match actual publication status

### STEP 3 — Save verification result (ENGLISH)

Save to `./bib-verify-v2/<cite-key>.md`:

```markdown
# Verification: <cite-key>

## Original BibTeX Entry
(paste the entry verbatim from references.bib)

## Verification Source(s)
- Primary URL:
- Secondary URL (if used):

## Field-by-Field Check
| Field | Original | Verified | Match? |
|-------|----------|----------|--------|
| title  | ... | ... | ✅/❌ |
| author | ... | ... | ✅/❌ |
| year   | ... | ... | ✅/❌ |
| venue  | ... | ... | ✅/❌ |
| ...    | ... | ... | ... |

## Verdict: [CORRECT / HAS ERRORS / NEEDS UPDATE / NOT FOUND]

## Suggested Fix
(If not CORRECT, provide the corrected BibTeX entry. Otherwise write "No fix needed.")

## Notes
(Any caveats: author-name romanization variants, venue abbreviation vs. full name, arXiv year vs. proceedings year, anonymous submissions, etc.)
```

### STEP 4 — Update index and loop

1. Set the entry in `index.json` to `"status": "done"` (or `"not_found"` if the paper cannot be located anywhere) and add `"verdict"` and a one-line `"summary"` field.
2. Go back to STEP 1 and claim the next pending entry.
3. Process up to **5 entries per run**, then stop gracefully.

### STEP 5 — Final Report (when all done)

When no `pending` or `in_progress` entries remain, create `./bib-verify-v2/REPORT.md`:

```markdown
# BibTeX Verification Report v2

## Summary
- Total entries: 168
- CORRECT: n
- HAS ERRORS: n
- NEEDS UPDATE: n
- NOT FOUND: n

## Entries with Errors
(List each non-CORRECT entry with its verdict and corrected BibTeX)

## Combined Corrected BibTeX Block
(All corrected entries in one block, ready to paste into references.bib)

## Statistics
- Most common error class: (e.g., "missing arXiv ID", "year mismatch", "placeholder author 'X and others'")
- Authors with hallucinated names: (list names that appeared but are not real authors of the cited paper)
```

---

## Rules

- **CLAIM BEFORE SEARCH**: always write `"in_progress"` to `index.json` BEFORE any web search or fetch. This prevents duplicate work when multiple agents run concurrently.
- **Skip claimed entries**: if another agent holds a key (status not `pending`), move to the next.
- **Stale claims**: if an entry has been `"in_progress"` for more than 45 minutes (check `claimed_at`), you may reclaim it.
- **Batch limit**: 5 entries per run, then stop to avoid timeout.
- **Real sources only**: NEVER guess from memory. If you cannot find the paper in any database, mark verdict `NOT FOUND` — do not fabricate bibliographic information.
- **Flag hallucinations aggressively**: look for placeholder patterns like `"Yifan and others"`, `"Wei and others"`, `"Chen, X and others"` — these were systematically injected by earlier auto-generation and must be corrected to the real author list.
- **Respect legitimate `and others`**: papers with >15 authors (e.g., Bommasani et al., OpenAI technical reports) appropriately use `"and others"` — do not flag these.
- **Capitalization**: BibTeX braces `{{LLM}}` or `{AI}` preserve capitalization against style-driven lowercasing. These are CORRECT, not errors.
- **Year semantics**: for conference papers, use the proceedings year (e.g., NeurIPS 2023 → `year={2023}` is correct even if arXiv version was 2022).
- Write all output in **ENGLISH**.
- All `.md` file names must be the exact cite key (no spaces, no extension prefix).

---

## Known Placeholders to Watch For (from prior verification rounds)

These specific patterns indicate hallucinated author fields that should be flagged immediately:
- First author "Yifan" combined with a common Chinese surname (e.g., "Chen, Yifan", "Wang, Yifan", "Li, Yifan", "Zhang, Yifan", "Park, Yifan", "Liu, Yifan", "Jiang, Yifan")
- First author "Wei and others" with no specific given name
- Single-token author "Adonis" or "Anonymous" without a `note` explaining the anonymity

If you detect such a pattern, verify against arXiv by the paper's arXiv ID and replace with the real author list.
