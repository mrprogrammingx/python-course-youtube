# Commands from Episode 3

Windows uses PowerShell. Mac uses Terminal. On Ubuntu, press Ctrl+Alt+T; on other Linux versions, search your apps for "Terminal".

## Open a terminal
| System | How |
|---|---|
| Windows | Search the Start menu for **PowerShell** |
| Mac | Press **Command + Space**, type **Terminal**, press Enter |
| Ubuntu | Press **Ctrl + Alt + T** (shortcuts vary on other Linux versions) |

## Check Python
| Job | Windows (PowerShell) | Mac / Linux |
|---|---|---|
| Check the version | `python --version` | `python3 --version` |
| Start Python | `python` | `python3` |
| Leave Python | `exit()` | `exit()` |

If `python --version` says "not found" on Windows, try `py --version`. See [troubleshooting.md](troubleshooting.md).

## Move around
| Job | Command (all systems) |
|---|---|
| Where am I? | `pwd` |
| What's here? | `ls` |
| Go into a folder | `cd Documents` |
| Go up one level | `cd ..` |
| Go to your home folder | `cd ~` |
| Make a folder | `mkdir python-course` |

## Two shortcuts
| Key | What it does |
|---|---|
| **Tab** | Finishes a folder name for you (works in most terminals) |
| **Up arrow** | Brings back your last command |

## Inside Python
```
>>> print("Hello")
Hello
>>> 2 + 2
4
>>> exit()
```
The `>>>` prompt means you are inside Python, not the terminal. Terminal commands such as `cd` do not work there:
```
>>> cd
NameError: name 'cd' is not defined
```

## Notes
- Use a dash, not a space, in folder names: `python-course`, not `python course`.
- In PowerShell, `ls` prints a table. That is fine.
- Windows uses backslashes in paths (`C:\Users\you`). Mac and Linux use forward slashes (`/Users/you`, `/home/you`).
