#!/usr/bin/env bash
# Local equivalent of the GitHub Actions build: runs `jekyll build`, then
# copies rmd/ and templates/ into _site/ verbatim (they're excluded from
# Jekyll's own processing -- see the comment in _config.yml -- so this copy
# step is what makes the "Download" links on each lab page work).
#
# Usage: scripts/build_site.sh [extra jekyll build args]
set -euo pipefail
cd "$(dirname "$0")/.."

bundle exec jekyll build "$@"

mkdir -p _site/rmd _site/templates
cp -r rmd/. _site/rmd/
cp -r templates/. _site/templates/

echo "Built _site/ (with rmd/ and templates/ copied in verbatim)."
