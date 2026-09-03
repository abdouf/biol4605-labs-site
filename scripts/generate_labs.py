#!/usr/bin/env python3
"""
Generate all per-week lab files from a single source of truth.

Reads:
    _data/labs.yml            -- the 13-week schedule
    templates/lab_template.Rmd -- the standardized R Markdown template

Writes:
    rmd/labNN-<slug>.Rmd        -- one starter R Markdown file per week
    _labs/NN-<slug>.md          -- one Just the Docs page per week

Re-run this any time you edit _data/labs.yml or templates/lab_template.Rmd
to regenerate every lab page/file consistently. It OVERWRITES existing
rmd/*.Rmd and _labs/*.md files -- commit or stash lab-specific edits you
want to keep before re-running, or move that lab's edits out of the
generator's placeholder tags.

Usage:
    python3 scripts/generate_labs.py
"""
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "_data" / "labs.yml"
TEMPLATE_FILE = ROOT / "templates" / "lab_template.Rmd"
RMD_DIR = ROOT / "rmd"
LABS_DIR = ROOT / "_labs"


def load_labs():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["labs"]


def render_rmd(template_text: str, lab: dict) -> str:
    note = lab.get("note") or ""
    note_block = f"> **Note:** {note}\n" if note.strip() else ""
    replacements = {
        "{{WEEK}}": str(lab["week"]),
        "{{LAB_LABEL}}": lab["lab_label"],
        "{{TITLE}}": lab["title"],
        "{{MODULE}}": lab["module"],
        "{{FOCUS}}": lab["focus"],
        "{{DELIVERABLE}}": lab["deliverable"],
        "{{SOFTWARE}}": lab["software"],
        "{{NOTE_BLOCK}}": note_block,
    }
    text = template_text
    for token, value in replacements.items():
        text = text.replace(token, value)
    return text


LAB_PAGE_TEMPLATE = """---
layout: default
title: "Week ??WEEK?? — ??LAB_LABEL??: ??TITLE??"
parent: Labs
nav_order: ??WEEK??
permalink: /labs/??WEEK_PADDED??/
---

# Week ??WEEK?? — ??LAB_LABEL??: ??TITLE??

**Module:** ??MODULE??
??NOTE_LINE??
> ??FOCUS??
{: .objectives }

**Key deliverable:** ??DELIVERABLE??
**Software / functions:** `??SOFTWARE??`

## Starter file

[Download ??RMD_BASENAME??]({{ '/??RMD_FILE??' | relative_url }}){: .btn .btn-blue }

Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
editing. This file is generated from
[`templates/lab_template.Rmd`]({{ '/templates/lab_template.Rmd' | relative_url }})
-- structure and section headings are standardized across all 13 labs.

[Back to schedule]({{ '/schedule/' | relative_url }})
"""


def render_lab_page(lab: dict) -> str:
    week_padded = lab.get("week_padded") or f"{lab['week']:02d}"
    note_line = f"\n**Note:** {lab['note']}\n" if lab.get("note") else ""
    replacements = {
        "??WEEK_PADDED??": week_padded,
        "??WEEK??": str(lab["week"]),
        "??LAB_LABEL??": lab["lab_label"],
        "??TITLE??": lab["title"],
        "??MODULE??": lab["module"],
        "??FOCUS??": lab["focus"],
        "??DELIVERABLE??": lab["deliverable"],
        "??SOFTWARE??": lab["software"],
        "??NOTE_LINE??": note_line,
        "??RMD_FILE??": lab["rmd_file"],
        "??RMD_BASENAME??": pathlib.Path(lab["rmd_file"]).name,
    }
    text = LAB_PAGE_TEMPLATE
    for token, value in replacements.items():
        text = text.replace(token, value)
    return text


def main():
    labs = load_labs()
    template_text = TEMPLATE_FILE.read_text(encoding="utf-8")

    RMD_DIR.mkdir(parents=True, exist_ok=True)
    LABS_DIR.mkdir(parents=True, exist_ok=True)

    for lab in labs:
        week_padded = lab.get("week_padded") or f"{lab['week']:02d}"

        # 1. R Markdown starter file
        rmd_text = render_rmd(template_text, lab)
        rmd_path = ROOT / lab["rmd_file"]
        rmd_path.parent.mkdir(parents=True, exist_ok=True)
        rmd_path.write_text(rmd_text, encoding="utf-8")

        # 2. Jekyll lab page (Just the Docs child page under "Labs")
        page_text = render_lab_page(lab)
        page_path = LABS_DIR / f"{week_padded}-{lab['slug']}.md"
        page_path.write_text(page_text, encoding="utf-8")

        print(f"  week {lab['week']:>2}: {rmd_path.relative_to(ROOT)}  +  {page_path.relative_to(ROOT)}")

    print(f"\nGenerated {len(labs)} labs from {DATA_FILE.relative_to(ROOT)}.")


if __name__ == "__main__":
    sys.exit(main())
