# ######################## Task 1  ############################
# class Marks:
#     def __init__(self, x):
#         self.mark = x
#     def __add__(self, x):
#         rs =  self.mark + x.mark
#         return Marks(rs)

# #Do not change the following lines of code
# Q1 = Marks(int(input("Quiz 1 (out of 10): ")))
# Q2 = Marks(int(input("Quiz 2 (out of 10): ")))
# Lab = Marks(int(input("Lab (out of 30): ")))
# Mid = Marks(int(input("Mid (out of 20): ")))
# Final = Marks(int(input("Final (out of 30): ")))
# total = Q1 + Q2 + Lab + Mid + Final
# print("Total marks: {}".format(total.mark))


######################## Task 2  ##############################
# class Teacher:
#     def __init__(self, name, dept):
#         self.__name = name
#         self.__dept = dept
#         self.__title = list()
    
#     def addCourse(self, x):
#         self.__title.append(x.title) 
#     def printDetail(self):
#         print("===============================")
#         print("Name:", self.__name)
#         print("Department:",self.__dept, "\nList of courses")
#         print("===============================")
#         print("\n".join(self.__title))
#         print("===============================")

# class Course:
#     def __init__(self, title):
#         self.title = title

# # Write your code here for subtasks 1-4
# t1 = Teacher("Saad Abdullah", "CSE")
# t2 = Teacher("Mumit Khan", "CSE")
# t3 = Teacher("Sadia Kazi", "CSE")
# c1 = Course("CSE 110 Programming Language I")
# c2 = Course("CSE 111 Programming Language-II")
# c3 = Course("CSE 220 Data Structures")
# c4 = Course("CSE 221 Algorithms")
# c5 = Course("CCSE 230 Discrete Mathematics")
# c6 = Course("CSE 310 Object Oriented Programming")
# c7 = Course("CSE 320 Data Communications")
# c8 = Course("CSE 340 Computer Architecture")
# t1.addCourse(c1)
# t1.addCourse(c2)
# t2.addCourse(c3)
# t2.addCourse(c4)
# t2.addCourse(c5)
# t3.addCourse(c6)
# t3.addCourse(c7)
# t3.addCourse(c8)
# t1.printDetail()
# t2.printDetail()
# t3.printDetail()

##########################  Task 3  ################################
# class Team:
#     def __init__(self, name = "default"):
#         self.__name = name
#         self.__player = list()

#     def setName(self, name):
#         self.__name = name
#     def addPlayer(self, player):
#         self.__player.append(player.pname)
#     def printDetail(self):
#         print("===========================")
#         print("Team:", self.__name, "\nList of players:")
#         print(self.__player)
#         print("===========================")

# class Player:
#     def __init__(self, pname):
#         self.pname = pname
# # Write your code here for subtasks 1-4
# b = Team()
# b.setName('Bangladesh')
# mashrafi = Player("Mashrafi")
# b.addPlayer(mashrafi)
# tamim = Player("Tamim")
# b.addPlayer(tamim)
# b.printDetail()
# a = Team("Australia")
# ponting = Player("Ponting")
# a.addPlayer(ponting)
# lee = Player("Lee")
# a.addPlayer(lee)
# a.printDetail()


###########################  Task 4  ####################################
# class Color:
#     def __init__(self, cname):
#         self.clr = cname
#     def __add__(self, other):
#         x = self.clr
#         y = other.clr
#         if (x == "red" or x == "yellow") and (y == "red" or y == "yellow") and x != y:
#             return Color("Orange")
#         elif (x == "red" or x == "blue") and (y == "red" or y == "blue") and x != y:
#             return Color("Violet")
#         elif (x == "yellow" or x == "blue") and (y == "yellow" or y == "blue") and x != y:
#             return Color("green")
#         else:
#             return Color(x)

# #Write your code here
# #Do not change the following lines of code
# C1 = Color(input("First Color: ").lower())
# C2 = Color(input("Second Color: ").lower())
# C3 = C1 + C2
# print("Color formed:", C3.clr)

##########################  Task 5   ##################################
# import math

