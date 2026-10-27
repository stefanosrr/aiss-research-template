# Instructions for AI coding agents

This is a research project built on the AISS lab template. Follow these rules exactly as a new research assistant would.

## Data

- `data/raw/` is read-only: never edit, overwrite, move or delete anything in it. `data/llm_cache/` is append-only: code adds new files but never changes or deletes existing ones.
- Data moves one way: raw → interim → clean. Scripts in `code/01_build/` read raw data and write to `data/interim/` and `data/clean/`. Scripts in `code/02_analysis/` read only `data/clean/` and write only to `output/`.
- A new data source gets an entry in `data/README.md` before any code uses it.
- Variables in `data/clean/` are defined in `data/codebook.md`. Read it before creating, renaming or interpreting a variable, and update its row in the same commit.

## Paths and environment

- Never hard-code a path. Python scripts use `from lib.paths import RAW, CLEAN, TABLES, ...`. Every do-file starts with `do "code/00_setup.do"` and uses the globals it defines (`$RAW`, `$CLEAN`, `$TABLES`, ...).
- Add Python packages only with `uv add <package>`, and ask before adding one. Never `pip install`, never edit `uv.lock` or the dependency list in `pyproject.toml` by hand.
- Stata packages install into `code/ado/` (`00_setup.do` points `PLUS` there). Ask before installing one.
- Secrets live in `.env`, which is never committed. Read keys from environment variables; never write a key into code, a notebook or a log.

## The pipeline

- `run.py` is the single entry point. Every new script goes into its `STEPS` list, in run order. A script not listed there is not part of the project.
- Tables and figures are written by code into `output/tables/` and `output/figures/`. Never type a number into `paper/` by hand.
- Randomness always uses the project seed: `SEED` from `lib.settings` in Python, the `set seed` in `00_setup.do` in Stata. Never set a different one.
- Quick experiments go in `scratch/`. Nothing outside `scratch/` may import from it or read from it.

## LLM calls

- Save every prompt and the raw response to `data/llm_cache/` before processing it. Before calling a model, check the cache; never re-query for an answer that is already saved.
- Record the exact model name and version, the date, temperature and seed for every call, so a result can be traced to the call that produced it.
- Before running code that makes new API calls, tell the researcher how many calls, the rough cost, and whether the data is marked personal or restricted in `data/README.md`, and wait for their go-ahead.

## Working with Git

- Work on a branch named `type/task`, where type is `data`, `analysis`, `paper` or `fix` (e.g. `data/merge-counties`); never directly on `main`. Commit small, working steps with a message saying what changed and why.
- Never push, open a pull request or merge without asking.
- Run `uv run python run.py` before saying a task is done; `uv run python run.py <name>` runs only the steps whose path contains `<name>`.

## When to stop and ask

Ask the researcher before deciding anything that changes results: sample restrictions, variable definitions, specifications, dropping observations, or handling of missing data. State the options; don't choose silently.

## Project specifics

<!-- The PI fills this in: the research question in one sentence, the main datasets, naming conventions, anything an RA would need to know. -->
