# requirements.txt
# Install dependencies
# numpy
# pandas
# Pillow
# torch
# diffusers
# transformers

# main.py
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from data_generators.tabular_generator import generate_tabular_data
from data_generators.image_generator import generate_image_data

def generate_data():
    data_type = data_type_var.get()
    if data_type == "Tabular":
        num_columns = simpledialog.askinteger("Input", "Enter number of columns:")
        columns = []
        for _ in range(num_columns):
            col_name = simpledialog.askstring("Input", "Enter column name:")
            col_type = simpledialog.askstring("Input", "Enter data type (int, float, str):")
            columns.append((col_name, col_type))

        num_rows = simpledialog.askinteger("Input", "Enter number of rows:")
        data = generate_tabular_data(columns, num_rows)
        messagebox.showinfo("Success", f"Generated Tabular Data:\n{data.head()}\nSaved as tabular_data.csv")

    elif data_type == "Image":
        image_type = simpledialog.askstring("Input", "Enter image type (cars, bikes, airplanes):")
        num_images = simpledialog.askinteger("Input", "Enter number of images:")
        generate_image_data(image_type, num_images)
        messagebox.showinfo("Success", "Generated and saved image data.")

# Enhanced UI
app = tk.Tk()
app.title("Synthetic Data Generator")
app.configure(bg="#f0f8ff")  # Light blue background

frame = ttk.Frame(app, padding=20)
frame.grid(padx=20, pady=20)

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14), background="#f0f8ff", foreground="#333")
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.map("TButton", background=[("active", "#add8e6")])  # Light blue on hover

label = ttk.Label(frame, text="Select Data Type:")
label.grid(column=0, row=0, pady=10)

data_type_var = tk.StringVar()
type_menu = ttk.Combobox(frame, textvariable=data_type_var, font=("Helvetica", 12))
type_menu['values'] = ("Tabular", "Image")
type_menu.grid(column=1, row=0, pady=10, padx=10)

button = ttk.Button(frame, text="Generate Data", command=generate_data)
button.grid(column=0, row=1, columnspan=2, pady=20)

app.mainloop()