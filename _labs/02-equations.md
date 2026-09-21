---
layout: default
title: "Week 2 — Lab 2: Equations"
parent: Labs
nav_order: 2
permalink: /labs/02/
---

# Week 2 — Lab 2: Equations

**Module:** Part 1: Quantitative Background

Location: CSF BIOL 2218B Computer Lab · Time: 3:00–6:00 PM

> Translating biological concepts into mathematical models. Defining response variables, parameters, and error structure.
{: .objectives }

**Key deliverable:** LaTeX / math notation in R Markdown
**Software / functions:** `R Markdown + LaTeX math syntax`

## Lab materials

This lab's instructions and exercises are Dr. David C. Schneider's original
**"Using Equations"** lab, unchanged from his site:

[Open Lab 2 (PDF) on Dr. Schneider's site ↗](https://davidcschneider.github.io/StatisticalScience/Labs/Lab02.pdf){:target="_blank" .btn .btn-outline }

[Find scientific literature here for your Lab2 Example 4 ↗](https://github.com/DavidCSchneider/StatisticalScience/tree/main/Data){:target="_blank" .btn .btn-outline }

## Starter file

{% assign this_lab = site.data.labs.labs | where: "week", 2 | first %}
{% if this_lab.downloadable %}
 [Download lab02-equations.Rmd]({{ '/rmd/lab02-equations.Rmd' | relative_url }}){: .btn .btn-blue }

 Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
 editing.
{% else %}
_Materials for this lab will be posted here a few hours before the session._
{% endif %}

 [Back to schedule]({{ '/schedule/' | relative_url }})
