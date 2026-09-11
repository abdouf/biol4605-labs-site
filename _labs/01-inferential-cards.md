---
layout: default
title: "Week 1 — Lab 1: Inferential Cards"
parent: Labs
nav_order: 1
permalink: /labs/01/
---

# Week 1 — Lab 1: Inferential Cards

**Module:** Part 1: Quantitative Background

Location: CSF BIOL 2218B Computer Lab · Time: 3:00–6:00 PM

> Hands-on sampling & statistical inference. Understanding variability, hypothesis testing, and standard errors using physical playing cards.
{: .objectives }

**Key deliverable:** Manual data collection worksheet
**Software / functions:** `None (physical cards; worksheet only)`

## Lab materials

This lab's instructions and exercises are Dr. Schneider's original
**"Inferential Cards"** lab, unchanged from his site:

[Open Lab 1 (PDF) on Dr. Schneider's site ↗](https://davidcschneider.github.io/StatisticalScience/Labs/Lab01.pdf){:target="_blank" .btn .btn-outline }

**What the session covers, in brief** (see the PDF above for the exact
wording and full instructions your group will follow):

- **Exercise 1: Random Card Method:** draw cards at random and use the
  resulting variability to build intuition for sampling error and standard
  errors before any hypothesis is involved.
- **Exercise 2: Selected Card Method:** deliberately select cards rather
  than drawing at random, and compare what that does to the same
  calculations. The contrast is the point of the exercise.
- **Exercise 3: Platt Decision Tree Method:** apply Platt's strong-inference
  logic (devise multiple competing hypotheses up front, then pick a
  "crucial" test card that can rule hypotheses out rather than merely
  confirm one) and work through at least one full H₁/H₂ → test → result
  decision tree.
- **Table 1.1:** each group's shared recording table across all three
  methods (Random / Selected / Crucial test columns).
- **Hand-in:** completed Table 1.1, one worked decision-tree example, a short
  written comparison of the three methods, and answers to the lab's
  discussion questions.

**Materials to bring:** each group (group of 3 students) needs one standard deck of playing cards
(52 cards; jokers can be set aside). A regular deck works fine

 ## Starter file

+{% assign this_lab = site.data.labs.labs | where: "week", 1 | first %}
+{% if this_lab.downloadable %}
 [Download lab01-inferential-cards.Rmd]({{ '/rmd/lab01-inferential-cards.Rmd' | relative_url }}){: .btn .btn-blue }

 Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
 editing.
+{% else %}
+_Materials for this lab will be posted here a few hours before the session._
+{% endif %}

 [Back to schedule]({{ '/schedule/' | relative_url }})
