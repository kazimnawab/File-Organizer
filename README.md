# File Organizer (AI-Powered)

A Python desktop app that automatically organizes messy folders — but instead of just sorting by file extension, it uses AI to understand what each file actually is based on its filename, and sorts it into meaningful categories and subcategories.

## What it does

1. You pick a folder using the Browse button
2. The app collects all filenames in that folder
3. It sends those filenames to an AI model (via OpenRouter API)
4. The AI reads each filename and decides a Main Category and Subcategory for it (e.g. `Documents/Work`, `Images/Personal`) — based on what the name suggests, not just the extension
5. A preview window shows every file with its suggested category, with checkboxes so you can pick exactly which files to move (or use "Select All")
6. Once confirmed, files are moved into folders matching the AI's suggestions
7. A summary shows how many files were moved into each category
8. If you change your mind, the Undo button restores everything to its original location

## Features

- AI-based categorization using filename context (not just file type)
- Nested categories (Main Category/Subcategory), auto-creates folders as needed
- Preview screen with checkboxes before anything is moved — nothing happens without confirmation
- "Select All" toggle for quick selection
- Duplicate filename handling (renames instead of overwriting)
- Undo — moves everything back to where it came from
- Progress bar while waiting on the AI response
- Light/Dark mode toggle
- Packaged as a standalone `.exe` — runs without installing Python

## Project structure

The code is split into separate files, each handling one part of the app:

- `main.py` — the GUI itself: window, buttons, labels, and the app's overall flow (Browse → Organize → Preview → Confirm)
- `ai_categorizer.py` — builds the prompt, calls the AI model via OpenRouter's API, and parses the response into a filename → category dictionary
- `file_operations.py` — handles the actual moving of files, duplicate renaming, and the undo logic (keeps a history of every move)
- `theme.py` — holds the light and dark color themes used by the UI

`main.py` imports and uses the other three files — it's the file you actually run.

## How to use it

**Option A — Run from source**
1. Install the required library:
pip install openai
2. Add your own OpenRouter API key in `ai_categorizer.py`
3. Run:


**Option B — Use the packaged app**
1. Download `main.exe` from the `dist` folder
2. Double-click to run — no Python installation needed
3. Click Browse, pick a folder, click Organize
4. Review the AI's suggestions in the preview window, uncheck anything you don't want moved
5. Click Confirm & Organize

## Tools and libraries used

- `os` — reading folders, building paths, creating directories
- `shutil` — moving files
- `tkinter` — the GUI (window, buttons, labels, checkboxes, scrollable preview, dark mode)
- `openai` Python library — used to call OpenRouter's API (which routes to various AI models, including free ones)
- PyInstaller — packaging the app into a standalone `.exe`

## Why I made this

I started this as a simple script to practice Python fundamentals — loops, file handling, conditionals. Over time I kept upgrading it: added a GUI, packaged it as a real app, then integrated an AI model to make the categorization smarter (based on filename meaning instead of just extension). Along the way I also learned to split a single large file into a proper multi-file project structure, use Git/GitHub properly (including fixing mistakes like committing large files or exposed API keys), and think about UX decisions like previewing AI suggestions before taking action instead of just trusting AI blindly.

## Bugs I ran into and fixed

- Script moving its own created folders into "Others" — fixed by skipping directories in the loop
- Files with the same name getting overwritten — fixed with duplicate detection and renaming
- Windows path errors from backslashes — fixed using raw strings
- Indentation mistakes causing only one file to move, or files always landing in "Others" — fixed by carefully aligning code blocks
- AI initially splitting filenames into individual letters — fixed by rewriting the prompt to be more explicit, with an example
- Accidentally committed a large test video file and exposed API keys to GitHub — fixed by resetting git history and moving the key out of the tracked source file

## Notes on the API key

The AI categorization feature requires an OpenRouter API key. The version of the code here uses a placeholder (`YOUR_API_KEY_HERE`) — you'll need to get your own free key from openrouter.ai to run the AI features yourself.

## Next steps / ideas

- Let users save/load their own API key through the app instead of hardcoding it
- Add a log file recording every organize session
- Add more nuanced category rules or let users customize categories

## License

This project is open for anyone to use, copy, or modify. Feel free to learn from it or build on top of it.
