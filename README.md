# [Project title]

> **Starting from the AISS template?** Follow these eight steps, then delete this box.
> The [step-by-step guide](https://aiss-unibocconi-eu.github.io/aiss-research-template/#start) explains each one.
>
> 1. **Create your project.** Click **Use this template** → **Create a new repository**, give it a short lowercase name (e.g. `census-migration`) and make it **Private**.
> 2. **Clone it.** In a terminal, run `git clone https://github.com/<owner>/<your-project>.git`, then `cd <your-project>`.
> 3. **Add your local settings.** Run `cp .env.example .env`, then fill in `DATA_DIR`, `STATA_PATH` and any API keys. `.env` never leaves your computer.
> 4. **Install and run.** Run `uv sync`, then `uv run python run.py` ([install uv](https://docs.astral.sh/uv/getting-started/installation/) first if needed). It ends with `setup looks good`, or tells you what is missing.
> 5. **Describe the project** in this README: title, research question, team.
> 6. **Add your project specifics** at the end of `AGENTS.md`, and any extra entries to `.gitignore`.
> 7. **Start the codebook** in `data/codebook.md` with your main variables.
> 8. **Commit and push.** Run `git add -A`, then `git commit -m "Describe the project"`, then `git push`.

## Question

[Two sentences: what this project wants to learn, and why it matters.]

## How to run

```bash
uv sync                    # same Python packages, same versions, on any machine
uv run python run.py       # every script, in order: raw data in, tables and figures out
```

`run.py` lists every script in the order it runs, Python and Stata alike. Stata scripts need `STATA_PATH` in `.env`.
To run part of the pipeline, add part of a script's path: `uv run python run.py build` runs every build step, and `uv run python run.py 01_import` runs just that script. Always start Python scripts this way: started directly, they stop with `No module named 'lib'`.

## Data

Data never goes into Git. It lives on lab storage, and each machine sets its location as `DATA_DIR` in `.env`.
Every source is documented in [`data/README.md`](data/README.md): origin, date, who downloaded it, licence.
Every variable in the clean data is defined in [`data/codebook.md`](data/codebook.md).

## Structure

```
README.md        what the project is and how to run it
AGENTS.md        standing instructions for AI coding agents (CLAUDE.md points to it)
run.py           the single entry point
pyproject.toml   Python packages requested    ─┐ changed only
uv.lock          exact versions installed      ─┘ through uv
.env.example     secrets and machine paths the project needs, without values

data/            ignored by Git, except the two files below
  README.md      where every dataset came from
  codebook.md    every variable in data/clean: label, unit, definition
  raw/           as received: never edited, never overwritten
  llm_cache/     prompts and raw model responses: written once, never deleted
  interim/       working files, rebuildable
  clean/         analysis-ready, rebuildable; the only data analysis reads

code/
  00_setup.do    Stata settings; every do-file runs it first
  01_build/      raw → clean (no estimation)
  02_analysis/   clean → output (reads only data/clean)
  lib/           shared Python functions, including paths.py and settings.py (the seed)
  ado/           project-local Stata packages, committed

output/          written by code only, never by hand
  tables/        tracked: a changed number shows up in the pull request
  figures/       tracked
  logs/          ignored

docs/
  log/           research log, one file per person, newest entry on top
  updates/       weekly update to the PI, one file per week

paper/           draft and slides; tables and figures come from output/
scratch/         your sandbox, ignored; nothing may depend on it
```

## Team

| Role | Name |
|:--|:--|
| PI | [name] |
| RA | [name] |

---
<sub>Built from the [AISS research template](https://github.com/aiss-unibocconi-eu/aiss-research-template) · AI in Social Sciences Lab, Bocconi University</sub>
