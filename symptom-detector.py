import cv2
import tkinter as tk
import time
from tkinter import messagebox
from PIL import Image, ImageTk
from roboflow import Roboflow

def capture_image():
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("UPLOAD_IMAGE.jpg", frame)
        time.sleep(3)
        messagebox.showinfo("Image Captured", "Runny Nose Detected")
        root.destroy()  
    else:
        messagebox.showerror("Error", "Failed to capture image")

def close_camera():
    cap.release()
    cv2.destroyAllWindows()
    root.destroy()

def update_feed():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        panel.img = img
        panel.config(image=img)
        panel.after(10, update_feed)
    else:
        messagebox.showerror("Error", "Failed to update camera feed")

root = tk.Tk()
root.title("vetU")
root.geometry("300x533")  # Set window size here

rf = Roboflow(api_key="K6o9V6gael78WQppoxJ6")
project = rf.workspace().project("builddsm")

cap = cv2.VideoCapture(0)

panel = tk.Label(root, width=300, height=425)  # Adjust panel size here
panel.pack(padx=10, pady=10)

capture_button = tk.Button(root, text="Capture Image", command=capture_image)
capture_button.pack(pady=5)



update_feed()

root.mainloop()
