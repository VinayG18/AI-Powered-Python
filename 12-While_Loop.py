# WHILE LOOP

# 1 Basic While Loop
i = 1
while i <= 10:
    print(i)
    i+=1

# # 2 Countdown
# n=5
# while n>0:
#     print(n)
#     n-=1


# 3️ Ask user until valid input
# num = ""
# while not num.isnumeric():
#     num = input("Enter any number: ")
#     print("Please Enter only number")
# print("Number accepted:", num)

# 4️ Loop through list using while
# items = ["Apple", "Banana", "Grapes","Orange"]
# i = 0
# while i < len(items):
#     print(items[i])
#     i += 1

# # 5️ Using break
# x = 1
# while x <= 10:
#     print(x)
#     if x == 5:
#         break
#     x += 1

# 6️ Using continue
# y = 0
# while y < 10:
#     y += 1
#     if y % 2 == 1:
#         continue
#     print(y)

# 7️ Password System (Advanced)
# password = ""
# attempts = 0

# while password != "admin123" and attempts < 3:
#     password = input("Enter password: ")
#     attempts += 1
#     if password == "admin123":
#         print("Login Successful")
#     else:
#         print("Wrong Password Try again, Attempt count :",attempts)
#     if attempts==3:
#         print("3 Attempt Expired")