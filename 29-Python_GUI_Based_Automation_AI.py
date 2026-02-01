import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

# -----------------------------
# Main Application
# -----------------------------
class DataCleaningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Data Cleaning Automation")
        self.root.geometry("650x450")
        self.root.resizable(False, False)

        self.input_file = tk.StringVar()
        self.output_folder = tk.StringVar()

        # Checkbox variables
        self.remove_duplicates = tk.BooleanVar()
        self.remove_blank_rows = tk.BooleanVar()
        self.trim_spaces = tk.BooleanVar()
        self.title_case = tk.BooleanVar()

        self.create_widgets()

    # -----------------------------
    # UI Components
    # -----------------------------
    def create_widgets(self):
        # Input File
        tk.Label(self.root, text="Input Excel File:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=5)
        tk.Entry(self.root, textvariable=self.input_file, width=70).pack(padx=20)
        tk.Button(self.root, text="Browse", command=self.browse_input).pack(pady=5)

        # Cleaning Options
        tk.Label(self.root, text="Data Cleaning Options:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=10)

        tk.Checkbutton(self.root, text="Remove Duplicate Rows", variable=self.remove_duplicates).pack(anchor="w", padx=40)
        tk.Checkbutton(self.root, text="Remove Blank Rows", variable=self.remove_blank_rows).pack(anchor="w", padx=40)
        tk.Checkbutton(self.root, text="Remove Leading & Trailing Spaces (Text Columns)", variable=self.trim_spaces).pack(anchor="w", padx=40)
        tk.Checkbutton(self.root, text="Convert Text Columns to Title Case", variable=self.title_case).pack(anchor="w", padx=40)

        # Output Folder
        tk.Label(self.root, text="Output Folder:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20, pady=10)
        tk.Entry(self.root, textvariable=self.output_folder, width=70).pack(padx=20)
        tk.Button(self.root, text="Browse", command=self.browse_output).pack(pady=5)

        # Action Buttons
        tk.Button(self.root, text="Clean Data", bg="green", fg="white", width=15, command=self.clean_data).pack(pady=10)
        tk.Button(self.root, text="Reset Paths", width=15, command=self.reset_paths).pack(pady=5)
        tk.Button(self.root, text="Reset Checkboxes", width=15, command=self.reset_checkboxes).pack(pady=5)

    # -----------------------------
    # Browse Input File
    # -----------------------------
    def browse_input(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Excel Files", "*.xlsx *.xls")]
        )
        if file_path:
            self.input_file.set(file_path)

    # -----------------------------
    # Browse Output Folder
    # -----------------------------
    def browse_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder.set(folder)

    # -----------------------------
    # Core Cleaning Logic
    # -----------------------------
    def clean_data(self):
        if not self.input_file.get() or not self.output_folder.get():
            messagebox.showerror("Error", "Please select input file and output folder.")
            return

        try:
            df = pd.read_excel(self.input_file.get())

            # Remove duplicate rows
            if self.remove_duplicates.get():
                df = df.drop_duplicates()

            # Remove blank rows
            if self.remove_blank_rows.get():
                df = df.dropna(how="all")

            # Process text columns
            text_columns = df.select_dtypes(include="object").columns

            if self.trim_spaces.get():
                for col in text_columns:
                    df[col] = df[col].astype(str).str.strip()

            if self.title_case.get():
                for col in text_columns:
                    df[col] = df[col].astype(str).str.title()

            # Save file
            input_name = os.path.basename(self.input_file.get())
            output_path = os.path.join(self.output_folder.get(), f"practical_cleaned_{input_name}")
            df.to_excel(output_path, index=False)

            messagebox.showinfo("Success", f"Cleaned file saved:\n{output_path}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # -----------------------------
    # Reset Functions
    # -----------------------------
    def reset_paths(self):
        self.input_file.set("")
        self.output_folder.set("")

    def reset_checkboxes(self):
        self.remove_duplicates.set(False)
        self.remove_blank_rows.set(False)
        self.trim_spaces.set(False)
        self.title_case.set(False)


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = DataCleaningApp(root)
    root.mainloop()
