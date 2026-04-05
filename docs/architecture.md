# Architecture

How SignalStack is structured, what tools it uses, and why.

---

## Design Decisions

### Why a Git repository instead of a CMS?

- **Version history** — Every change is tracked and attributable
- **Open contributions** — Anyone can fork, improve, and submit a PR
- **No vendor lock-in** — Content is plain Markdown, readable anywhere
- **CI/CD integration** — Automated quality checks on every change
- **Part of a larger ecosystem** — Consistent tooling across all OpenStacks repos

### Why Markdown?

Markdown is the most portable, widely-supported format for structured text. It renders natively on GitHub, works with static site generators (Jekyll, Hugo, MkDocs), and can be converted to PDF, HTML, or EPUB.

---

## Directory Structure

```
SignalStack/
├── issues/                         # Content: newsletter archives
│   ├── april-2025/README.md        #   Each issue gets its own folder
│   └── june-2024/README.md
├── featured/                       # Content: tool and method reviews
│   └── *.md                        #   One file per featured resource
├── extras/                         # Content: companion materials
│   ├── books/                      #   Book-specific study aids
│   └── issue notes/                #   Extended newsletter references
├── docs/                           # Meta: project documentation
├── .github/                        # Infra: GitHub-specific config
│   ├── workflows/                  #   CI/CD pipelines
│   │   ├── lint-content.yml        #     Markdown lint + spell check + link check
│   │   └── update-changelog.yml    #     Auto-generate CHANGELOG on push to main
│   ├── ISSUE_TEMPLATE/             #   Bug, feature, and content issue forms
│   ├── pull_request_template.md    #   PR checklist
│   ├── SECURITY.md                 #   Vulnerability reporting policy
│   ├── CODEOWNERS                  #   Default reviewers
│   └── dependabot.yml              #   Automated dependency updates
├── .githooks/                      # Infra: local git hooks
│   ├── pre-commit                  #   Block sensitive files, warn on large files
│   └── commit-msg                  #   Enforce commit message prefix convention
├── assets/banner/                  # Media: images (Git LFS tracked)
├── CONTRIBUTING.md                 # Meta: contribution guidelines
├── CHANGELOG.md                    # Meta: auto-generated change log
├── CITATION.cff                    # Meta: machine-readable citation
├── LICENSE                         # Legal: MIT license
├── package.json                    # Infra: Node dependencies and scripts
├── .auto-changelog                 # Config: changelog generation settings
├── .markdownlint.json              # Config: markdown linting rules
├── .cspell.json                    # Config: spell checker dictionary
├── .editorconfig                   # Config: editor formatting standards
├── .gitattributes                  # Config: line endings + LFS tracking
└── .nvmrc                          # Config: Node.js version
```

---

## CI/CD Pipeline

### `lint-content.yml` — Runs on push and PR to `main`

Three parallel jobs:

| Job | Tool | What It Checks |
|-----|------|---------------|
| **Markdown Lint** | [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) | Consistent formatting, heading structure, list syntax |
| **Spell Check** | [cspell](https://cspell.org/) | Typos and misspellings (with a project-specific dictionary in `.cspell.json`) |
| **Link Check** | [lychee](https://github.com/lycheeverse/lychee) | Broken external and internal links |

### `update-changelog.yml` — Runs on push to `main`

Generates `CHANGELOG.md` from git commit history using [auto-changelog](https://github.com/CookPete/auto-changelog). Commit message prefixes (`Add:`, `Fix:`, `Update:`, etc.) are mapped to changelog categories via `.auto-changelog`.

---

## Git Hooks

Installed automatically via `npm install` (the `prepare` script sets `core.hooksPath` to `.githooks/`).

| Hook | What It Does |
|------|-------------|
| `pre-commit` | Blocks sensitive files (.env, .key, .pem, credentials), warns on console.log/debugger statements, checks for merge conflict markers, warns on files > 500 KB |
| `commit-msg` | Enforces commit message prefix convention (Add/Fix/Update/Docs/CI/Chore/etc.), warns on subject lines > 72 characters |

---

## Dependencies

Intentionally minimal — this is a content repo, not a software project.

| Package | Purpose |
|---------|---------|
| `auto-changelog` | Generates CHANGELOG.md from commit history |

That's it. No build step, no bundler, no framework.

---

## Branch Strategy

| Branch | Purpose | Protection |
|--------|---------|-----------|
| `main` | Production content — what readers see | Protected: require PR reviews, status checks must pass |
| `feature/*` | New content or improvements | Created from `main`, merged via PR |
| `fix/*` | Bug fixes and broken link repairs | Created from `main`, merged via PR |

All changes to `main` should go through a pull request with passing CI checks.
