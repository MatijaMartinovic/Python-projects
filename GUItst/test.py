import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
tree = ttk.Treeview(root, columns=("Value", "Elapsed"), show="headings")
tree.heading("Value", text="Value")
tree.heading("Elapsed", text="Elapsed")
tree.pack()

start_times = {}

def add_entry():
    value = entry.get().strip()
    if value:
        item_id = tree.insert("", "end", values=(value, "00:00:00"))
        start_times[item_id] = time.time()
        entry.delete(0, tk.END)

def update_elapsed_times():
    now = time.time()
    for item_id in tree.get_children():
        start = start_times.get(item_id)
        if start:
            elapsed = int(now - start)
            h = elapsed // 3600
            m = (elapsed % 3600) // 60
            s = elapsed % 60
            elapsed_str = f"{h:02}:{m:02}:{s:02}"
            value = tree.item(item_id, "values")[0]
            tree.item(item_id, values=(value, elapsed_str))
    root.after(1000, update_elapsed_times)

entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Add", command=add_entry)
button.pack()

update_elapsed_times()
root.mainloop()