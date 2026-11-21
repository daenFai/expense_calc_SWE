# AGENTS.md — Expense Calculator

## Purpose
Small educational CLI that records expenses (name, amount, category) and computes
totals, totals with tax, totals with discount, per-category totals and CSV export.

## Architecture
- `expense_calc/calculator.py` — pure business logic (no input/output except CSV export).
- `expense_calc/cli.py` — interactive command loop; must only parse input and print output.
- `tests/test_calculator.py` — unit tests (stdlib `unittest`).
- No third-party dependencies. Python 3.12 was used for verification.

## Setup and safe commands (allowed without asking)
- Run tests:  `python3 -m unittest discover -s tests -v`
- Syntax check: `python3 -m compileall -q expense_calc tests`
- Run app: `python3 -m expense_calc.cli`
- Read-only git: `git status`, `git diff`, `git log`
- Optional, only if installed: `ruff check .`, `mypy expense_calc`

## Coding conventions
- Keep business logic in `calculator.py`; do not add logic to `cli.py`.
- Public functions need a short docstring; prefer type hints on new code.
- Keep changes small: one concern per commit, with a clear message.
- Categories are lowercase strings; tax/discount rates live in data tables, not in `if/elif` chains.

## Test expectations
- Every behavior change needs a test in `tests/`. All tests must pass before commit.
- These acceptance criteria must stay true:
  1. total = sum of amounts; 2. tax multipliers food 1.05 / transport 1.10 /
  entertainment 1.20 / other 1.00; 3. discount multipliers 0.95 / 0.90 / 0.80 / 1.00;
  4. per-category totals group correctly; 5. CSV export writes header + one row per expense.

## Forbidden actions
- Never read, create, print or commit secrets, tokens, `.env` files or real personal data.
- No production deployment, publishing or release tagging.
- No destructive commands: `rm -rf`, `git reset --hard`, `git push --force`, `git clean -fd`, history rewrites.
- No adding, upgrading or removing dependencies without human review.
- No network access or installing packages unless a human approves.
- Do not edit files outside this repository.

## Review gates
- A human reviews every diff before it is committed or merged.
- The agent must report: changed files, test command and its real output, and anything not run.
- Never claim a check passed unless it was actually executed.
