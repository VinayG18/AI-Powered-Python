import pandas as pd
from datetime import datetime

# Load CSV file
df = pd.read_csv("day24_Employee_Data.csv")

# -------------------------------
# 1. Clean Employee_Name & City
# -------------------------------

df['Employee_Name'] = (
    df['Employee_Name']
    .astype(str)
    .str.strip()                 # remove leading/trailing spaces
    .str.title()                 # proper case
)

df['City'] = (
    df['City']
    .astype(str)
    .str.strip()
    .str.title()
)

df['Department'] = (
    df['Department']
    .astype(str)
    .str.strip()
    .str.title()
)

# -------------------------------
# 2. Remove duplicate records
# -------------------------------
# Remove full duplicate rows
df = df.drop_duplicates()

# Optional: Remove duplicates based on Employee_ID only
df = df.drop_duplicates(subset='Employee_ID')
# print(df.head())

# -------------------------------
# 3. Add Experience column
# -------------------------------
current_year = datetime.now().year

df['Experience'] = current_year - df['Joining_Year']

# -------------------------------
# Save cleaned data (optional)
# -------------------------------
df.to_csv("day24_Employee_Data_Cleaned.csv", index=False)

# Preview result
print(df.head())
