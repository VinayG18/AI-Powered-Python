# String, List and Number Functions (Set 2)

# STRING FUNCTIONS
text = "banana"
print(text.count("a"))

# print("hello.py".endswith(".py"))

# print("Sales_Report.csv".startswith("Saes"))

# print("123".isdigit())
# print("4545".isalpha())
# print("A1B2".isalnum())

# print("Line1\nLine2\nLine3")

# print("Line1\nLine2\nLine3".splitlines())

# LIST FUNCTIONS
# nums = [5, 2, 7, 1]
# nums.sort()             # Sorting
# print(nums)

# fruits = ["Banana", "Apple", "Mango"]
# print(sorted(fruits))

# marks = [10,20,30]
# print(min(marks), max(marks), sum(marks))

# mylist = [1,2,1,3,1,5,8,5]
# print(mylist.count(5))
# print(mylist.index(8))

# a = [1,2]
# b = [3,4]
# a.extend(b)
# print(a)


# NUMBER FUNCTIONS
# print(round(3.678, 0))
# print(abs(-50))
# print(pow(25, 2))
# print(divmod(10, 2))
# print(sum([5,5,5], 5))

# PRACTICAL EXAMPLES
# products = [" mobile ", "Laptop", "  TABLET"]
# clean = [p.strip().title() for p in products]
# clean.sort()
# print(clean)

emails = ["rohit@gmail.com", "sneha1@yahoo.com"]
domains = [mail[mail.find("@")+1:] for mail in emails]
print(domains)

mobiles = ["9876543210", "9988AB2211", "12345"]
valid = [m for m in mobiles if m.isdigit() and len(m)==10]
print(valid)
