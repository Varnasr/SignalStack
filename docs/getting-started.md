# Getting started

## Read

No setup. Open [companions/](../companions/) for the compiled sections or
[archive/](../archive/) for editions as sent. On the site,
[varnasr.github.io/SignalStack](https://varnasr.github.io/SignalStack/).

## Run the tools

Python 3.10 or later. Nothing to install.

```bash
git clone https://github.com/Varnasr/SignalStack.git
cd SignalStack
python tools/poverty_lines.py --year 2024
python tools/deletion_rate.py --removed 4700000 --roll 78900000 --stage draft
```

## Run the tests

```bash
pip install pytest
python -m pytest tests/
python scripts/build_companions.py --check
```

## Sync the archive

```bash
python scripts/sync_substack.py --check     # exit 1 if Substack has posts we do not
python scripts/sync_substack.py             # fetch them
python scripts/build_companions.py          # recompile the companions
```

The sync reads the public Substack API; no key is needed. The monthly
workflow does the same and opens a pull request.

## Build the site locally

GitHub Pages builds it with Jekyll and `jekyll-readme-index`. Locally:

```bash
gem install bundler jekyll jekyll-readme-index
jekyll serve
```

Do not check links against `python -m http.server`: it serves directory
listings, so every folder link passes locally and fails in production. Build
with Jekyll and check that `_site/archive/index.html` and
`_site/companions/index.html` exist.
