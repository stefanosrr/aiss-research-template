# Data sources

Every dataset the project uses has an entry here **before** any code reads it. Together with `codebook.md`, it is one of the two files in `data/` that Git tracks.

Rules for `raw/`: files stay exactly as received. Never edit them, never re-save them from Excel, never overwrite them. A new download gets a new file with the date in its name, e.g. `census_1900_2026-10-20.csv`.

Mark a source **yes** under *Personal or restricted?* if it contains information about identifiable people or comes with access restrictions. Before such data is sent to an external API (an LLM call, or an AI agent reading it), the researcher is told and decides.

| File in `raw/` | Source and link | Downloaded (date, by) | Licence and access | Personal or restricted? | Notes |
|:--|:--|:--|:--|:--|:--|
| [census_1900_2026-10-20.csv] | [IPUMS USA, 1900 full count] | [2026-10-20, name] | [IPUMS terms; no redistribution] | [no] | [extract settings, variables] |

## LLM outputs (`llm_cache/`)

Prompts and raw model responses, saved by code the first time a call is made and never deleted. A retired model cannot be queried again, so these files are the only record of what it answered.

| Folder in `llm_cache/` | Model and version | Dates | Settings (temperature, seed) | Produced by |
|:--|:--|:--|:--|:--|
| [classify_speeches/] | [model-name-2026-05-01] | [2026-10-20 to 2026-10-22] | [temperature 0, seed 42] | [code/01_build/03_classify.py] |
