---
layout: default
title: "Week 7 — Lab 9a: Problem-Solving with GLM (Setup)"
parent: Labs
nav_order: 7
permalink: /labs/07/
---

# Week 7 — Lab 9a: Problem-Solving with GLM (Setup)

**Module:** Parts 3–5: Applied Integration

Location: CSF BIOL 2218B Computer Lab · Time: 3:00–6:00 PM

> Experimental setup & data structuring. Formulating research questions into verifiable statistical architecture prior to execution.
{: .objectives }

**Key deliverable:** Model structure & DAGs / worksheets
**Software / functions:** `R Markdown planning worksheet (no analysis code yet)`

This lab's instructions and exercises are Dr. David C. Schneider's original
**"Problem-Solving with GLM "** lab, unchanged from his site:

[Open Lab 9a (PDF) on Dr. Schneider's site ↗](https://davidcschneider.github.io/StatisticalScience/Labs/Lab09a.pdf){:target="_blank" .btn .btn-outline }

## Lab materials (Data)

[Open wireworms 1 data (Snedecor and Cochran 1980 p. 289) on Dr. Schneider's site ↗](https://github.com/DavidCSchneider/StatisticalScience/blob/main/Data/Labs/wworm1.txt){:target="_blank" .btn .btn-outline }

[Open wireworms 2 data (Snedecor and Cochran 1980 p. 273) on Dr. Schneider's site ↗](https://github.com/DavidCSchneider/StatisticalScience/blob/main/Data/Labs/wworm2.txt){:target="_blank" .btn .btn-outline }

[Open Leprosy bacilli data on Dr. Schneider's site ↗](https://github.com/DavidCSchneider/StatisticalScience/blob/main/Data/Labs/LeprosyScores.txt){:target="_blank" .btn .btn-outline }

## Starter file

{% assign this_lab = site.data.labs.labs | where: "week", 7 | first %}
{% if this_lab.downloadable %}
 [Download lab09a-problem-solving-setup.Rmd]({{ '/rmd/lab09a-problem-solving-setup.Rmd' | relative_url }}){: .btn .btn-blue }

 Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
 editing.
{% else %}
_Materials for this lab will be posted here a few hours before the session._
{% endif %}

 [Back to schedule]({{ '/schedule/' | relative_url }})
