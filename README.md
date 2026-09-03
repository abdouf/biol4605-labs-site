# BIOL/OCSC 4605 · 7220 — Course Site & Lab Templates

Starter GitHub Pages site + standardized R Markdown lab template for
<<<<<<< HEAD
**Statistical Analysis in Biology and Environmental Science**, structured
around Dr. A. Hurford [*Statistical Analysis in Biology and Environmental Science*] lecture syllabus. Both the Labs and the Lectures are built around Dr. D. C. Schneider's curriculum [*Statistical Science*](https://davidcschneider.github.io/StatisticalScience/)
=======
**Statistical Analysis in Biology and Environmental Science** (BIOL/OCSC 4605 · 7220).
This repo builds the **Labs** portion of the course; lectures for the current
offering are delivered separately by Dr. Amy Hurford
([lecture notes](https://ahurford.github.io/biol-4605-f26/)). Both the labs
and the lectures are built around Dr. David C. Schneider's original
curriculum, [*Statistical Science*](https://davidcschneider.github.io/StatisticalScience/),
kept there for reference.
>>>>>>> 6b0c2f6 (Fix broken links, remove duplicate deploy workflow, reconcile attribution)

Built with [Jekyll](https://jekyllrb.com/) + [Just the Docs](https://just-the-docs.com/),
deployed via GitHub Actions so it works on any GitHub repo without needing to
be on GitHub Pages' restricted theme list.

## What's in here

```
.
├── _config.yml              # site config -- EDIT title/url/baseurl/links first
├── Gemfile                  # Ruby deps (only needed for local preview)
├── .github/workflows/pages.yml   # builds + deploys on every push to main
├── index.md                 # home page
├── syllabus.md               # 6-part curriculum -> 13-week mapping
├── schedule.md               # full week-by-week table (rendered from _data/labs.yml)
├── resources.md               # software setup, packages, links
├── labs/index.md              # "Labs" parent nav page
├── _data/labs.yml             # single source of truth for the 13-week schedule
├── _labs/                     # generated: one Jekyll page per week (do not hand-edit headers)
├── rmd/                       # generated: one starter .Rmd per week (Body will be edited)
├── templates/lab_template.Rmd # master R Markdown template all labs are generated from
├── assets/css/course.css      # shared CSS knit into every lab's HTML output
└── scripts/generate_labs.py   # regenerates _labs/ and rmd/ from the template + data
```


## 1. Working with the lab schedule and templates

The 13 weeks are **data-driven**: `_data/labs.yml` holds every week's title,
module, focus, deliverable, and software, and `scripts/generate_labs.py`
turns that (plus `templates/lab_template.Rmd`) into the actual files.

**To change a date, deliverable, or objective across the site:** edit
`_data/labs.yml` — `schedule.md`, `labs/index.md`, and the per-week pages all
render from it.

**To change the standardized template all labs are generated from** (e.g.
add a new section, change the YAML output options, tweak the grading
checklist):

```bash
# 1. Edit templates/lab_template.Rmd
# 2. Regenerate every week's files
pip install pyyaml   # once
python3 scripts/generate_labs.py
```

This **overwrites** `rmd/*.Rmd` and `_labs/*.md`. Since real lab content
(exercises, data descriptions, questions) lives inside those generated
files, either:

- do your template edits *before* filling in each week's actual content, or
- keep a copy of any lab-specific edits (git makes this easy: `git stash`
  or check the diff) and re-apply them after regenerating, or
- edit that one lab's `rmd/labNN-*.Rmd` directly and skip the regenerate
  step (fine for one-off changes; just note the file will no longer track
  future template updates automatically).

**To add a 14th lab / a new course using this structure:** copy
`templates/lab_template.Rmd` as a starting point, or add an entry to
`_data/labs.yml` and re-run the generator.

## 2. Content depth in the generated labs

The generated `rmd/labNN-*.Rmd` files are **skeletal templates**: YAML
header, learning objectives, deliverable, and section scaffolding are
pre-filled from `_data/labs.yml`, but the actual walkthrough code, exercise
questions, and datasets are left as `(edit me)` placeholders for you or your
TAs to fill in against your real course material.

## 3. Attribution

<<<<<<< HEAD
Curriculum structure and part sequencing follow David C. Schneider,
[*Statistical Analysis in Biology and Environmental Science*](https://davidcschneider.github.io/StatisticalScience/).
=======
Curriculum structure and part sequencing originate from Dr. David C.
Schneider's course site, [*Statistical Science*](https://davidcschneider.github.io/StatisticalScience/)
(*Statistical Analysis in Biology and Environmental Science*, BIOL/OCSC
4605 · 7220) — kept here for reference, not the current course site.
Lectures for the current offering are delivered by Dr. Amy Hurford
([lecture notes](https://ahurford.github.io/biol-4605-f26/)); this repo
covers the labs.
>>>>>>> 6b0c2f6 (Fix broken links, remove duplicate deploy workflow, reconcile attribution)
