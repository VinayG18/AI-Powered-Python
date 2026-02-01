# Sets in Python

# Create Set
fruits = {"Apple", "Banana", "Apple", "Mango"}
print(fruits)

# Add Item
fruits.add("Orange")
print(fruits)

# Remove Item
fruits.discard("Banana")
print(fruits)

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union", a | b)
print("Intersection", a & b)
print("Difference", a - b)
print("Symmentric Difference", a ^ b)

# Remove Duplicates
cities = ["Mumbai","Pune","Delhi","Mumbai"]
unique = set(cities)
print("Unique cities", unique)

# Missing Values
list1 = {"SQL","Excel","Power BI"}
list2 = {"SQL", "Power BI"}
missing = list1 - list2
print("Missing", missing)

# Common Skills
deptA = {"SQL","Excel","Python"}
deptB = {"Excel","Python","Power BI"}
print("Common Skills", deptA & deptB)