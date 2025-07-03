import os  

# name  = "Dhiraj"
# age  = 21
# print ("My name is",name, "and my age is ", age)

# list_ex = ["Dhiraj","vatsal","akhilesh","anish"]

# print(list_ex[1])

# for i in list_ex :
    # print(i)

# for i in range(0,len(list_ex),2) :
    # print ("the item index is  ",i , " -> and item name is ",list_ex[i])

# task question :
# fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]

# Print the 3rd item in the list 
# print(fruits[2])

# Use a for loop to print each fruit one by one
# for i in fruits :
    # print(i)

# Use a for loop with range() and step = 2 to:

# for i in range(0,len(fruits),2) :
    # print(f"Index {i} → Fruit: {fruits[i]}")

# example of list of list 
# passcount = 0   
# failcount = 0  
# students = [
#     ["Dhiraj", 95],
#     ["Vatsal", 32],
#     ["Anish", 77],
#     ["Akhilesh", 23],
#     ["nishant", 50]
# ]
# for i in students :
#     if i[1] >= 40 :
#         print (f"{i} score {i[1]} -> passed")
#         passcount = passcount+1
#     else :
#         print (f"{i} score {i[1]} -> failed")
#         failcount= failcount + 1
# print(f"Total passed -> {passcount}")
# print(f"total failed -> {failcount}")

# file handling 


# if os.path.exists("test.txt"):
#     print("✅ File exists")
# else:
#     print("❌ File does not exist")

# file = open("test.txt","w")
# file.write("Hello dhiraj \n")
# file.write("I am testing my code now")
# file.close()

# file = open("test.txt","r")
# content  = file.read()
# print(content)
# file.close()

# filename = "rplus_example.txt"

# # 🔐 Check if file exists
# if not os.path.exists(filename):
#     print("File not found. Creating it...")
#     with open(filename, "w") as f:
#         f.write("Initial line\n")

# # ✅ Now safely open in r+ mode
# with open(filename, "r+") as f:
#     content = f.read()
#     print("Old Content:\n", content)

#     f.write("New line added using r+ mode\n")

# filename = "rplus_example.txt"

# # 🔐 Check if file exists
# if not os.path.exists(filename):
#     print("File not found. Creating it...")
#     with open(filename, "w") as f:
#         f.write("Initial line\n")

# # ✅ Now safely open in r+ mode
# with open(filename, "r+") as f:
#     content = f.read()
#     print("Old Content:\n", content)

#     f.write("New line added using r+ mode\n")


# 🧹 Delete file if it exists
# if os.path.exists("bonus_eligible.txt"):
#     os.remove("bonus_eligible.txt")

# eligibleCount = 0
# noteligibleCount = 0

# employees = [
#     ["Dhiraj", 60000, "active"],
#     ["Vatsal", 45000, "active"],
#     ["Anish", 75000, "inactive"],
#     ["Akhilesh", 52000, "active"],
#     ["Riya", 50000, "inactive"]
# ]

# for i in employees:
#     name, salary, status = i  # cleaner unpacking
#     if status == "active" and salary > 50000:
#         print(f"{name} earns {salary} → {status} → Eligible for bonus!")
#         eligibleCount += 1

#         # Append eligible name to file with newline
#         with open("bonus_eligible.txt", "a") as f:
#             f.write(name + "\n")
#     else:
#         print(f"{name} earns {salary} → {status} → Not eligible")
#         noteligibleCount += 1

# # Final counts
# print(f"\nTotal eligible: {eligibleCount}")
# print(f"Total not eligible: {noteligibleCount}")

# # Show file content
# print("\nEligible Employees (from file):")
# with open("bonus_eligible.txt", "r") as f:
#     print(f.read())
