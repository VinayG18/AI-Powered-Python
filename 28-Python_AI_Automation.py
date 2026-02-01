import os
import pandas as pd

def csvs_to_excel():
    # Ask user for folder path
    folder_path = input("Paste the folder path containing CSV files and press Enter:\n").strip()

    # Validate folder path
    if not os.path.isdir(folder_path):
        print("❌ Invalid folder path.")
        return

    # Output Excel file path
    output_file = os.path.join(
        folder_path, 
        "All_CSV_Converted_Into_Sheets_Practice.xlsx"
    )

    # Get all CSV files in the folder
    csv_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".csv")]

    if not csv_files:
        print("❌ No CSV files found in the folder.")
        return

    # Create Excel workbook
    with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
        for csv_file in csv_files:
            csv_path = os.path.join(folder_path, csv_file)
            
            # Read CSV
            df = pd.read_csv(csv_path)
            
            # Sheet name = file name without extension (max 31 chars)
            sheet_name = os.path.splitext(csv_file)[0][:31]
            
            # Write to Excel sheet
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"✅ Excel file created successfully:\n{output_file}")

if __name__ == "__main__":
    csvs_to_excel()
