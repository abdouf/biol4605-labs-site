#!/usr/bin/env ruby
# Copy only "released" lab .Rmd files into _site/rmd/ during the GitHub
# Pages build.
#
# _data/labs.yml's `downloadable` flag controls this per week. A lab marked
# downloadable: false has its .Rmd file left OUT of _site/ entirely -- not
# just unlinked from the page, genuinely absent from the published site --
# so there's no URL a student could guess or bookmark to get it early.
#
# Uses only Ruby's standard library (yaml, fileutils) so it needs no extra
# gems beyond what ruby/setup-ruby + bundler-cache already provide in the
# workflow.
#
# Run from the repo root (that's what .github/workflows/pages.yml does):
#   ruby scripts/copy_released_rmd.rb

require "yaml"
require "fileutils"

root = File.expand_path("..", __dir__)
data = YAML.load_file(File.join(root, "_data", "labs.yml"))
labs = data["labs"]

released = []
withheld = []

labs.each do |lab|
  src = File.join(root, lab["rmd_file"])
  dest = File.join(root, "_site", lab["rmd_file"])

  if lab["downloadable"]
    FileUtils.mkdir_p(File.dirname(dest))
    FileUtils.cp(src, dest)
    released << lab["rmd_file"]
  else
    withheld << lab["rmd_file"]
  end
end

puts "Copied #{released.size} released lab file(s) into _site/:"
released.each { |f| puts "  + #{f}" }
puts "Withheld #{withheld.size} not-yet-released lab file(s) (left out of _site/ entirely):"
withheld.each { |f| puts "  - #{f}" }
