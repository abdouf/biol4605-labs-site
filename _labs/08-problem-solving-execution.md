---
layout: default
title: "Week 8 — Lab 9b: Problem-Solving with GLM (Execution)"
parent: Labs
nav_order: 8
permalink: /labs/08/
---

# Week 8 — Lab 9b: Problem-Solving with GLM (Execution)

**Module:** Parts 3–5: Applied Integration

Location: CSF BIOL 2218B Computer Lab · Time: 3:00–6:00 PM

> Full analytical pipeline. Data cleaning, model fitting, model selection, diagnostic checking, and biological interpretation.
{: .objectives }

**Key deliverable:** Complete R script / R Markdown report
**Software / functions:** `Full tidyverse + lm()/glm() pipeline`

This lab's instructions and exercises are Dr. David C. Schneider's original
**"Problem-Solving with GLM "** lab, unchanged from his site:

[Open Lab 9b (PDF) on Dr. Schneider's site ↗](https://davidcschneider.github.io/StatisticalScience/Labs/Lab09b.pdf){:target="_blank" .btn .btn-outline }

## Lab materials (Data)

[Open wireworms 1 data (Snedecor and Cochran 1980 p. 289) on Dr. Schneider's site ↗](https://github.com/DavidCSchneider/StatisticalScience/blob/main/Data/Labs/wworm1.txt){:target="_blank" .btn .btn-outline }

[Open wireworms 2 data (Snedecor and Cochran 1980 p. 273) on Dr. Schneider's site ↗](https://github.com/DavidCSchneider/StatisticalScience/blob/main/Data/Labs/wworm2.txt){:target="_blank" .btn .btn-outline }

[Open Leprosy bacilli data on Dr. Schneider's site ↗](https://github.com/DavidCSchneider/StatisticalScience/blob/main/Data/Labs/LeprosyScores.txt){:target="_blank" .btn .btn-outline }

## Starter file

{% assign this_lab = site.data.labs.labs | where: "week", 8 | first %}
{% if this_lab.downloadable %}
 [Download lab09b-problem-solving-execution.Rmd]({{ '/rmd/lab09b-problem-solving-execution.Rmd' | relative_url }}){: .btn .btn-blue }

 Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
 editing.
{% else %}
_Materials for this lab will be posted here a few hours before the session._
{% endif %}

 [Back to schedule]({{ '/schedule/' | relative_url }})
