import tkinter as tk
from tkinter import ttk
import prcs_fetch
import datetime as dt
import time


monitoring = []
start_times = {}

def compare_and_add_to_table(prcs: dict, entry) -> None:
    entry = entry.get()
    print("Comparing entry:", entry)
    for name, status in prcs.items():
        if name.lower() == entry.lower():
            duplicate = False
            for item in tree.get_children():
                tree_item = tree.item(item, 'values')[0]
                if tree_item.lower() == name.lower():
                    duplicate = True
                    break
            if not duplicate:
                value = entry.strip()
                if value:
                    item_id = tree.insert("", "end", values=(value, status, "00:00:00"))
                    start_times[item_id] = time.time()

def update_elapsed_times():
    now = time.time()
    for item in tree.get_children():
        start = start_times.get(item)
        if start:
            elapsed = int(now - start)
            h = elapsed // 3600
            m = (elapsed % 3600) // 60
            s = elapsed % 60
            elapsed_to__str = f"{h:02}:{m:02}:{s:02}"
            name = tree.item(item, "values")[0]
            status = tree.item(item, "values")[1]
            tree.item(item, values=(name, status, elapsed_to__str))
    root.after(1000, update_elapsed_times)


    """
    for name, status in prcs.items():
        if name.lower() == entry.lower():
            # Check for duplicates in the Treeview
            duplicate = False
            for item in tree.get_children():
                item_value = tree.item(item, "values")[0]
                if item_value.lower() == name.lower():
                    duplicate = True
                    break
            if not duplicate:
                tree.insert("", "end", values=(name, status))
    """

def monitored_list(entry) -> list:
    monitoring.append(entry.get())
    print("Current monitoring list:", monitoring)
    tree.insert("", "end", values=(monitoring[-1],))
    return monitoring

def show_input(entry, event=None):
    user_input = entry.get()
    print("You entered:", user_input)

def on_click(entry):
    show_input(entry)
    #monitored_list(entry)
    compare_and_add_to_table(prcs_fetch.get_monitored(prcs_fetch.get_process_info()), entry)

    entry.delete(0, tk.END) # clear textbox


root = tk.Tk()
root.title("My Application")
root.geometry("853x480")

label = tk.Label(root, text="Main Title", font=("Arial", 24))
label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10)

button = tk.Button(root, text="Submit", command=lambda: on_click(entry), font=("Arial", 16))
button.pack(pady=10)

entry.bind("<Return>", lambda event: on_click(entry))

columns = ["Program", "Status", "Time"]
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)





tree.pack(expand=True, fill="both", padx=30, pady=30)

update_elapsed_times()

root.mainloop()