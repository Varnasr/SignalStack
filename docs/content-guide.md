# Content guide

## archive/

One file per post, named `YYYY-MM-DD-slug.md`. Front matter carries
`title`, `date`, `type` (edition, daily, brief, other), `url` (the Substack
original) and `subtitle`. The body is the post's HTML converted to Markdown:
headings, paragraphs, lists, blockquotes, links, emphasis, images by URL.
Substack's button and embed wrappers become links.

`README.md` is the index, newest first. `SECTIONS.md` lists where each
recurring section appears, so you can follow Research praxis or Researchers
worth following across every edition.

The text is the newsletter's. Typos and the corrupted words in the August
2025 edition are in the Substack source and are kept; `companions/errata.md`
records them.

## companions/

Eight generated pages, one per recurring section. An entry is one note, one
glossary term, one person, or one edition's reading list, with a source line
naming the edition and date. `researchers.md` merges a person mentioned in
several editions into one entry that lists every mention.

Where a section's heading conventions changed between years, the builder
reconciles them; the rules are documented in `scripts/build_companions.py`.

## tools/

Four scripts with a shared shape: a docstring naming the edition and the
formula, functions that can be imported, a command line, and tests pinned to
closed-form answers or cited figures. `tools/README.md` describes each.

## What is deliberately not here

Summaries. The archive is the full text, and a summary of a newsletter that
is itself a digest adds a layer of loss. Editorial additions to the
newsletter's text: corrections go in `errata.md`, not in the archive.
Content from any source other than the newsletter.