# class Circle:
#     def __init__(self, r):
#         self.__radius = r
#     def getRadius(self):
#         return self.__radius
#     def  area(self):
#         return (math.pi * self.__radius**2)
#     def __add__(self, other):
#         return Circle(self.__radius + other.__radius)
# # Write your code here for subtasks 1-5
# c1 = Circle(4)
# print("First circle radius:" , c1.getRadius())
# print("First circle area:" ,c1.area())
# c2 = Circle(5)
# print("Second circle radius:" ,c2.getRadius())
# print("Second circle area:" ,c2.area())
# c3 = c1 + c2
# print("Third circle radius:" ,c3.getRadius())
# print("Third circle area:" ,c3.area())

##############################  Task 6  #################################
# class Triangle:
#     def __init__(self, f1, f2):
#         self.__f1 = f1
#         self.__f2 = f2
#     def getBase(self):
#         return self.__f1
#     def getHeight(self):
#         return self.__f2
#     def area(self):
#         rs = 0.5*self.__f1 * self.__f2
#         return rs
#     def __sub__(self, other):
#         ans1 = self.__f1 - other.__f1
#         ans2 = self.__f2 - other.__f2
#         return Triangle(ans1, ans2)

# # Write your code here for subtasks 1-5
# t1 = Triangle(10, 5)
# print("First Triangle Base:" , t1.getBase())
# print("First Triangle Height:" , t1.getHeight())
# print("First Triangle area:" ,t1.area())
# t2 = Triangle(5, 3)
# print("Second Triangle Base:" , t2.getBase())
# print("Second Triangle Height:" , t2.getHeight())
# print("Second Triangle area:" ,t2.area())
# t3 = t1 - t2
# print("Third Triangle Base:" , t3.getBase())
# print("Third Triangle Height:" , t3.getHeight())
# print("Third Triangle area:" ,t3.area())

################################  Task 7  ###############################
# class Dolls:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def detail(self):
#         rs = (f"Doll: {self.name} \nTotal price: {self.price} taka")
#         return rs
#     def __gt__(self, other):
#         if self.price > other.price:
#             return True
#         else:
#             return False
#     def __add__(self, other):
#         name = self.name + " "+ other.name
#         price = self.price + other.price
#         return Dolls(name, price)

# # Write your code here
# obj_1 = Dolls("Tweety", 2500)
# print(obj_1.detail())
# if obj_1 > obj_1:
#     print("Congratulations! You get the Tweety as a gift!")
# else:
#     print("Thank you!")
# print("=========================")
# obj_2 = Dolls("Daffy Duck", 1800)
# print(obj_2.detail())
# if obj_2 > obj_1:
#     print("Congratulations! You get the Tweety as a gift!")
# else:
#     print("Thank you!")
# print("=========================")
# obj_3 = Dolls("Bugs Bunny", 3000)
# print(obj_3.detail())
# if obj_3 > obj_1:
#     print("Congratulations! You get the Tweety as a gift!")
# else:
#     print("Thank you!")
# print("=========================")
# obj_4 = Dolls("Porky Pig", 1500)
# print(obj_4.detail())
# if obj_4 > obj_1:
#     print("Congratulations! You get the Tweety as a gift!")
# else:
#     print("Thank you!")
# print("=========================")
# obj_5 = obj_2 + obj_3
# print(obj_5.detail())
# if obj_5 > obj_1:
#     print("Congratulations! You get the Tweety as a gift!")
# else:
#     print("Thank you!")

############################  Task 8 ##################################
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def detail(self):
        return (self.x, self.y)

    def __sub__(self, other):
        f1 = self.x - other.x
        f2 = self.y - other.y
        return Coordinates(f1, f2)
    def __mul__(self, other):
        f1 = self.x * other.x
        f2 = self.y * other.y
        return Coordinates(f1, f2)
    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            return "The calculated coordinates are the same."
        else:
            return "The calculated coordinates are NOT the same."

#Write your code here
#Do not change the following lines of code
p1 = Coordinates(int(input()),int(input()))
p2 = Coordinates(int(input()),int(input()))
p4 = p1 - p2
print(p4.detail())
p5 = p1 * p2
print(p5.detail())
point_check = (p4 == p5)
print(point_check)