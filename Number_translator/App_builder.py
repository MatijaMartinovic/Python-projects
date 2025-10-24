import tkinter as tk
from tkinter import ttk
from Calculations import *

# === Window setup ===
root = tk.Tk()
root.title("Number Processor")

# Proportional window size
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
width = int(screen_w * 0.4)
height = int(screen_h * 0.4)
x = (screen_w // 2) - (width // 2)
y = (screen_h // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")

# === Main layout ===
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# --- Title (centered) ---
title_frame = ttk.Frame(main_frame, borderwidth=2, relief="solid", padding=5)
title_frame.pack(pady=(10, 40))
title_label = ttk.Label(title_frame, text="Title", font=("Arial", 20))
title_label.pack(padx=30, pady=5)

# --- Content area (left-aligned) ---
content_frame = ttk.Frame(main_frame)
content_frame.pack(anchor="w", padx=30)

# Input row
ttk.Label(content_frame, text="Input number:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
entry = ttk.Entry(content_frame, width=15, font=("Arial", 12))
entry.grid(row=0, column=1, sticky="w", padx=(10, 0), pady=5)

# Result label
result_label = ttk.Label(content_frame, text="Result:", font=("Arial", 12))
result_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=(15, 5))

# Button area
button_frame = ttk.Frame(content_frame)
button_frame.grid(row=2, column=0, columnspan=2, sticky="w", pady=10)


# === Functions ===
def do_logic():
    try:
        result = dec_to_bin(int(entry.get()))
        display_results(result)
    except ValueError:
        display_results("Invalid Input!")
    return result

def clear_input():
    entry.delete(0, tk.END)
    entry.focus_set()

def display_results(res):
    result_label.configure(text=f"Result: {res}")
    clear_input()


def add_button(text, command):
    """Add a new button dynamically."""
    btn = ttk.Button(button_frame, text=text, command=command)
    btn.pack(side="left", padx=5)


# Add your first button
add_button("Double Number", do_logic)


# === Run ===

if __name__ == "__main__":
    root.mainloop()
