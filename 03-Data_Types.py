# 1. Text Type
# String
customer_name = "Vidhi"
print("Customer Name: ", customer_name)
print("Customer DataType is: ", type(customer_name))

# 2. Numeric Data Type
# 2.1: Integer - Complete Number
rating = 4
order_qty = 3
print("Rating Data Type: ", type(rating))
print("Order Qty Data Type: ", type(order_qty))

# 2.2 Float - Decimal Number
order_amount = 360.55
print("order_amt data type", type(order_amount))

# 2.3 Complex Number
a = 3+4j
print(type(a))

# 3. Boolean - True/False
is_paid = True
print(is_paid, type(is_paid))


# 4. Sequence Type
# 4.1 List
cities = ["Mumbai", "Delhi", "Pune", "Chennai"]
print(cities)
print(type(cities))

# 4.2 Tuple
dimensions = (1920, 1080)
print(dimensions)
print(type(dimensions))

# 4.3 Range
num = range(0,6)
print(list(num)) # [0,1,2,3,4]
print(type(num))


# 5 Mapping Type
# dict (dictionary)
student = {
    "name": "Vinay",
    "age": 30,
    "city": "Surat"
}
print(student)
print(type(student))

# 6 Set
number = {1, 2, 2, 3, 4, 5}
print(number) # Output: {1, 2, 3, 4, 5}
print(type(number))

# Frozenset
number = ([1, 2, 2, 3, 4, 5])
print(number) # Output: [1, 2, 2, 3, 4, 5]
print(type(number))

# 7 None Type - No Value
remarks = None
print(remarks, type(remarks))
