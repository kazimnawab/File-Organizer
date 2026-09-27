import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

from ai_categorizer import get_ai_categories
from theme import light_theme, dark_theme
from file_operations import confirm_and_organize, undo_last_organize

current_theme = light_theme
folder_path = ""

def apply_theme(theme):
    window.configure(bg=theme["bg"])
    title_label.configure(bg=theme["label_bg"], fg=theme["fg"])
    path_label.configure(bg=theme["label_bg"], fg=theme["fg"])
    summary_label.configure(bg=theme["label_bg"], fg=theme["fg"])

def browse_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    path_label.config(text=folder_path)
    print(folder_path)

def show_preview(file_categories):
    preview_window = tk.Toplevel(window)
    preview_window.title("Preview - Confirm Organization")
    preview_window.geometry("500x600")

    check_vars = {}

    confirm_button = tk.Button(preview_window, text="Confirm & Organize",
        command=lambda: confirm_and_organize(file_categories, check_vars, preview_window, folder_path, summary_label),
        bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=25, height=2)
    confirm_button.pack(side="bottom", pady=15)

    canvas = tk.Canvas(preview_window)
    scrollbar = tk.Scrollbar(preview_window, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas)

    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    def toggle_all():
        for var in check_vars.values():
            var.set(select_all_var.get())

    select_all_var = tk.BooleanVar(value=True)
    select_all_check = tk.Checkbutton(scroll_frame, text="Select All", variable=select_all_var, command=toggle_all)
    select_all_check.pack(anchor="w", pady=5)

    for filename, category_path in file_categories.items():
        var = tk.BooleanVar(value=True)
        check_vars[filename] = var
        chk = tk.Checkbutton(scroll_frame, text=f"{filename} → {category_path}", variable=var)
        chk.pack(anchor="w")

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def organize_files():
    files = []
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isdir(full_path):
            continue
        files.append(file)

    progress_bar.pack(pady=10)
    progress_bar.start()
    window.update()

    file_categories = get_ai_categories(files)

    progress_bar.stop()
    progress_bar.pack_forget()

    show_preview(file_categories)

def toggle_theme():
    global current_theme
    if current_theme == light_theme:
        current_theme = dark_theme
    else:
        current_theme = light_theme
    apply_theme(current_theme)

window = tk.Tk()
window.title("File Organizer")
window.geometry("1200x720")
window.configure(bg="#f0f8f6")

title_label = tk.Label(window, text="File Organizer", font=("Arial", 18, "bold"), bg="#f0f4f8", fg="#333333")
title_label.pack(pady=15)

browse_button = tk.Button(window, text="Browse", command=browse_folder, font=("Arial", 14), width=15, height=2, bg="#4CAF50", fg="white", relief="flat")
browse_button.pack(pady=10)

path_label = tk.Label(window, text="no folder salected", font=("Arial", 12), bg="#f0f4f8")
path_label.pack(pady=5)

organize_button = tk.Button(window, text="Organize", command=organize_files, font=("Arial", 14), width=15, height=2, bg="#2196F3", fg="white", relief="flat")
organize_button.pack(pady=10)

summary_label = tk.Label(window, text="", justify="left", font=("Arial", 11), bg="#f0f4f8")
summary_label.pack()

footer_label = tk.Label(window, text="Made by Kazim", font=("Arial", 12, "bold"), bg="red", fg="white")
footer_label.pack(side="bottom", pady=10)

progress_bar = ttk.Progressbar(window, mode="indeterminate", length=300)

undo_button = tk.Button(window, text="Undo", command=lambda: undo_last_organize(summary_label), font=("Arial", 14), width=15, height=2, bg="#f44336", fg="white", relief="flat")
undo_button.pack(pady=10)

theme_button = tk.Button(window, text="Toggle Dark Mode", command=toggle_theme, font=("Arial", 10))
theme_button.pack(pady=5)

window.mainloop()