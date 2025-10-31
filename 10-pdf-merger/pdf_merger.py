import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
import os

# Function to select PDF files
def select_pdfs():
    files = filedialog.askopenfilenames(
        title="Select PDF Files",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if files:
        pdf_list.delete(0, tk.END)
        for file in files:
            pdf_list.insert(tk.END, file)

# Function to merge selected PDFs
def merge_pdfs():
    pdf_files = pdf_list.get(0, tk.END)
    if not pdf_files:
        messagebox.showwarning("Warning", "No PDF files selected!")
        return

    output_path = filedialog.asksaveasfilename(
        title="Save Merged PDF As",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if output_path:
        merger = PdfMerger()
        try:
            for pdf in pdf_files:
                merger.append(pdf)
            merger.write(output_path)
            merger.close()
            messagebox.showinfo("Success", f"Merged PDF saved as:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs.\n{str(e)}")

# GUI Setup
root = tk.Tk()
root.title("PDF Merger App")
root.geometry("500x400")

tk.Label(root, text="Selected PDF Files:", font=("Arial", 12)).pack(pady=10)

pdf_list = tk.Listbox(root, width=60, height=10)
pdf_list.pack(pady=10)

tk.Button(root, text="Select PDFs", command=select_pdfs, bg="#6fa8dc", fg="white", width=15).pack(pady=5)
tk.Button(root, text="Merge PDFs", command=merge_pdfs, bg="#38761d", fg="white", width=15).pack(pady=5)

root.mainloop()
