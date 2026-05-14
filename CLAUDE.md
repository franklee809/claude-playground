# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository

A beginner tutorial playground repository, part of a FreeCodeCamp guide to Claude Code.

Remote: `git@github.com:franklee809/claude-playground.git`

Branches:
- `master` — clean base project
- `freecodecamp` — tutorial work (this branch)

## Commands

```bash
# Run the main entry point
python3 main.py

# Run the CSV reader tutorial script
python3 read_members.py

# Install dependencies (uses uv)
uv sync
```

## Architecture

This is a minimal Python project managed with `uv` (pyproject.toml). There are no external dependencies.

- `main.py` — project entry point (hello world stub)
- `read_members.py` — tutorial script: reads `members.csv` and prints first/last name of each member
- `members.csv` — sample data with `first_name` and `last_name` columns
