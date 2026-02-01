# STRING METHODS (VERY IMPORTANT)

text1 = "     hello python learners     "

# Remove Spaces
print("Original text:", text1)
print("Remove spaces:", text1.strip())
print("Remove right spaces:", text1.rstrip())
print("Remove left spaces:", text1.lstrip())

# Convert to capital letters (UpperCase)
print("Capital Letters:", text1.upper().strip())

# Convert to lower case
print("Lower Letters:", text1.lower().strip())

# Convert to proper case
print("Proper Letters:", text1.title().strip())

# Convert to capitalize case
print("Capitalize first letter:", text1.strip().capitalize())

# Replace
print("Replace python word with SQL:", text1.replace("python", "SQL"))

# Count occurrences of a letter of word
print("Count of o", text1.count("o"))

# Check if text start with something
print("Start with hello?", text1.strip().startswith("hello"))

print("End with hello?", text1.strip().endswith("hello"))

# Check if only numbers are presents in data
mobile="9876543210"
print("Is numeric:", mobile.isnumeric())

alpha="ABCD"
print("Is alphabetic:", alpha.isalpha())

alphaNumeric = "vsqr2422"
print("Is alphanumeric:", alphaNumeric.isalnum())

msg="Welcome to Python Course"

# Split string into list of words
words=msg.split()
print("Word list : ", words)

# Join back with hyphen
joined_text="-".join(words)
print("Joined text:", joined_text)

# Find position of letter
print("Index of P :",msg.find("P"))

# index() - Same but gives error if not found
print("Index of 1: ", msg.index("1"))

# Extract domain
email="student@example.com"
domain = email[email.find("@")+1:]
print("Domain :", domain)

# Advanced Example: Clean Price (Remove Special Characters)
# Example: "Price: ₹3500/-" → "3500"
price_text = "Price: ₹3500/-"
clean_price = price_text.replace("Price:", "") \
                        .replace("₹", "") \
                        .replace("/-", "") \
                        .strip()
print("Clean Price:", clean_price)
