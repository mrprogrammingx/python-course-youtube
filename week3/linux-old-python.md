# Linux: your Python is older than 3.12

This course needs Python 3.12 or newer. Check yours:
```
python3 --version
```
If it prints 3.12 or newer, you are ready. Skip this file.

**Do not remove or replace the system Python.** Your system uses it. Install a second Python next to it.

> **TO VERIFY BEFORE PUBLISHING:** the steps below are a proposed route and have NOT been tested for this course. Test them on Ubuntu 22.04 (which ships Python 3.10) and confirm the output. Replace this note when done, or choose a different route.

## Option: uv (installs Python without touching the system Python)

1. Install uv (see the official instructions at https://docs.astral.sh/uv/getting-started/installation/):
   ```
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   Then open a new terminal.
2. Install a newer Python:
   ```
   uv python install 3.13
   ```
3. Check it:
   ```
   uv run --python 3.13 python --version
   ```

The system `python3` stays exactly as it was. To run your own scripts with the new Python, use `uv run --python 3.13 python yourfile.py`.

## Questions
Paste your `python3 --version` output, your Linux version and any error in the video comments.
