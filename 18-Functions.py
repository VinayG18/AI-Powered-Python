# Functions (def, return)

def greet():
    print("Hello Python Learners")
    print("Learning Functions")

greet()

# def welcome(name):
#     print("Welcome", name)
    
# welcome("Virat Kohli")


# def add(a,b):
#     print("a+b : ", a+b)
#     print("a*b : ", a*b)

# add(10,30)


# def add(a,b):
#     return a + b


# def multiple(x):
#     return x*2 

# result = multiple(add(10,30))

# print(result)




# def clean_text(value):
#     return value.strip().title()

# output=clean_text("    muMbai   ")
# print(output)


# def fix_city(city):
#     city = city.lower().strip()
#     city = city.replace("mombai", "mumbai")
#     city = city.replace("kolkatta", "kolkata")
#     return city.title()


# print(fix_city("  mombai  "))



# def get_year(code):
#     return code[-4:]

# print(get_year("Laptop-2024"))


# def is_valid_email(email):
#     return "@" in email and "." in email


# print(is_valid_email("test@gmail.com"))



# def total_salary(basic, bonus):
#     return basic + bonus

# print(total_salary(20000, 5000))



# def stats(nums):
#     return min(nums), max(nums), sum(nums)/len(nums)

# print(stats([10, 20, 30]))


# def clean_list(values):
#     cleaned = []
#     for v in values:
#         cleaned.append(v.strip().title())
#     return cleaned

# print(clean_list([" delhi ", " MUMBAI", "pUne "]))