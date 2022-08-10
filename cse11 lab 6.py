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
# class Laptop:
#     laptopCount = 0
#     def __init__(self, name, count):
#         self.name = name
#         self.count = count
#         Laptop.laptopCount += self.count

#     @staticmethod
#     def advantage():
#         print("Laptops are portable")
#     @classmethod
#     def resetCount(cls):
#         Laptop.laptopCount = 0

# # Write your code here
# lenovo = Laptop("Lenovo", 5);
# dell = Laptop("Dell", 7);
# print(lenovo.name, lenovo.count)
# print(dell.name, dell.count)
# print("Total number of Laptops", Laptop.laptopCount)
# Laptop.advantage()
# Laptop.resetCount()
# print("Total number of Laptops", Laptop.laptopCount)

#############################  Task 10  ##########################
# class SultansDine:
#     def __init__(self, place, taka = 10000):
#         self.place = place
#         self.taka = taka
#     def details(self, branch = 0, taka = 0):
#         self.branch = branch
#         self.taka = taka
#         print("Total number of branch(s):", self.branch, "\nTotal Sell:", self.taka, "Taka")

#     def branchInformation(self):
#         print("Branch Name:", self.place, "\nBranch sell:", self.taka, "Taka")

#     def sellQuantity(self, num):
#         self.num = num
# Write your code here
# SultansDine.details()
# print('########################')
# dhanmodi = SultansDine('Dhanmondi')
# dhanmodi.sellQuantity(25)
# dhanmodi.branchInformation()
# print('-----------------------------------------')
# SultansDine.details()
# print('========================')
# baily_road = SultansDine('Baily Road')
# baily_road.sellQuantity(15)
# baily_road.branchInformation()
# print('-----------------------------------------')
# SultansDine.details()
# print('========================')
# gulshan = SultansDine('Gulshan')
# gulshan.sellQuantity(9)
# gulshan.branchInformation()
# print('-----------------------------------------')
# SultansDine.details()


















class SultansDine:
    total_sell = 0
    total_branch = 0
    info = []

    def __init__(self, place):
        self.place = place
        self.quantity = 0
        SultansDine.total_branch += 1
        SultansDine.info.append([self.place])

    def sellQuantity(self, quantity):
        self.quantity = quantity

    def branchInformation(self):
        total = 0
        if self.quantity < 10:
            total = self.quantity * 300
        elif self.quantity < 20:
            total = self.quantity * 350
        else:
            total = self.quantity * 400
        SultansDine.total_sell += total
        SultansDine.info[SultansDine.total_branch - 1] += [total]
        print(f"Branch Name: {self.place}\nBranch Sell: {total} Taka")

    @classmethod
    def details(cls):
        print(f"Total Number of branch(s): {SultansDine.total_branch}\nTotal Sell: {SultansDine.total_sell} Taka")
        for b, s in cls.info:
            print(f"Branch Name: {b}, Branch Sell: {s} Taka")
            print(f"Branch consists of total sell's: {round(s / SultansDine.total_sell * 100, 2)}%")

    # Driver class...


SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()
# 