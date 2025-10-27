import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(screen.get())))
            screen.set(result)
        except Exception:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# ------------------ UI ------------------
root = tk.Tk()
root.title("🧮 Calculator")
root.geometry("300x400")
root.config(bg="#222")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20 bold", justify="right", bd=8, relief=tk.RIDGE)
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

button_texts = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

for row_values in button_texts:
    frame = tk.Frame(root, bg="#222")
    frame.pack(expand=True, fill="both")
    for val in row_values:
        btn = tk.Button(
            frame, text=val, font="Arial 18", relief=tk.GROOVE,
            bg="#333", fg="white", borderwidth=0, padx=20, pady=10
        )
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        btn.bind("<Button-1>", click)

root.mainloop()
