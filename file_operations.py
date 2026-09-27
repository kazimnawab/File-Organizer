import os
import shutil
from tkinter import messagebox

move_history = []

def confirm_and_organize(file_categories, check_vars, preview_window, folder_path, summary_label):
    move_history.clear()
    counter = {}

    for filename, category_path in file_categories.items():
        if not check_vars[filename].get():
            continue

        source_path = os.path.join(folder_path, filename)
        destination_folder = os.path.join(folder_path, category_path)
        os.makedirs(destination_folder, exist_ok=True)
        destination_path = os.path.join(destination_folder, filename)

        if os.path.exists(destination_path):
            name, ext = os.path.splitext(filename)
            new_filename = name + "_1" + ext
            destination_path = os.path.join(destination_folder, new_filename)
            shutil.move(source_path, destination_path)
            move_history.append((destination_path, source_path))
        else:
            shutil.move(source_path, destination_folder)
            move_history.append((os.path.join(destination_folder, filename), source_path))

        counter[category_path] = counter.get(category_path, 0) + 1

    summary_text = ""
    for key, value in counter.items():
        summary_text = summary_text + f"{key}: {value} files moved\n"

    summary_label.config(text=summary_text)
    preview_window.destroy()
    messagebox.showinfo("Done", "Files organized successfully!")


def undo_last_organize(summary_label):
    if not move_history:
        messagebox.showinfo("Undo", "Nothing to undo.")
        return

    for current_location, original_location in move_history:
        if os.path.exists(current_location):
            shutil.move(current_location, original_location)

    move_history.clear()
    summary_label.config(text="Undo complete — files restored.")
    messagebox.showinfo("Undo", "Files moved back to original location!")