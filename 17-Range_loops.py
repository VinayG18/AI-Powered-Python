# RANGE + LOOPS

# print("\n1) Print 1 to 5")
# for i in range(1, 6):
#     print(i)

# print("\n2) Even Numbers (0-18)")
# for i in range(0, 20, 2):
#     print(i)

# print("\n3) Countdown from 10 to 1")
# for i in range(10, 0, -1):
#     print(i) 

# print("\n4) Loop through list using index")
# items = ["Pen","Book","Laptop"]
# for i in range(len(items)):
#     print(i, items[i])

# print("\n5) Generate Employee IDs")
# for i in range(1, 6):
#     print("EMP -",i)

# print("\n6) Create years list")
# years = []
# for y in range(2015, 2026):
#     years.append(y)
# print(years)

# print("\n7) Clean city names using range")
# cities = [" mUMbai"," DElhi ","pune "]
# for i in range(len(cities)):
#     cities[i] = cities[i].strip().title()
# print(cities)

# print("\n8) Extract last 4 digits from IDs")
# ids = ["EMP-001122","EMP-550044","EMP-990011"]
# for i in range(len(ids)):
#     print(ids[i][-4:])


for i in range(1,4):
    for j in range(1,4):
        print(f"i Value : {i} j Value : {j}")