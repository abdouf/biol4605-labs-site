---
layout: default
title: "Week 4 — Lab 4: Probability Values by Randomization"
parent: Labs
nav_order: 4
permalink: /labs/04/
---

# Week 4 — Lab 4: Probability Values by Randomization

**Module:** Part 2: Quantifying Uncertainty

Location: CSF BIOL 2218B Computer Lab · Time: 3:00–6:00 PM

> Non-parametric / permutation tests. Empirical p-value computation via Monte Carlo reshuffling of observational data.
{: .objectives }

**Key deliverable:** Custom simulation loops in R
**Software / functions:** `Base R (for/replicate loops); no external package required`

## Lab materials (instructions)

This lab's instructions and exercises are Dr. David C. Schneider's original
**"Probability Values by Randomization "** lab, unchanged from his site:

[Open Lab 4 (PDF) on Dr. Schneider's site ↗](https://davidcschneider.github.io/StatisticalScience/Labs/Lab04.pdf){:target="_blank" .btn .btn-outline }

## Lab materials (Data)

[Open Daphnia Data (Box 9.5 in Sokal and Rohlf 1995) on Dr. Schneider's site ↗](https://github.com/DavidCSchneider/StatisticalScience/blob/main/Data/Labs/DaphniaAges.txt){:target="_blank" .btn .btn-outline }

[Open Guinea Pig Data (Box 13.12 of Sokal and Rohlf (1995) on Dr. Schneider's site ↗](https://github.com/DavidCSchneider/StatisticalScience/blob/main/Data/Labs/LitterSize.txt){:target="_blank" .btn .btn-outline }

## Starter file

{% assign this_lab = site.data.labs.labs | where: "week", 4 | first %}
{% if this_lab.downloadable %}
 [Download lab04-probability-values-randomization.Rmd]({{ '/rmd/lab04-probability-values-randomization.Rmd' | relative_url }}){: .btn .btn-blue }

 Open it in RStudio and knit to HTML (or PDF) to confirm it runs before
 editing.
{% else %}
_Materials for this lab will be posted here a few hours before the session._
{% endif %}

 [Back to schedule]({{ '/schedule/' | relative_url }})
