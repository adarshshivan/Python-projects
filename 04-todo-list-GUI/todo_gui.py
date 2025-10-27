import tkinter as tk
from tkinter import messagebox

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        task = tasks.pop(selected_index)
        update_listbox()
        messagebox.showinfo("Deleted", f"Task '{task}' deleted successfully.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        update_listbox()

# ------------------ UI ------------------
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x450")
root.config(bg="#f0f0f0")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=25, font=("Arial", 14))
entry.grid(row=0, column=0, padx=10)

add_button = tk.Button(frame, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1)

listbox = tk.Listbox(root, width=40, height=15, selectmode=tk.SINGLE, font=("Arial", 12))
listbox.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

delete_button = tk.Button(button_frame, text="Delete Task", width=12, command=delete_task)
delete_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", width=12, command=clear_tasks)
clear_button.grid(row=0, column=1, padx=5)

root.mainloop()
