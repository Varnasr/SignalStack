# Getting started

## Read

Open [companions/](../companions/) for the compiled sections or
[archive/](../archive/) for editions as sent. On the web:
[varnasr.github.io/SignalStack](https://varnasr.github.io/SignalStack/).

## Run the tools

Python 3.10 or later.

```bash
git clone https://github.com/Varnasr/SignalStack.git
cd SignalStack
python tools/poverty_lines.py --year 2024
```

## Run the tests

```bash
pip install pytest
python -m pytest tests/
python scripts/build_companions.py --check
```

## Update the archive

```bash
python scripts/sync_substack.py --check     # exit 1 if Substack has new posts
python scripts/sync_substack.py
python scripts/build_companions.py
```

No key is needed; the Substack API is public.

## Build the site locally

```bash
gem install bundler jekyll jekyll-readme-index
jekyll serve
```

Check links against the Jekyll build, not `python -m http.server`, which
serves directory listings and so passes folder links that fail in
production.
