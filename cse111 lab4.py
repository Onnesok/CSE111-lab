######################### Task 1 ###############################
# class Customer:
#     def __init__(self, name):
#         self.name = name

#     def greet(self, name = None):
#         if name == None:
#             print("Hello!")
#         else:
#             print(f"Hello {name}!")
#     def purchase(self, *args):
#         count = len(args)
#         print(f"{self.name}, you purchased {count} items")
#         for i in range(len(args)):
#             print(args[i])

# customer_1 = Customer("Sam")
# customer_1.greet()
# customer_1.purchase("chips", "chocolate", "orange juice")
# print("-----------------------------")
# customer_2 = Customer("David")
# customer_2.greet("David")
# customer_2.purchase("orange juice")


##########################  Task 2  ############################
# class Panda:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age
#     def sleep(self, time = -20):
#         if time >= 3 and time <= 5:
#             return f"{self.name} sleeps {time} hours daily and should have Mixed Veggies"
#         elif time >= 6 and time <= 8:
#             return f"{self.name} sleeps {time} hours daily and should have Eggplant & Tofu"
#         elif time >= 9 and time <= 11:
#             return f"{self.name} sleeps {time} hours daily and should have Broccoli Chicken"
#         elif time == -20:
#             return f"{self.name}'s duration is unknown thus should have only bamboo leaves"
# #Write your code here for subtasks 1-4.
# panda1 = Panda("Kunfu","Male", 5)
# panda2=Panda("Pan Pan","Female",3)
# panda3=Panda("Ming Ming","Female",8)
# print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
# print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
# print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
# print("===========================")
# print(panda2.sleep(10))
# print(panda1.sleep(4))
# print(panda3.sleep())

##########################  Task 3  ############################
# class Cat:
#     def __init__(self, name = "White", work = "sitting"):
#         self.name = name
#         self.work = work
#         print(self.name, "cat is", self.work)
#     def printCat(self):
#         pass
#     def changeColor(self, color):
#         self.name = color
#         self.work = "sitting"
#         print(self.name, "cat is", self.work)
#         self.work = "jumping"
#  #Write your code here 
# c1 = Cat()
# c2 = Cat("Black")
# c3 = Cat("Brown", "jumping")
# c4 = Cat("Red", "purring")
# c1.printCat()
# c2.printCat()
# c3.printCat()
# c4.printCat()
# c1.changeColor("Blue")
# c3.changeColor("Purple")
# c1.printCat()
# c3.printCat()

############################## Task 4  ###############################
# class Student:
#     def __init__(self, name = "default Student"):
#         self.name = name

#     def quizcalc(self, q1 = 0, q2 = 0, q3 = 0):
#         score = (q1+q2+q3)/3
#         self.score = score

#     def printdetail(self):
#         print(f"Hello {self.name}")
#         print("Your average quiz score is", self.score)

# # Write your code here
# s1 = Student()
# s1.quizcalc(10)
# print('--------------------------------')
# s1.printdetail()
# s2 = Student('Harry')
# s2.quizcalc(10,8)
# print('--------------------------------')
# s2.printdetail()
# s3 = Student('Hermione')
# s3.quizcalc(10,9,10)
# print('--------------------------------')
# s3.printdetail()

########################  Task 5 #############################
class Student:
    def __init__(self, name, id, department = "CSE"):
        self.name = name
        self.id = id
        self.department = department
    def dailyEffort(self, effort):
        self.effort = effort
    def printDetails(self):
        print(f"Name: {self.name}\nID: {self.id}\nDepartment: {self.department}\nDaily Effort: {self.effort} hours")
        if self.effort <= 2:
            print("Suggestion: Should give more effort!'")
        elif self.effort <= 4:
            print("Suggestion: Keep up the good work!")
        else:
            print("Suggestion: Excellent! Now motivate others.'")

# Write your code here.
harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()

###########################  Task 6  ############################

