"""Every path in the project comes from here, so no script contains a path to someone's laptop.

    from lib.paths import RAW, CLEAN, TABLES
    df = pd.read_csv(RAW / "census_1900_2026-10-20.csv")
"""
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _read_env(path):
    """Read KEY=value lines from .env (no extra package needed)."""
    values = {}
    if path.exists():
        for line in path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                value = re.split(r"\s#", value, maxsplit=1)[0]  # drop a comment after the value
                values[key.strip()] = value.strip().strip('"').strip("'")
    return values


# Settings already in the shell win over .env.
for _key, _value in _read_env(ROOT / ".env").items():
    os.environ.setdefault(_key, _value)

DATA = Path(os.environ.get("DATA_DIR") or "data").expanduser()
if not DATA.is_absolute():
    DATA = ROOT / DATA

RAW = DATA / "raw"
LLM_CACHE = DATA / "llm_cache"
INTERIM = DATA / "interim"
CLEAN = DATA / "clean"

OUTPUT = ROOT / "output"
TABLES = OUTPUT / "tables"
FIGURES = OUTPUT / "figures"
LOGS = OUTPUT / "logs"


def ensure_dirs():
    """Create the data and output folders if they do not exist yet."""
    for folder in (RAW, LLM_CACHE, INTERIM, CLEAN, TABLES, FIGURES, LOGS):
        folder.mkdir(parents=True, exist_ok=True)
