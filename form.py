import tkinter as tk


def submit_form():
    with open("symptoms_data.txt", "w") as file:
        file.write(f"So we have gotten these results of a dog from the owner and we want you to figure out what is wrong with the dog. Figure out the health status of the dog and the disease it may or not have")
        file.write(f"Breed: {breed_entry.get()}\n")
        file.write(f"Color: {color_entry.get()}\n")
        file.write(f"Size Standing (inches): {size_scale.get()}\n")
        file.write(f"Temperament: {temperament_entry.get()}\n")
        file.write(f"Weight (lbs): {weight_scale.get()}\n")
        file.write(f"Energy Level(1 - low 5- high ): {energy_scale.get()}\n")
        file.write(f"Heart Rate(1 - low 3- high ): {heart_scale.get()}\n")
        file.write(f"Respiratory Rate: {respiratory_scale.get()}\n")
        file.write(f"Temperature (1 - low, 2 - good, 3- high ): {temperature_scale.get()}\n")
        file.write(f"Coat Condition: {coat_entry.get()}\n")
        file.write(f"Appetite: {appetite_entry.get()}\n")
        file.write(f"Thirst: {thirst_entry.get()}\n")
        file.write(f"Behavior Change: {behavioral_entry.get()}\n")
        file.write(f"Eye Symptoms: {eye_entry.get()}\n")
    root.destroy()


root = tk.Tk()
root.title("vetU")
root.geometry("300x533")  # Set window size here


frame = tk.Frame(root)
frame.pack(padx=10, pady=10)



# Breed
breed_label = tk.Label(frame, text="Breed")
breed_label.grid(row=0, column=0, sticky="w")
breed_entry = tk.Entry(frame)
breed_entry.grid(row=0, column=1)

# Color
color_label = tk.Label(frame, text="Color")
color_label.grid(row=1, column=0, sticky="w")
color_entry = tk.Entry(frame)
color_entry.grid(row=1, column=1)

# Size
size_label = tk.Label(frame, text="Height")
size_label.grid(row=2, column=0, sticky="w")
size_scale = tk.Scale(frame, from_=4, to=100, orient="horizontal")
size_scale.grid(row=2, column=1)

# Temperament
temperament_label = tk.Label(frame, text="Temperament")
temperament_label.grid(row=3, column=0, sticky="w")
temperament_entry = tk.Entry(frame)
temperament_entry.grid(row=3, column=1)

# Weight
weight_label = tk.Label(frame, text="Weight")
weight_label.grid(row=4, column=0, sticky="w")
weight_scale = tk.Scale(frame, from_=2, to=200, orient="horizontal")
weight_scale.grid(row=4, column=1)

# Energy Level
energy_label = tk.Label(frame, text="Energy Level")
energy_label.grid(row=6, column=0, sticky="w")
energy_scale = tk.Scale(frame, from_=1, to=5, orient="horizontal")
energy_scale.grid(row=6, column=1)

# Heart Rate
heart_label = tk.Label(frame, text="Heart Rate")
heart_label.grid(row=7, column=0, sticky="w")
heart_scale = tk.Scale(frame, from_=1, to=3, orient="horizontal")
heart_scale.grid(row=7, column=1)

# Respiratory Rate
respiratory_label = tk.Label(frame, text="Breathing")
respiratory_label.grid(row=9, column=0, sticky="w")
respiratory_scale = tk.Scale(frame, from_=1, to=3, orient="horizontal")
respiratory_scale.grid(row=9, column=1)

# Body Temperature
temperature_label = tk.Label(frame, text="Temperature")
temperature_label.grid(row=11, column=0, sticky="w")
temperature_scale = tk.Scale(frame, from_=1, to=3, orient="horizontal")
temperature_scale.grid(row=11, column=1)

# Coat Condition
coat_label = tk.Label(frame, text="Coat")
coat_label.grid(row=13, column=0, sticky="w")
coat_entry = tk.Entry(frame)
coat_entry.grid(row=13, column=1)


# Appetite
appetite_label = tk.Label(frame, text="Appetite")
appetite_label.grid(row=15, column=0, sticky="w")
appetite_entry = tk.Entry(frame)
appetite_entry.grid(row=15, column=1)

# Thirst
thirst_label = tk.Label(frame, text="Thirst")
thirst_label.grid(row=16, column=0, sticky="w")
thirst_entry = tk.Entry(frame)
thirst_entry.grid(row=16, column=1)

# Behavioral Changes
behavioral_label = tk.Label(frame, text="Behavior")
behavioral_label.grid(row=17, column=0, sticky="w")
behavioral_entry = tk.Entry(frame)
behavioral_entry.grid(row=17, column=1)

# Eye Symptoms
eye_label = tk.Label(frame, text="Eyes")
eye_label.grid(row=18, column=0, sticky="w")
eye_entry = tk.Entry(frame)
eye_entry.grid(row=18, column=1)



# Submit button
submit_button = tk.Button(frame, text="Submit", command=submit_form)
submit_button.grid(row=22, column=0, columnspan=2, pady=10)



root.mainloop()
