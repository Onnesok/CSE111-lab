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


#Write your code here
#Do not change the following lines of code
C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)