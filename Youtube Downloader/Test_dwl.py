import tkinter as tk
from tkinter import ttk

def show_video_info(info_dict):
    """Display video info in a organized Tkinter window"""
    
    # Create the main window
    root = tk.Tk()
    root.title("Video Information")
    
    frame = ttk.Frame(root, padding="10")
    frame.pack(fill=tk.BOTH, expand=True)
    
    row = 0
    for key, value in info_dict.items():
        ttk.Label(frame, text=f"{key}:", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, padx=5, pady=2)
        
        ttk.Label(frame, text=value).grid(
            row=row, column=1, sticky=tk.W, padx=5, pady=2)
        
        row += 1
    
    
    root.mainloop()

# Example usage:
video_info = {
    "title": "How to Use Python with Tkinter",
    "author": "Python Tutorials",
    "views": "1,234,567",
    "Date": "2023-05-15"
}

show_video_info(video_info)