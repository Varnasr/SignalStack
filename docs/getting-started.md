# Getting Started

## For Readers

No setup needed. Browse the repository directly on GitHub:

- **[Newsletter Issues](../issues/)** — Start here for curated research summaries
- **[Featured Tools](../featured/)** — Highlighted tools and methods for practitioners
- **[Book Companions](../extras/books/)** — Study aids with definitions, applications, and walkthroughs
- **[Extended Notes](../extras/issue%20notes/)** — Deep-dive source links for newsletter topics

Each newsletter issue page includes summaries and key takeaways so you can get value without leaving the repo.

---

## For Contributors

### Prerequisites

- [Git](https://git-scm.com/) (any recent version)
- [Node.js](https://nodejs.org/) 20 or later (for git hooks and changelog generation)
- A text editor with Markdown support (VS Code, Obsidian, or similar)

### Setup

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/SignalStack.git
cd SignalStack

# 2. Install dependencies (sets up git hooks automatically)
npm install

# 3. Create a branch
git checkout -b add/your-contribution-name
```

The `npm install` step runs the `prepare` script, which configures git to use the project's commit hooks. These hooks enforce:

- **Commit message format** — Messages must start with a prefix like `Add:`, `Fix:`, `Update:`, etc.
- **Sensitive file blocking** — Prevents accidental commits of `.env`, credentials, or key files
- **Large file warnings** — Flags files over 500 KB

### Verifying Your Setup

```bash
# This should show the hooks path is set to .githooks
git config core.hooksPath
# Expected output: .githooks

# Try a test commit (this should fail with a format error)
git commit --allow-empty -m "test"
# Expected: "Invalid commit message format" error
```

### What to Work On

See the [Roadmap](roadmap.md) for planned work, or browse [open issues](https://github.com/Varnasr/SignalStack/issues) for things that need help.

---

## Project Layout

```
SignalStack/
├── issues/          # One folder per newsletter issue
├── featured/        # One file per featured tool or resource
├── extras/          # Book companions and extended notes
├── docs/            # This documentation (you are here)
├── .github/         # CI workflows, issue templates, security policy
├── .githooks/       # Pre-commit and commit-msg hooks
└── assets/          # Images and visual assets (Git LFS tracked)
```

See [Architecture](architecture.md) for a detailed breakdown of each directory and the reasoning behind the structure.
