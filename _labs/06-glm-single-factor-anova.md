---
layout: default
title: "Week 6 — Lab 6a/b: GLM – Single Factor ANOVA"
parent: Labs
nav_order: 6
permalink: /labs/06/
---

# Week 6 — Lab 6a/b: GLM – Single Factor ANOVA

**Module:** Part 3: The General Linear Model – Single Explanatory Variable

Location: CSF BIOL 2218B Computer Lab · Time: 3:00–6:00 PM

> Group comparison models. Factor coding, sum of squares decomposition, variance partitioning, and post-hoc contrasts.
{: .objectives }

**Key deliverable:** ANOVA table with post-hoc contrasts
**Software / functions:** `lm(), anova(), emmeans package`

This lab's instructions and exercises are Dr. David C. Schneider's original
**"GLM - Single Factor ANOVA "** lab, unchanged from his site:

[Open Lab 6 (PDF) on Dr. Schneider's site ↗](https://davidcschneider.github.io/StatisticalScience/Labs/Lab06ab.pdf){:target="_blank" .btn .btn-outline }

## Lab materials (Data)

[Open Daphnia ages data (Box 9.5 in Sokal and Rohlf, 1995) on Dr. Schneider's site ↗](https://raw.githubusercontent.com/DavidCSchneider/StatisticalScience/refs/heads/main/Data/Labs/DaphniaAges.txt){:target="_blank" .btn .btn-outline }

[Open Fly wing lengths data (Table 8.1 in Sokal and Rohlf, 2012) on Dr. Schneider's site ↗](https://raw.githubusercontent.com/DavidCSchneider/StatisticalScience/refs/heads/main/Data/Labs/FlyWings.txt){:target="_blank" .btn .btn-outline }

[Open Cod movements data (Cod movements by hour of day) on Dr. Schneider's site ↗](https://raw.githubusercontent.com/DavidCSchneider/StatisticalScience/refs/heads/main/Data/Labs/FishMove.txt){:target="_blank" .btn .btn-outline }

## Starter file

{% assign this_lab = site.data.labs.labs | where: "week", 6 | first %}
{% if this_lab.downloadable %}
 [Download lab06-glm-single-factor-anova.Rmd]({{ '/rmd/lab06-glm-single-factor-anova.Rmd' | relative_url }}){: .btn .btn-blue }

 Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
 editing.
{% else %}
_Materials for this lab will be posted here a few hours before the session._
{% endif %}

 [Back to schedule]({{ '/schedule/' | relative_url }})
