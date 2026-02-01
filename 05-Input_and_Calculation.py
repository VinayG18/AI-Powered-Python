# Input and Typecasting

# name = input("Enter your name:")
# print("Welcome ", name)

# age=int(input("Enter your age:"))
# print(type(age))
# age=age+5
# print("Your age is :", age)

# temprature=float(input("Enter today's temp :"))
# print(type(temprature))

# Convert number to string
# sales = 50000
# text = "Total sales: " + str(sales)
# print(text)

#Total Sales Calculator
# product = input("Product Name: ")
# quantity = int(input("Enter quantity sold: "))
# price_per_unit = float(input("Enter price per unit"))

# total_sales = quantity * price_per_unit


# print("______________________")
# print("Product:", product)
# print("Total Sales Amount =", total_sales)


# fnum=int(input("Enter first num:"))
# snum=int(input("Enter Second num:"))

# sum=fnum+snum
# print(sum)

# Assignment: Salary Slip Calculator
employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
bonus_amount = float(input("Enter bonus amount: "))
tax_percentage = float(input("Enter tax percenatge(%): "))

gross_salary = basic_salary + bonus_amount
tax_amount = gross_salary * (tax_percentage/100)

print('Salary Slip')
print('Employee Name', employee_name)
print('Basic Salary', basic_salary)
print('Bonus Amount', bonus_amount)
print('Tax Percentage', tax_percentage)
print('Gross Salary', basic_salary + bonus_amount)
print('Tax Amount', tax_amount)
print("Net Salary", gross_salary - tax_amount)
