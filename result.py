import tkinter as tk

def load_text(file_name, text_widget):
    try:
        with open(file_name, "r") as f:
            text = f.read()
            text_widget.config(state="normal")
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, text)
            text_widget.config(state="disabled")
    except FileNotFoundError:
        text_widget.config(state="normal")
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, f"Error: {file_name} not found.")
        text_widget.config(state="disabled")

root = tk.Tk()
root.title("vetU")
root.geometry("300x533")  # Set window size to 300x533

# Heading for Diagnosis text
label_diagnosis = tk.Label(root, text="Diagnosis")
label_diagnosis.pack(padx=10, pady=5)

# Diagnosis text
text_output_diagnosis = tk.Text(root, wrap="word", height=10, width=50)
text_output_diagnosis.pack(padx=10, pady=5)
text_output_diagnosis.config(state="disabled")
load_text("diagnosis.txt", text_output_diagnosis)

# Heading for Completion text
label_completion = tk.Label(root, text="Vets Near You")
label_completion.pack(padx=10, pady=5)

# Completion text
text_output_completion = tk.Text(root, wrap="word", height=10, width=50)
text_output_completion.pack(padx=10, pady=5)
text_output_completion.config(state="disabled")
load_text("completion.txt", text_output_completion)

image = tk.PhotoImage(file="/Users/asray/Desktop/Screenshot 2024-02-18 at 9.53.38 AM.png")  # Change "your_image.png" to the path of your image
image = image.subsample(2, 2)  # Adjust the subsampling factor as needed

# Display the image
image_label = tk.Label(root, image=image)
image_label.pack(padx=0, pady=0)
root.mainloop()
