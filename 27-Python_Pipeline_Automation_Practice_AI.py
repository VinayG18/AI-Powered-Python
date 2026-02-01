import pandas as pd

# -----------------------------
# 1. Load raw data
# -----------------------------
df = pd.read_csv("27-Pandas_Pipelines_Automation/raw_sales_data.csv")

# -----------------------------
# 2. Clean text columns
# -----------------------------
def clean_text(series):
    return (
        series.astype(str)
              .str.strip()
              .str.title()
              .str.replace(r"\s+", " ", regex=True)
    )

df["Customer_Name"] = clean_text(df["Customer_Name"])
df["City"] = clean_text(df["City"])
df["State"] = clean_text(df["State"])

# -----------------------------
# 3. Remove duplicate orders
# -----------------------------
df = df.drop_duplicates(subset=["Order_ID"])

# -----------------------------
# 4. Convert numeric columns
# -----------------------------
numeric_cols = ["Quantity", "Unit_Price", "Discount"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df[numeric_cols] = df[numeric_cols].fillna(0)

# -----------------------------
# 5. Calculate Total Sales
# -----------------------------
df["Total_Sales"] = (df["Quantity"] * df["Unit_Price"]) - df["Discount"]

# -----------------------------
# 6. Categorize order value
# -----------------------------
def sales_category(value):
    if value >= 10000:
        return "High"
    elif value >= 3000:
        return "Medium"
    else:
        return "Low"

df["Order_Value_Category"] = df["Total_Sales"].apply(sales_category)

# -----------------------------
# 7. Summary Reports
# -----------------------------
# Total sales by City
city_summary = (
    df.groupby("City", as_index=False)["Total_Sales"]
      .sum()
      .sort_values(by="Total_Sales", ascending=False)
)

# Total sales by Product Category
category_summary = (
    df.groupby("Product_Category", as_index=False)["Total_Sales"]
      .sum()
      .sort_values(by="Total_Sales", ascending=False)
)

# -----------------------------
# 8. Export outputs
# -----------------------------
df.to_csv("cleaned_sales_data.csv", index=False)
city_summary.to_csv("sales_by_city.csv", index=False)
category_summary.to_csv("sales_by_category.csv", index=False)

print("✅ Sales data pipeline executed successfully!")