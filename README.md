# File Organizer

This is a simple Python project I made to organize messy folders automatically. It started as a command-line script and later I added a GUI version using tkinter.

## What it does

It looks at all the files in a folder and moves them into subfolders based on their type:
- Images (.jpg, .png, .jpeg)
- Videos (.mp4, .mkv)
- Documents (.pdf, .docx)
- Music (.mp3, .wav)
- Code (.py, .txt, .zip, .exe)
- Others (anything that doesn't match)

If two files have the same name, it won't overwrite one — it renames the new one automatically so nothing gets lost.

At the end it shows a summary of how many files went into each folder.

## Two versions in this repo

**1. Command-line version** (`AUTOMATIC FILE ORGANIZER.PY`)
- You type the folder path manually
- Summary shows in the terminal

**2. GUI version** (`gui_organizer.py`)
- A window with buttons instead of typing commands
- "Browse" button opens a folder picker
- Shows the selected folder path on screen
- "Organize" button runs the sorting
- Summary shows inside the window
- A popup confirms when it's done

## How to use it

**Command-line version:**
1. Run the script
2. Type the folder path you want to organize
3. Check the folder — it'll be sorted into subfolders

**GUI version:**
- A window with buttons instead of typing commands
- "Browse" button opens a folder picker
- Shows the selected folder path on screen
- "Organize" button runs the sorting
- Summary shows inside the window
- A popup confirms when it's done
- Styled interface: custom colors, bigger buttons, background image, and a footer credit
- Packaged as a standalone .exe using PyInstaller (no need to install Python to run it)

## What I used

- `os` for reading folders and creating new ones
- `shutil` for moving the files
- `tkinter` for building the GUI (buttons, labels, folder picker, popup)

## Why I made this

I'm learning Python and wanted to build something real instead of just doing exercises. This helped me actually understand loops, if/else, dictionaries, functions, and how to work with files — not just read about them. Adding the GUI later also taught me how tkinter works and how buttons connect to functions.

## Bugs I ran into (and fixed)

- The script kept moving its own created folders into "Others" — had to add a check to skip folders
- Files with the same name were getting overwritten — added a check for that
- Windows paths kept crashing because of backslashes — fixed with raw strings
- In the GUI version, indentation mistakes caused only one file to move, or files to only go into "Others" — fixed by carefully aligning the code inside the loop and if/else blocks

## UI Styling

The GUI version has a custom look:
- Background image
- Colored buttons (green for Browse, blue for Organize)
- Bigger fonts for readability
- A footer showing who made it

## AI-Powered Categorization (New)

The GUI version now uses AI instead of just file extensions to decide categories:
- Collects filenames from the selected folder
- Sends them to an AI model (via OpenRouter API, using a free model)
- AI reads each filename and decides what it's actually about (not just its extension)
- Files get moved into folders based on what the AI decided

This means a file like `vacation_video.mp4` gets sorted by understanding the *name*, not just checking `.mp4` — more context-aware than the original rule-based version.

### Tools added
- `openai` Python library (used to talk to OpenRouter's API)
- OpenRouter — lets you call various free AI models through one API

## Turning it into an app

I used PyInstaller to package the GUI version into a standalone `.exe` file, so it can run on any Windows PC without needing Python installed:
```
py -m PyInstaller --onefile --windowed gui_organizer.py
```

