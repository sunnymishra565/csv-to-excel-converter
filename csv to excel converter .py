import pandas as pd

def convert_csv_to_excel(csv_file, excel_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Write the DataFrame to an Excel file
    df.to_excel(excel_file, index=False, engine='openpyxl')
    
    print(f"Successfully converted '{csv_file}' to '{excel_file}'")

if __name__ == "__main__":
    # Input CSV file name
    csv_file = input("Enter the path of the CSV file: ")
    
    # Output Excel file name
    excel_file = input("Enter the desired path for the Excel file (e.g., output.xlsx): ")
    
    convert_csv_to_excel(csv_file, excel_file)