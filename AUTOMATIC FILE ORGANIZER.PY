import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from openai import OpenAI
import shutil

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_API_KEY_HERE"
)
  
folder_path = ""

def get_ai_categories(files):
    prompt = f"""You will categorize a list of filenames.

Filenames (one per line):
{chr(10).join(files)}

For EACH filename above, output exactly one line in this format:
filename: Category

Category must be one of: Images, Videos, Documents, Music, Code, Others

Do not split filenames into letters. Treat each full filename as one single item.

Example:
resume.pdf: Documents
vacation.jpg: Images
"""
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[{"role": "user", "content": prompt}]
    )

    ai_text = response.choices[0].message.content
    file_categories = {}
    for line in ai_text.split("\n"):
        if ":" in line:
            filename, category = line.split(":", 1)
            file_categories[filename.strip()] = category.strip()

    return file_categories

def browse_folder():
    global folder_path
    folder_path =  filedialog.askdirectory()
    path_label.config(text=folder_path)
    print(folder_path)
    
def organize_files():
    counter = {
        "Images": 0, "Videos": 0, "Documents": 0,
        "Music": 0, "code": 0, "Others": 0
    }

    files = []
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isdir(full_path):
            continue
        files.append(file)

    file_categories = get_ai_categories(files)

    for filename, category in file_categories.items():
        source_path = os.path.join(folder_path, filename)
        destination_folder = os.path.join(folder_path, category)
        os.makedirs(destination_folder, exist_ok=True)
        destination_path = os.path.join(destination_folder, filename)

        if os.path.exists(destination_path):
            name, ext = os.path.splitext(filename)
            new_filename = name + "_1" + ext
            destination_path = os.path.join(destination_folder, new_filename)
            shutil.move(source_path, destination_path)
        else:
            shutil.move(source_path, destination_folder)

        counter[category] = counter.get(category, 0) + 1

    summary_text = ""
    for key, value in counter.items():
        summary_text = summary_text + f"{key}: {value} files moved\n"

    summary_label.config(text=summary_text)
    messagebox.showinfo("Done", "Files organized successfully!")
    
window = tk.Tk()
window.title("File Organizer")
window.geometry("1200x720")
window.configure(bg="#f0f8f6")

title_label = tk.Label(window, text="File Organizer", font=("Arial", 18, "bold"), bg="#f0f4f8", fg="#333333")
title_label.pack(pady=15)

browse_button = tk.Button(window, text="Browse", command=browse_folder, font=("Arial", 14), width=15, height=2,bg="#4CAF50", fg="white", relief="flat")
browse_button.pack(pady=10)

path_label = tk.Label(window, text = "no folder salected",  font=("Arial", 12),bg="#f0f4f8")
path_label.pack(pady=5)

organize_button = tk.Button(window, text="Organize", command=organize_files,  font=("Arial", 14), width=15, height=2,bg="#2196F3", fg="white", relief="flat")
organize_button.pack(pady=10)

summary_label = tk.Label(window, text="", justify="left", font=("Arial", 11), bg="#f0f4f8")
summary_label.pack()

footer_label = tk.Label(window, text="Made by Kazim", font=("Arial", 12, "bold"), bg="red", fg="white")
footer_label.pack(side="bottom", pady=10)

window.mainloop()    
