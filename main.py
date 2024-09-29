import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        value = float(entry_value.get())
        unit = variable.get()
        
        if unit == 'C':
            fahrenheit = celsius_to_fahrenheit(value)
            kelvin = celsius_to_kelvin(value)
            result_label.config(text=f"{value}°C = {fahrenheit:.2f}°F, {kelvin:.2f}K")
        elif unit == 'F':
            celsius = fahrenheit_to_celsius(value)
            kelvin = fahrenheit_to_kelvin(value)
            result_label.config(text=f"{value}°F = {celsius:.2f}°C, {kelvin:.2f}K")
        elif unit == 'K':
            celsius = kelvin_to_celsius(value)
            fahrenheit = kelvin_to_fahrenheit(value)
            result_label.config(text=f"{value}K = {celsius:.2f}°C, {fahrenheit:.2f}°F")
        else:
            result_label.config(text="Please select a valid unit.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric value for the temperature.")

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")
root.resizable(False, False)

# Entry for temperature value
tk.Label(root, text="Enter Temperature Value:", font=('Arial', 12)).pack(pady=10)
entry_value = tk.Entry(root, font=('Arial', 12), width=10)
entry_value.pack()

# Dropdown for temperature unit
variable = tk.StringVar(root)
variable.set("Select Unit")  # default value
units_menu = tk.OptionMenu(root, variable, "C", "F", "K")
units_menu.config(width=10, font=('Arial', 12))
units_menu.pack(pady=10)

# Button to convert temperature
convert_button = tk.Button(root, text="Convert", font=('Arial', 12), command=convert_temperature)
convert_button.pack(pady=10)

# Label to display results
result_label = tk.Label(root, text="", font=('Arial', 12), fg="blue")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
