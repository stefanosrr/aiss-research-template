* 00_setup.do: settings shared by every do-file.
* Start every do-file with:   do "code/00_setup.do"
* Run from the project root (run.py does this). Python counterpart: code/lib/paths.py

version 18                 // the lab's Stata version: results stay identical on newer releases
clear all
set more off
set varabbrev off          // no silent abbreviation of variable names
set seed 20261020          // set once per project, then never change it; same as SEED in code/lib/settings.py

* Project root and folders
global ROOT "`c(pwd)'"
local data : env DATA_DIR
if `"`data'"' == "" local data "$ROOT/data"
global DATA     "`data'"
global RAW      "$DATA/raw"
global LLM      "$DATA/llm_cache"
global INTERIM  "$DATA/interim"
global CLEAN    "$DATA/clean"
global TABLES   "$ROOT/output/tables"
global FIGURES  "$ROOT/output/figures"
global LOGS     "$ROOT/output/logs"

* Project-local packages: ssc install / net install now write to code/ado,
* which is committed, so everyone runs the same version of reghdfe, estout, ...
sysdir set PLUS     "$ROOT/code/ado/plus"
sysdir set PERSONAL "$ROOT/code/ado/personal"
