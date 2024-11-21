import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_csv_to_excel(csv_file, excel_file):
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file)
        
        # Write the DataFrame to an Excel file
        df.to_excel(excel_file, index=False, engine='openpyxl')
        
        messagebox.showinfo("Success", f"Successfully converted '{csv_file}' to '{excel_file}'")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_csv_file():
    # Open a file dialog to select a CSV file
    file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
    csv_file_var.set(file_path)

def select_excel_file():
    # Open a file dialog to specify where to save the Excel file
    file_path = filedialog.asksaveasfilename(title="Save Excel file", defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    excel_file_var.set(file_path)

def convert_file():
    # Get the CSV and Excel file paths from the entry fields
    csv_file = csv_file_var.get()
    excel_file = excel_file_var.get()
    
    if not csv_file or not excel_file:
        messagebox.showwarning("Input Error", "Please select both the CSV file and the destination Excel file.")
    else:
        convert_csv_to_excel(csv_file, excel_file)

# Set up the main window
root = tk.Tk()
root.title("CSV to Excel Converter")

# Variable to hold file paths
csv_file_var = tk.StringVar()
excel_file_var = tk.StringVar()

# CSV File selection
tk.Label(root, text="CSV File:").grid(row=0, column=0, padx=10, pady=10)
csv_file_entry = tk.Entry(root, textvariable=csv_file_var, width=40)
csv_file_entry.grid(row=0, column=1, padx=10, pady=10)
csv_file_button = tk.Button(root, text="Browse", command=select_csv_file)
csv_file_button.grid(row=0, column=2, padx=10, pady=10)

# Excel File selection
tk.Label(root, text="Excel File:").grid(row=1, column=0, padx=10, pady=10)
excel_file_entry = tk.Entry(root, textvariable=excel_file_var, width=40)
excel_file_entry.grid(row=1, column=1, padx=10, pady=10)
excel_file_button = tk.Button(root, text="Browse", command=select_excel_file)
excel_file_button.grid(row=1, column=2, padx=10, pady=10)

# Convert Button
convert_button = tk.Button(root, text="Convert", command=convert_file)
convert_button.grid(row=2, column=1, padx=10, pady=20)

# Run the Tkinter event loop
root.mainloop()
