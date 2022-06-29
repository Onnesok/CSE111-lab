#############################  Task 1  ##############################

# class calculator:
#     def __init__(self) -> None:
#         self.val1 = "value"
#         self.val2 = "value"
#     def add(self):
#         print(self.val1 + self.val2)
#     def substract(self):
#         print(self.val1 - self.val2)
#     def multiply(self):
#         print(self.val1 - self.val2)
#     def divide(self):
#         print(self.val1 / self.val2)

# c1 = calculator()
# print("Let's calculate!")

# val1 = float(input("Value 1:"))
# op = input("Operator:")
# val2 = float(input("Value 2:"))

# c1.val1 = val1
# c1.val2 = val2

# if op == "+":
#     c1.add()
# elif op == "-":
#     c1.substract()
# elif op == "*":
#     c1.multiply()
# elif op == "/":
#     c1.divide()




####################################  Task 2   ##################################

# class Course:
#     def __init__(self, course, faculty, section):
#         self.course = course
#         self.faculty = faculty
#         self.section = section
#     def detail(self):
#         print(f"{self.course}-{self.faculty}-{self.section}")


# # Write your code here

# c1 = Course("CSE110", "TBA", 8)
# c1.detail()
# print("===============")
# c2 = Course("CSE111", "TBA", 9)
# c2.detail()


###################################  Task 3  ########################################

# class Patient:
#     def __init__(self, name, age, weight, height):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.height = height
#     def printDetails(self):
        
#         bmi = self.weight / (self.height/100)**2
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Weight:", self.weight, "kg")
#         print("Height:", self.height, "cm")
#         print("BMI:", bmi)
# # Write your code here
# p1 = Patient("A", 55, 63.0, 158.0)
# p1.printDetails()
# print("====================")
# p2 = Patient("B", 53, 61.0, 149.0)
# p2.printDetails()

################################  Task 4  ##########################################

# class Vehicle:
#     def __init__(self) -> None:
#         self.x, self.y = 0, 0
#     def print_position(self):
#         print(f"({self.x},{self.y})")
#     def moveUp(self):
#         self.y += 1
#     def moveLeft(self):
#         self.x -= 1
#     def moveDown(self):
#         self.y -= 1
#     def moveRight(self):
#         self.x += 1

# # Write your class here
# car = Vehicle()
# car.print_position()
# car.moveUp()
# car.print_position()
# car.moveLeft()
# car.print_position()
# car.moveDown()
# car.print_position()
# car.moveRight()


#################################  Task 5  #########################################

# class Shape:
#   def __init__(self, shape_name, num1, num2):
#     self.shape_name = shape_name
#     self.num1 = num1
#     self.num2 = num2

#   def area(self):
#     if self.shape_name == "Triangle":
#       area = (self.num1*self.num2)/2
#       print("Area:", area)
#     elif self.shape_name == "Square":
#       area = self.num1*self.num2
#       print("Area:", area)
#     elif self.shape_name == "Rhombus":
#       area = (self.num1*self.num2)/2
#       print("Area:", area)
#     elif self.shape_name == "Rectangle":
#       area = self.num1 * self.num2
#       print("Area:", area)
#     else:
#       area = "Shape unknown"
#       print("Area:", area)


# # Write your code here
# triangle = Shape("Triangle",10,25)
# triangle.area()
# print("==========================")
# square = Shape("Square",10,10)
# square.area()
# print("==========================")
# rhombus = Shape("Rhombus",18,25)
# rhombus.area()
# print("==========================")
# rectangle = Shape("Rectangle",15,30)
# rectangle.area()
# print("==========================")
# trapezium = Shape("Trapezium",15,30)
# trapezium.area()

#################################  Task 6 ##########################################

# class Calculator:
#     def __init__(self):
#         print("Calculator is ready!")

#     def calculate(self, num1, num2, sign):
#         self.num1 = num1
#         self.num2=num2
#         self.sign = sign
#         if self.sign == "+":
#             val = self.num1+self.num2
#             return val
#         elif self.sign == "-":
#             val = self.num1-self.num2
#             return val
#         elif self.sign == "*":
#             val = self.num1*self.num2
#             return val
#         elif self.sign == "/":
#             val = self.num1/self.num2
#             return val

#     def showCalculation(self):
#         if self.sign == "+":
#             print(f"{self.num1} + {self.num2} = {val}")
#         elif self.sign == "-":
#             print(f"{self.num1} - {self.num2} = {val}")
#         elif self.sign == "*":
#             print(f"{self.num1} * {self.num2} = {val}")
#         elif self.sign == "/":
#             print(f"{self.num1} / {self.num2} = {val}")
# # Write your code here
# c1 = Calculator()
# print("==================")
# val = c1.calculate(10, 20, '+')
# print("Returned value:", val)
# c1.showCalculation()
# print("==================")
# val = c1.calculate(val, 10, '-')
# print("Returned value:", val)
# c1.showCalculation()
# print("==================")
# val = c1.calculate(val, 5, '*')
# print("Returned value:", val)
# c1.showCalculation()
# print("==================")
# val = c1.calculate(val, 16, '/')
# print("Returned value:", val)
# c1.showCalculation()


