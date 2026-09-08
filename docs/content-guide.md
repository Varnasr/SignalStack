# Content guide

## archive/

One file per post, `YYYY-MM-DD-slug.md`. Front matter carries `title`,
`date`, `type` (edition, daily, brief, other), `url` and `subtitle`. The body
is the post converted from HTML: headings, paragraphs, lists, quotes, links,
emphasis, images by URL.

`README.md` is the index. `SECTIONS.md` lists where each recurring section
appears.

The text is as published. Errors in it are listed in `companions/errata.md`.

## companions/

Eight generated pages, one per recurring section. An entry is one note, one
glossary term, one person, or one edition's list, with a line naming the
edition and date. A person mentioned in several editions has one entry
listing each mention.

## tools/

Four scripts. Each has a docstring naming the edition and the formula,
functions that can be imported, a command line, and tests.

## Not included

Summaries of editions. Edits to the newsletter's text. Content from any
source other than the newsletter.
