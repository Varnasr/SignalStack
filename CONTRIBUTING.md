# Contributing to SignalStack

Thanks for your interest in contributing to SignalStack! Whether you're fixing a broken link, suggesting a resource, or adding a new newsletter issue, your help is welcome.

## How to Contribute

1. **Fork** this repository
2. **Create a branch** from `main` with a descriptive name
3. **Make your changes** following the guidelines below
4. **Open a pull request** with a clear description of what you changed and why

## What You Can Contribute

- **Newsletter content** — New issue archives, extended notes, or source links
- **Featured resources** — Tools, methods, or frameworks relevant to development research
- **Book companion materials** — Notes, extras, or study resources
- **Bug fixes** — Broken links, typos, formatting issues
- **Translations** — Translated versions of existing content

## Commit Message Format

All commits must use a prefix from this list:

| Prefix | Use For |
|--------|---------|
| `Add:` | New feature, course, or tool |
| `Fix:` | Bug fix or broken link |
| `Update:` | Improvement to existing content or code |
| `Translate:` | Translation work |
| `Docs:` | Documentation changes |
| `Refactor:` | Code restructuring (no behaviour change) |
| `Test:` | Adding or updating tests |
| `CI:` | CI/CD pipeline changes |
| `Chore:` | Maintenance (deps, configs, tooling) |

**Example:** `Add: interactive Theory of Change lab`

Keep the subject line under 72 characters. These conventions are enforced by a commit-msg hook.

## Content Guidelines

- Write in clear, accessible English
- Use [Markdown](https://www.markdownguide.org/) for all content files
- Include source links for any claims, data, or references
- Use descriptive link text (avoid "click here")
- Keep file and folder names lowercase with hyphens (e.g., `my-new-resource.md`)

## Setting Up Locally

```bash
git clone https://github.com/Varnasr/SignalStack.git
cd SignalStack
npm install        # installs auto-changelog and sets up git hooks
```

The `npm install` step automatically configures git hooks via the `prepare` script, which enforces commit message format and blocks sensitive files from being committed.

## Large Files

Images (PNG, JPG, GIF) and PDFs are tracked with [Git LFS](https://git-lfs.com/). Before adding binary assets, install LFS:

```bash
git lfs install
```

This is a one-time setup. After that, Git handles LFS-tracked files transparently. Avoid committing images larger than 500 KB without LFS — the pre-commit hook will warn you.

## Pull Request Checklist

Before submitting your PR, please verify:

- [ ] Links are working and point to the correct destinations
- [ ] Markdown renders correctly (preview in your editor or on GitHub)
- [ ] Commit messages follow the prefix convention above
- [ ] No sensitive files (.env, credentials, keys) are included

## Reporting Issues

- **Broken links or content errors** — Open a [Content Issue](https://github.com/Varnasr/SignalStack/issues/new?template=content_issue.md)
- **Bugs** — Open a [Bug Report](https://github.com/Varnasr/SignalStack/issues/new?template=bug_report.md)
- **Ideas** — Open a [Feature Request](https://github.com/Varnasr/SignalStack/issues/new?template=feature_request.md)
- **Security vulnerabilities** — See [SECURITY.md](.github/SECURITY.md) (do NOT open a public issue)

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
