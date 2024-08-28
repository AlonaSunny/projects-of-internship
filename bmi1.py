import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get()) / 100  # Convert cm to meters
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}")
        
        # Display message based on BMI
        if bmi < 18.5:
            messagebox.showinfo("Result", "You are underweight.")
        elif 18.5 <= bmi < 24.9:
            messagebox.showinfo("Result", "You have a normal weight.")
        elif 25 <= bmi < 29.9:
            messagebox.showinfo("Result", "You are overweight.")
        else:
            messagebox.showinfo("Result", "You are obese.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")

# Height label and entry
height_label = tk.Label(root, text="Height (cm):")
height_label.pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Weight label and entry
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="BMI: ", font=("Arial", 14))
result_label.pack(pady=10)

# Run the application
root.mainloop()
