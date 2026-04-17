#!/usr/bin/env python3
"""
Sync Google Drive slides to references/knowledge/ for the data-analyst-expert skill.
Run this script whenever the source slides are updated.

Usage:
    python3 skills/data-analyst-expert/sync_knowledge.py
"""

import urllib.request
import json
import ssl
import subprocess
import os
import shutil
from datetime import datetime

# --- Config ---
FILES = {
    "1RusXHimR7rrgc8U2gvLyk47lUXSsvciGmIv_shcWozA": "pricing_experiment_knowledge_hub",
    "15ndalILUVoUP6HbHmCaqARDNI7BtFbSRm26eUdpLlV8": "pricing_action_standards_process",
}

SKILL_ROOT = os.path.join(os.path.dirname(__file__))
OUTPUT_DIRS = [
    os.path.join(SKILL_ROOT, "references", "knowledge"),
    os.path.join(os.path.dirname(SKILL_ROOT), "..", ".claude", "skills", "data-analyst-expert", "references", "knowledge"),
]
# --- End Config ---

def get_ssl_context():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def get_token():
    return subprocess.check_output(["gcloud", "auth", "print-access-token"]).decode().strip()

def export_file(file_id, token, ctx):
    url = f"https://www.googleapis.com/drive/v3/files/{file_id}/export?mimeType=text/plain"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    return urllib.request.urlopen(req, context=ctx).read().decode("utf-8")

def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Syncing knowledge files from Google Drive...\n")
    ctx = get_ssl_context()
    token = get_token()

    for output_dir in OUTPUT_DIRS:
        os.makedirs(output_dir, exist_ok=True)

    for file_id, filename in FILES.items():
        print(f"  Exporting: {filename}...")
        try:
            content = export_file(file_id, token, ctx)
            for output_dir in OUTPUT_DIRS:
                path = os.path.join(output_dir, f"{filename}.md")
                with open(path, "w") as f:
                    f.write(content)
            print(f"  Saved ({len(content):,} chars) → references/knowledge/{filename}.md")
        except Exception as e:
            print(f"  ERROR: {e}")

    print("\nDone. Remember to commit the changes to git.")

if __name__ == "__main__":
    main()
