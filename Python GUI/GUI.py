import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import processes as pr
from datetime import datetime, timedelta
import json
import os
import pystray
import threading

running = True

session_start_times = {}
total_playtimes = {}



def on_close():
    global running
    running = False
    #root.destroy()
    save_playtimes()
    save_sessions()
    hide_window()

def create_image():
    image = Image.new('RGB', (64, 64), color=(255,255,255))
    d = ImageDraw.Draw(image)
    d.ellipse((16,16,48,48), fill='black')
    return image

def on_quit(icon, item):
    icon.stop()
    root.quit()

def show_window(icon, item):
    icon.stop()
    root.after(0, root.deiconify)

def hide_window():
    root.withdraw()
    image = create_image()
    menu = pystray.Menu(
        pystray.MenuItem("Open", show_window),
        pystray.MenuItem("Quit", on_quit)
        )
    icon = pystray.Icon("name", image, "Observer", menu)
    threading.Thread(target=icon.run, daemon=True).start()

def clear_table():
    for item in tree.get_children():
        tree.delete(item)

def load_playtimes():
    if not os.path.exists("playtimes.json"):
        return {}
    
    with open("playtimes.json", "r") as f:
        data = json.load(f)

    return {k: timedelta(seconds=float(v)) for k, v in data.items()}

total_playtimes = load_playtimes()

def load_sessions():
    if not os.path.exists("sessions.json"):
        return {}
    
    with open("sessions.json", "r") as f:
        data = json.load(f)
    
    return {k: datetime.fromtimestamp(v) for k, v in data.items()}

recovered_sessions = load_sessions()

def save_sessions():
    data = {k: v.timestamp() for k, v in session_start_times.items()}

    with open("sessions.json", "w") as f:
        json.dump(data, f)

def save_playtimes():
    data = {k: v.total_seconds() for k, v in total_playtimes.items()}
    with open("playtimes.json", "w") as f:
        json.dump(data, f)


root = tk.Tk()
root.title("Observer")
root.geometry("1280x720")
root.resizable(False, False)
#root.configure(bg="red")

root.protocol("WM_DELETE_WINDOW", on_close)

"""image = Image.open("Outline.png")
bg_image = ImageTk.PhotoImage(image)

bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)"""


label = tk.Label(root, text = "Welcome to The Observer", font=("Calibri", 32, "bold"))
label.pack(pady=50)

entry = tk.Entry(root, width=30, font=("Calibri", 14))
entry.pack(pady=10)

result = tk.Label(root, text="Input:")
result.pack(pady=10)

def on_click():
    cur_text = result.cget("text")
    usr_input = entry.get()
    if usr_input == "":
        result.config(text = "Input:")
    else:
        result.config(text = cur_text + ' ' + usr_input)

button = tk.Button(root, text="Send", command=on_click)
button.pack(pady=10)

tree = ttk.Treeview(root, columns=("Game", "Playtime Session", "Total Playtime"), show="headings")
tree.heading("Game", text="Game")
tree.heading("Playtime Session", text="Session Playtime")
tree.heading("Total Playtime", text="Total Playtime")

tree.pack(padx=30, pady=30 ,fill="both", expand=True)

monitored = pr.monitored_present(pr.register_running_processes())
for name, start in recovered_sessions.items():
    if name in monitored:
        session_start_times[name] = start
    else:
        duration = datetime.now() - start
        total_playtimes[name] = total_playtimes.get(name, timedelta()) + duration

"""def check_for_monitored_processes():

    monitored = pr.monitored_present(pr.register_running_processes())
    print(monitored)
    
    if not running:
        return
    print("working")
    for prcs in monitored:
        if not tree.exists(prcs):
            tree.insert("", "end", iid=prcs, values=(prcs, "Not running"))
    root.after(2000, check_for_monitored_processes)"""

def check_for_monitored_processes():
    monitored = pr.monitored_present(pr.register_running_processes())
    print(monitored)
    
    if not running:
        return

    for prcs in monitored:
        if not tree.exists(prcs):
            tree.insert("", "end", iid=prcs, values=(prcs, "0:00:00", "0:00:00"))

        if prcs not in session_start_times:
            session_start_times[prcs] = datetime.now()

        session_duration = datetime.now() - session_start_times[prcs]
        total = total_playtimes.get(prcs, timedelta())
        tree.item(prcs, values=(prcs, str(session_duration).split(".")[0], str(total).split(".")[0]))

    for prcs in list(session_start_times):
        if prcs not in monitored:
            start_time = session_start_times.pop(prcs)
            session_duration = datetime.now() - start_time
            total_playtimes[prcs] = total_playtimes.get(prcs, timedelta()) + session_duration

            tree.item(prcs, values=(prcs, "0:00:00", str(total_playtimes[prcs]).split(".")[0]))

    root.after(1000, check_for_monitored_processes)




# Invisble
excluded_widgets = [entry, button]

def widget_color(widget, bg_color):
    for widget in root.winfo_children():
        if widget in excluded_widgets:
            pass
        else:
            widget.configure(bg=bg_color)


# RUN APP
check_for_monitored_processes()
root.mainloop()