#################################  Task 7 ###########################################

# class Student:
#   def __init__(self, name, id, subject, grade):
#     self.name = name
#     self.id = id
#     self.subject = subject
#     self.grade = grade

#   def calculate_CGPA(self):
#     pass
#   def print_details(self):
#     res = 0
#     temp = -100000
#     for i in range(len(self.grade)):
#       res = res + self.grade[i]
#       if temp < i:
#         temp = i
#     result = round(res/(temp+1), 2)
#     self.gpa = result
#     print("Name:", self.name+",","ID:", self.id)
#     print("Department:", self.subject)
#     print("CGPA:",result)
#     if self.gpa > 3.80:
#       print("Your academic standing is Highest Distinction")
#     elif self.gpa > 3.65:
#       print("Your academic standing is High Distinction")
#     elif self.gpa > 3.50:
#       print("Your academic standing is Distinction")
#     elif self.gpa > 2:
#       print("Your academic standing is Satisfactory")
#     elif self.gpa < 2:
#       print("Sorry, you Can't Graduate")
# # Write your code here
# s1 = Student('Dora', '15995599','CSE', [4,3.7,3.7,4])
# s1.calculate_CGPA()
# print("==========================")
# s1.print_details()
# print("==========================")
# s2 = Student('Pingu', '12312322', 'EEE', [1.7,1.3,1.3,1.3,1])
# s2.calculate_CGPA()
# print("==========================")
# s2.print_details()
# print("==========================")
# s3 = Student('Bob', '13311331', 'CSE', [2,3,3,3.7,2.7,2.7])
# s3.calculate_CGPA()
# print("==========================")
# s3.print_details()



#####################################  Task 8  ###############################

# class Shinobi:
#     def __init__(self, name, rank):
#         self.name = name
#         self.rank = rank
#         self.salary = 0
#         self.mission = 0
#     def changeRank(self, rank):
#         self.rank = rank
#     def calSalary(self, mission):
#         self.mission = mission
#         if self.rank == "Genin":
#             self.salary = mission*50
#         elif self.rank == "Chunin":
#             self.salary = mission*100
#         else:
#             self.salary = mission*500

#     def printInfo(self):
#         print("Name:", self.name)
#         print("Rank:", self.rank)
#         print("Number of missions:", self.mission)
#         print("Salary:", self.salary)



# # Write your code here.
# naruto = Shinobi("Naruto", "Genin")
# naruto.calSalary(5)
# naruto.printInfo()
# print('====================')
# shikamaru = Shinobi('Shikamaru', "Genin")
# shikamaru.printInfo()
# shikamaru.changeRank("Chunin")
# shikamaru.calSalary(10)
# shikamaru.printInfo()
# print('====================')
# neiji = Shinobi("Neiji", "Jonin")
# neiji.calSalary(5)
# neiji.printInfo()


##################################  Task 9  ############################

# class Programmer:
#     def __init__(self, name, language, year):
#         self.name = name
#         self.language = language
#         self.year = year
#         self.temp = 0
#     def printDetails(self):
#         if self.temp == 0:
#             print("Horray! A new programmer is born")
#         print("Name:", self.name)
#         print("Language:", self.language)
#         print("Experience:", self.year, "years")
#     def addExp(self, year):
#         print("Updating experience of Jon Snow")
#         self.year += year
#         self.temp = 1

# # Write your code here.
# p1 = Programmer("Ethen Hunt", "Java", 10)
# p1.printDetails()
# print('--------------------------')
# p2 = Programmer("James Bond", "C++", 7)
# p2.printDetails()
# print('--------------------------')
# p3 = Programmer("Jon Snow", "Python", 4)
# p3.printDetails()
# p3.addExp(5)
# p3.printDetails() 


############################ Task 10 #################################

class UberEats:
    def __init__(self, name, number, place):
        self.name = name
        self.number = number
        self.place = place
        print(f"{self.name}, welcome to UberEats!")
        self.res = 0
        self.dict = {}
    
    def add_items(self, order1, order2, num1, num2):
        self.dict[order1] = num1
        self.dict[order2] = num2
        self.res = num1+num2
    def print_order_detail(self):
        print(f"User detail: Name: {self.name}, phone: {self.number}, Address: {self.place}")
        print("Orders:", self.dict)
        print("Total Paid Amount:", self.res)

# Write your code here
order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats ("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())


############################## Task 11   ##############################

# class Spotify:
#     def __init__(self, playlist):
#         self.playlist = playlist
#         print("Welcome to Spotify!")

#     def add_to_playlist(self, song_name):
#         self.playlist.append(song_name)
    
#     def playing_number(self, song_num):
#         if song_num <= len(self.playlist):
#             return f'playing {song_num} number song for you\nsong name: {self.playlist[song_num-1]}'
#         else:
#             return f'{song_num} number song not found\nYour playlist has {len(self.playlist)} songs only'


# user1 = Spotify(["See You Again", "Uptown Funk", "Hello"])
# print("=========================")
# print(user1.playing_number(4))
# user1.add_to_playlist("Dusk Till Dawn")
# print(user1.playing_number(3))
# print(user1.playing_number(4))


