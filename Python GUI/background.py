from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

# Load JPG or other image types using PIL
image = Image.open("blow.png")  # change to your image file
bg_image = ImageTk.PhotoImage(image)

# Set it as a background
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add other widgets
label = tk.Label(root, text="Hello", bg="white")
label.pack(pady=20)

root.mainloop()