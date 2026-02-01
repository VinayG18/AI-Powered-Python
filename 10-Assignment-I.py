# Task I: Multi Level Verification System

# print("Meeting Room")

# security_code = int(input("Enter the security code:"))

# if security_code == 242210:
#     department = input("Enter your department:")
#     if department.capitalize() == "Backend":
#         access_level = int(input("Enter your access level:"))
#         if access_level >= 5:
#             print("Access Granted: Welcome to the meeting room.")
#         else:
#             print("Insufficient access level.")
#     else:
#         print("Access denied: Department not allowed.")
# else:
#     print("Invalid security code.")


# Task II: Online Exam Login

print("Online Exam Login")

registration_no = int(input("Enter registration number:"))

if registration_no == 2208:
    exam_subject = input("Enter exam subject:")
    if exam_subject.lower() == "python":
        password = int(input("Enter exam password:"))
        if password == 2422:
            print("Login successful! Start your exam.")
        else:
            print("Wrong password")
    else:
        print("Subject not available")
else:
    print("Registration failed")