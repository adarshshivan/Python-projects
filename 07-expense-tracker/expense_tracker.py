import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

# ------------------- CSV File Setup -------------------
CSV_FILE = "expenses.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Amount", "Category"])  # header

# ------------------- Functions -------------------
def add_expense():
    title = title_entry.get().strip()
    amount = amount_entry.get().strip()
    category = category_entry.get().strip()

    if not title or not amount or not category:
        messagebox.showwarning("Warning", "All fields are required!")
        return

    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    # Save to CSV
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([title, amount, category])

    # Clear input fields
    title_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Expense added successfully!")
    load_expenses()

def load_expenses():
    for row in expense_tree.get_children():
        expense_tree.delete(row)

    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            expense_tree.insert("", tk.END, values=row)

# ------------------- UI Setup -------------------
root = tk.Tk()
root.title("💰 Expense Tracker")
root.geometry("600x400")
root.config(bg="#f8f9fa")

# Title
tk.Label(root, text="Expense Tracker", font=("Arial", 18, "bold"), bg="#f8f9fa").pack(pady=10)

# Input frame
frame = tk.Frame(root, bg="#f8f9fa")
frame.pack(pady=10)

tk.Label(frame, text="Title:", font=("Arial", 12), bg="#f8f9fa").grid(row=0, column=0, padx=5, pady=5)
title_entry = tk.Entry(frame, width=20, font=("Arial", 12))
title_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Amount:", font=("Arial", 12), bg="#f8f9fa").grid(row=0, column=2, padx=5, pady=5)
amount_entry = tk.Entry(frame, width=15, font=("Arial", 12))
amount_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame, text="Category:", font=("Arial", 12), bg="#f8f9fa").grid(row=1, column=0, padx=5, pady=5)
category_entry = tk.Entry(frame, width=20, font=("Arial", 12))
category_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame, text="Add Expense", font=("Arial", 12), bg="#007bff", fg="white", command=add_expense).grid(row=1, column=3, padx=5, pady=5)

# Expense list
columns = ("Title", "Amount", "Category")
expense_tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    expense_tree.heading(col, text=col)
    expense_tree.column(col, width=180, anchor="center")
expense_tree.pack(pady=10)

# Load existing data
load_expenses()

root.mainloop()
