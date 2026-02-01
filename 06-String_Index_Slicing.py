# String Indexing

name="python"
print(name)
print(name[0])
print(name[-5])

# String Slicing
product = "Laptop pro 2026"
print(product[-4:])

text = "DataAnalysis"
# Extracting first 4 characters
print("First 4 letters:", text[0:4]) # Data

# Extracting characters from middle
print("Middle slice:", text[4:12]) # Analysis

# Extract till end
print("Till end:", text[4:]) # Analysis

# Extract from beginning
print("From start:", text[:4]) # Data

# Extract last 5 characters
print("Last 5 letters:", text[-5:]) # lysis

# Skip Text "DataAnalysis"
print("Skip Text :", text[0:12:3])
print("Reverse :", text[::-1])

# PRACTICAL USE CASES OF SLICING
# Extracting year from product code
product_code = "Laptop-Pro-2026"
year = product_code[-4:]
print("Product Year:", year)

# Extracting first name using slicing
full_name = "Rohit Sharma"
first_name = full_name[:5]
print("First name:", first_name)