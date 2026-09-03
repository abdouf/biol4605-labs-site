---
title: Resources
layout: default
nav_order: 5
permalink: /resources/
---

# Resources
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Primary course references

- Dr. Amy Hurford's lecture notes for the current offering:
  [BIOL/OCSC 4605 · 7220 course site](https://ahurford.github.io/biol-4605-f26/){:target="_blank"}
  (Fall 2026). This lab site follows the same weekly pacing.
- Dr. David C. Schneider's original course site, [*Statistical Science*](https://davidcschneider.github.io/StatisticalScience/){:target="_blank"}.
  Dr Schneider developed the six-part curriculum (*Statistical Analysis in Biology and
  Environmental Science*) both the lectures and this lab sequence are built
  on. Kept here for reference only; it is not the current course site.

## Software

- [R](https://cran.r-project.org/){:target="_blank"} (≥ 4.3 recommended)
- [RStudio Desktop](https://posit.co/download/rstudio-desktop/){:target="_blank"}
- R Markdown (bundled with RStudio); confirm with `rmarkdown::pandoc_version()`

### Core packages used across the term

```r
install.packages(c(
  "rmarkdown",   # knit labs to HTML
  "tidyverse",   # dplyr / ggplot2 / readr, etc.
  "emmeans",     # post-hoc contrasts (Lab 6a/b)
  "car",         # Type II/III ANOVA, diagnostics (Labs 7-8)
  "boot",        # bootstrap resampling (Lab 11)
  "broom",       # tidy model output
  "here"         # project-relative file paths
))
```

## Getting help

- Office hours: CSF 2211 Tuesday 9:00 AM to 5:00 PM
- Course discussion board / email: amf347@mun.ca
- R debugging first step: read the error message top line, then check
  `traceback()`. Most lab errors are a missing package or a mismatched
  column name.
