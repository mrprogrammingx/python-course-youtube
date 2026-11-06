# Troubleshooting: Python "not found"

Start here if `python --version` or `python3 --version` does not print a version.

## 1. You typed the wrong word
- **Windows:** use `python --version`.
- **Mac and Linux:** use `python3 --version`. On many of these systems, plain `python` does not exist or points somewhere else.

## 2. Your terminal window is old
A terminal that was open **before** you installed Python may not see it. Close it and open a new one, then try again.

## 3. Windows opens the Microsoft Store instead of Python
Try the launcher:
```
py --version
```
If that prints a version, Python is installed. You can use `py` in place of `python` for now.

The Windows install manager also has a setup checker:
```
py install --configure
```
Windows only. It checks your setup and can fix some problems.
<!-- TO VERIFY before publishing: confirm what `py install --configure` does on your recording machine. -->

## 4. Linux: command missing
On Ubuntu:
```
sudo apt install python3
```
`sudo` runs one command with extra permission and may ask for your password. Then check again with `python3 --version`.

## 5. Linux: version older than 3.12
See [linux-old-python.md](linux-old-python.md).

## Never remove the system Python on Linux
Your system uses its own Python. Do not remove it or replace it. Install a newer one next to it instead.

## Still stuck?
Paste the exact error, and your operating system, in the video comments.
