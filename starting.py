import tkinter as tk
from PIL import Image, ImageTk

def load_image():
    try:
        image = Image.open("1.png")
        image.thumbnail((360, 640))  # Resize the image to fit within 360x640 without distortion
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
    except FileNotFoundError:
        label.config(text="Error: 1.png not found.")
        
    # Schedule the closing of the window after 5 seconds
    root.after(2000, root.destroy)

# Create the main window
root = tk.Tk()
root.title("Image Viewer")
root.geometry("360x640")  # Set window size to 360x640

# Create a label to display the image
label = tk.Label(root)
label.pack(padx=0, pady=0)

# Load image automatically when the GUI is launched
load_image()

# Run the Tkinter event loop
root.mainloop()
