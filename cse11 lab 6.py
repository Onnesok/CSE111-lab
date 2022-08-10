# ##########################  Task 1  ########################
# from traceback import print_tb


# class Student:
#     ID = 0
#     def __init__(self, name, department, age, cgpa):
#         self.name=name
#         self.department = department
#         self.age = age
#         self.cgpa = cgpa
#     def get_details(self):
#         if Student.ID == 0:
#             Student.ID = 1
#         print("ID:", Student.ID)
#         print("Name:", self.name, "\nDepartment:", self.department, "\nAge:", self.age, "\nCGPA:", self.cgpa)
#         Student.ID += 1

#     @classmethod
#     def from_String(cls, other):
#         name, dp, age, cg = other.split("-")
#         return Student(name, dp, age, cg)


# #Write your code here for subtasks 1-6.
# s1 = Student("Samin", "CSE", 21, 3.91)
# s1.get_details()
# print("-----------------------")
# s2 = Student("Fahim", "ECE", 21, 3.85)
# s2.get_details()
# print("-----------------------")
# s3 = Student("Tahura", "EEE", 22, 3.01)
# s3.get_details()
# print("-----------------------")
# s4 = Student.from_String("Sumaiya-BBA-23-3.96")
# s4.get_details()

# # Write the answer of subtask 5 here
# # Write the answer of subtask 6 here

# #You are not allowed to change the code above

############################  Task 6  ###########################
class Laptop:
    laptopCount = 0
    def __init__(self, name, count):
        self.name = name
        self.count = count
        Laptop.laptopCount += self.count

    @staticmethod
    def advantage():
        print("Laptops are portable")
    @classmethod
    def resetCount(cls):
        Laptop.laptopCount = 0

# Write your code here
lenovo = Laptop("Lenovo", 5);
dell = Laptop("Dell", 7);
print(lenovo.name, lenovo.count)
print(dell.name, dell.count)
print("Total number of Laptops", Laptop.laptopCount)
Laptop.advantage()
Laptop.resetCount()
print("Total number of Laptops", Laptop.laptopCount)

#############################  Task 10  ##########################

