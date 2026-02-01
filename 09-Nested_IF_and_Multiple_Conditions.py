# Nested IF and Multiple Conditions

# print("Check your eligibility")

# age = int(input("Enter your age:"))

# if age >= 18:
#     id_no = int(input("Enter your id no:"))
#     if id_no == 1722:
#         print("👍 you can enter")
#     else:
#         print("Wrong ID number")
# else:
#     print("You are underage.")


# Multiple conditions (and)
# age=int(input("Enter your age :"))
# residence=input("Are you Indian? : ")

# if age>=18 and residence.lower()=="yes":
#     print("Eligible to drive")
# else:
#     print("Not Eligible to drive")



# Multiple conditions (OR)
age=int(input("Enter your age :"))
residence=input("do you have licence : ")

if age>=18 or residence.lower()=="yes":
    print("Eligible to register")
else:
    print("Not Eligible to register")