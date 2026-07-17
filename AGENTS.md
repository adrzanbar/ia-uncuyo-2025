# AGENTS.md

Work happens only in `/tp5`. tp1–tp4 are finished course assignments; ignore them.

## /tp5/aima-python is the AIMA library

- It is the [`aimacode/aima-python`](https://github.com/aimacode/aima-python) library (Russell & Norvig, *AI: A Modern Approach* 4th ed), version `4.0.0`, Python `>=3.9`.
- The importable package is `aima` (`import aima.search`, `aima.agents`, …).
- `lite/` is a JupyterLite/Pyodide companion build (separate toolchain, `build.sh`). It is NOT used for normal Python runs.

## Git: tp5 is a nested repo, treated as untracked by the parent

- `tp5/aima-python` is its own git clone of `aimacode/aima-python` — **not** a submodule of the parent `ia-uncuyo-2025` repo. The parent repo sees `tp5/` only as untracked content.
- Git operations inside `tp5/aima-python` are isolated from the parent repo. Don't expect the parent `git` to track or commit changes made there.
- It contains ONE real submodule: `aima-data` (dataset files). Update it only via the procedure in `tp5/aima-python/SUBMODULE.md` (deinit → rm → re-add), never by hand.

## Dependencies are heavy — don't install everything blindly

- `requirements.txt` pulls in tensorflow, keras, opencv, cvxopt, etc. Most `aima` modules only need `numpy`, `matplotlib`, `networkx`, `pandas`, `scipy`, `sortedcontainers`.
- Only `pip install -r requirements.txt` if you actually touch deep-learning / vision / optimization code. Otherwise install the small subset a given module needs.

## Tests and lint

- Run all tests from `tp5/aima-python/`: `pytest`
- Single test file: `pytest tests/test_search.py`
- `pytest.ini` suppresses Deprecation/User/Runtime warnings — do not "fix" code just to silence them.
- Lint: `flake8` (config `.flake8`): `max-line-length = 100`, many E/W rules ignored, `tests/` excluded. Match existing style rather than reformatting.

## Pre-commit / CI

- No CI workflows, pre-commit, or task runner in this repo. Verify changes by running the relevant `pytest` file directly.
