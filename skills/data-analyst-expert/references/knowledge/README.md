# Knowledge Files — data-analyst-expert

This folder contains business knowledge documents exported from Google Drive.
They are used by the skill to answer questions about experiment methodology,
pricing strategy, and decision-making processes — context that cannot be derived
from BigQuery schema alone.

## What lives here

| File | Source | Content |
|------|--------|---------|
| `pricing_experiment_knowledge_hub.md` | Google Slides | AB test methodology, data normalization, extrapolation logic, top experiments by month |
| `pricing_action_standards_process.md` | Google Slides | Pricing experiment decision framework, segmentation, action standards process |

## How the skill uses these files

The skill consults these files when the question is about:
- experiment methodology (how tests are designed, measured, or evaluated)
- pricing action standards (PAS compliance, decision criteria)
- how metrics like FLGPO, iAP, iOrders are calculated
- how results are extrapolated from test traffic to full market

These files are NOT consulted for every query — only when relevant to the
business question at hand.

## How to add a new document

### Step 1 — Add the file to Google Drive

Place the new Google Doc or Google Slides in the Drive folder:
`My Drive/claude-skills/data-analyst-expert/references/`

Folder ID: `14YTH1dMZEcZHRNQt5GjoJTo6xX_j4l44`

### Step 2 — Add it to the sync script

Open `skills/data-analyst-expert/sync_knowledge.py` and add a new entry
to the `FILES` dictionary:

```python
FILES = {
    "1RusXHimR7rrgc8U2gvLyk47lUXSsvciGmIv_shcWozA": "pricing_experiment_knowledge_hub",
    "15ndalILUVoUP6HbHmCaqARDNI7BtFbSRm26eUdpLlV8": "pricing_action_standards_process",
    "YOUR_NEW_FILE_ID": "your_descriptive_filename",   # ← add here
}
```

The file ID is in the Google Drive URL:
- Slides: `https://docs.google.com/presentation/d/FILE_ID/edit`
- Docs: `https://docs.google.com/document/d/FILE_ID/edit`

### Step 3 — Run the sync

```bash
python3 skills/data-analyst-expert/sync_knowledge.py
```

This exports all files from Drive and saves them to:
- `skills/data-analyst-expert/references/knowledge/` (source)
- `.claude/skills/data-analyst-expert/references/knowledge/` (active copy used by skill)

### Step 4 — Update SKILL.md

Tell the skill when to use the new file. Open `skills/data-analyst-expert/SKILL.md`
and add a line to the knowledge section:

```markdown
- `references/knowledge/your_descriptive_filename.md` — brief description of what's in it
```

### Step 5 — Commit and push

```bash
git add skills/data-analyst-expert/references/knowledge/
git add skills/data-analyst-expert/sync_knowledge.py
git add skills/data-analyst-expert/SKILL.md
git commit -m "Add [document name] to skill knowledge base"
git push
```

## How to update an existing document

If the source slides have been updated in Google Drive, just re-run the sync:

```bash
python3 skills/data-analyst-expert/sync_knowledge.py
```

Then commit the updated `.md` files.

## Technical notes

- Supported source types: Google Slides, Google Docs (exported as plain text)
- Google Sheets are not ideal — prefer exporting relevant tables manually
- PDFs are not supported by this sync script
- Authentication uses your existing `gcloud auth` session — no additional setup needed
- If you get an SSL error, the script already handles it via `ssl.CERT_NONE`
- If you get a 401 error, refresh your gcloud session: `gcloud auth login --enable-gdrive-access`
