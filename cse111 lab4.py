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
# class Student:
#     def __init__(self, name, id, department = "CSE"):
#         self.name = name
#         self.id = id
#         self.department = department
#     def dailyEffort(self, effort):
#         self.effort = effort
#     def printDetails(self):
#         print(f"Name: {self.name}\nID: {self.id}\nDepartment: {self.department}\nDaily Effort: {self.effort} hours")
#         if self.effort <= 2:
#             print("Suggestion: Should give more effort!")
#         elif self.effort <= 4:
#             print("Suggestion: Keep up the good work!")
#         else:
#             print("Suggestion: Excellent! Now motivate others.")

# # Write your code here.
# harry = Student('Harry Potter', 123)
# harry.dailyEffort(3)
# harry.printDetails()
# print('========================')
# john = Student("John Wick", 456, "BBA")
# john.dailyEffort(2)
# john.printDetails()
# print('========================')
# naruto = Student("Naruto Uzumaki", 777, "Ninja")
# naruto.dailyEffort(6)
# naruto.printDetails()

###########################  Task 6  ############################
class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # def Patient(self, name, age):
    #     self.name = name
    #     self.age = age
    def add_Symptom(self, *sym):
        ls = []
        for i in sym:
            ls.append(i)
        self.sym = ls
    def printPatientDetail(self):
        print(f"Name: {self.name}\nAge: {self.age}")
        print("Symptoms:", end= " ")
        print(*self.sym, sep=", ")

# Write your code here.
p1 = Patient("Thomas", 23)
p1.add_Symptom("Headache")
p2 = Patient("Carol", 20)
p2.add_Symptom("Vomiting", "Coughing")
p3 = Patient("Mike", 25)
p3.add_Symptom("Fever", "Headache", "Coughing")
print("=========================")
p1.printPatientDetail()
print("=========================")
p2.printPatientDetail()
print("=========================")
p3.printPatientDetail()

###########################  Task 7 ##################################
# class Match:
#     def __init__(self, name):
#         print("5..4..3..2..1.. Play !!!")
#         ls = name.split("-")
#         self.bat = ls[0]
#         self.bowl = ls[1]
#         self.wicket = 0
#         self.run = 0
#         self.over = 0
#     def add_run(self, run):
#         self.run += run
#     def add_over(self, over = 0):
#         if over < 5:
#             self.over += over
#         elif over >= 5:
#             print(f"Warning! Cannot add {over} over/s (5 over match)")
#     def add_wicket(self, wicket = 0):
#         self.wicket = wicket
#     def print_scoreboard(self):
#         return f"Batting Team: {self.bat} \nBowling Team: {self.bowl} \nTotal Runs: {self.run} Wickets: {self.wicket} Overs: {self.over}"
# # Write your code here.
# match1 = Match("Rangpur Riders-Cumilla Victorians")
# print("=========================")
# match1.add_run(4)
# match1.add_run(6)
# match1.add_over(1)
# print(match1.print_scoreboard())
# print("=========================")
# match1.add_over(5)
# print("=========================")
# match1.add_wicket(1)
# print(match1.print_scoreboard())

######################### Task 8  #####################################
# class ParcelKoro:
#     def __init__(self, name = "No name set", weight = 0):
#         self.name = name
#         self.product_weight = weight
#     def calculateFee(self, location = None):
#         fee = 0
#         if location == None:
#             fee = 50
#         else:
#             fee = 100
#         if self.product_weight == 0:
#             total = 0
#         else:
#             total = (self.product_weight*20)+fee
#         self.total = total
#     def printDetails(self):
#         print("Customer Name:", self.name)
#         print("Product Weight:", self.product_weight)
#         print("Total fee:", self.total)

# # Write your code here.
# print("**********************")
# p1 = ParcelKoro()
# p1.calculateFee()
# p1.printDetails()
# print("**********************")
# p2 = ParcelKoro('Bob The Builder')
# p2.calculateFee()
# p2.printDetails()
# print("----------------------------")
# p2.product_weight = 15
# p2.calculateFee()
# p2.printDetails()
# print("**********************")
# p3 = ParcelKoro('Dora The Explorer', 10)
# p3.calculateFee('Dhanmondi')
# p3.printDetails()

#########################  Task 9  ############################
# class Batsman:
#     def __init__(self, *ls):
#         if type(ls[0]) is str:
#             self.name = ls[0]
#             self.run = ls[1]
#             self.ball = ls[2]
#         else:
#             self.name = "New Batsman"
#             self.run = ls[0]
#             self.ball = ls[1]

#     def printCareerStatistics(self):
#         print("Name:", self.name)
#         print("Runs Scored:", self.run, "Balls Faced:", self.ball)

#     def battingStrikeRate(self):
#         rate = (self.run / self.ball) * 100
#         return rate

#     def setName(self, name):
#         self.name = name

# # Write your code here
# b1 = Batsman(6101, 7380)
# b1.printCareerStatistics()
# print("============================")
# b2 = Batsman("Liton Das", 678, 773)
# b2.printCareerStatistics()
# print("----------------------------")
# print(b2.battingStrikeRate())
# print("============================")
# b1.setName("Shakib Al Hasan")
# b1.printCareerStatistics()
# print("----------------------------")
# print(b1.battingStrikeRate())

###########################  Task 10  ##############################
# class EPL_Team:
#     def __init__(self, team, song = "No slogan", title = 0):
#         self.team = team
#         self.song = song
#         self.title = title
#     def showClubInfo(self):
#         return (f"Name: {self.team} \nSong: {self.song} \nTotal No of title: {self.title}")
#     def increaseTitle(self):
#         self.title +=1
#     def changeSong(self, song):
#         self.song = song

# # Write your code here
# manu = EPL_Team('Manchester United', 'Glory Glory Man United')
# chelsea = EPL_Team('Chelsea')
# print('===================')
# print(manu.showClubInfo())
# print('##################')
# manu.increaseTitle()
# print(manu.showClubInfo())
# print('===================')
# print(chelsea.showClubInfo())
# chelsea.changeSong('Keep the blue flag flying high')
# print(chelsea.showClubInfo())

############################  Task 11  ##################################
# class Author:
#     def __init__(self, name = "Default", *books):
#         self.name = name
#         self.book = books
#     def addBooks(self, *books):
#         self.book = books
#     def changeName(self, name):
#         self.name = name
#     def printDetails(self):
#         print("Author Name:", self.name, "\nList of Books:")
#         for i in range(len(self.book)):
#             print(self.book[i])

# # Write your code here
# auth1 = Author('Humayun Ahmed')
# auth1.addBooks('Deyal', 'Megher Opor Bari')
# auth1.printDetails()
# print("===================")
# auth2 = Author()
# print(auth2.name)
# auth2.changeName('Mario Puzo')
# auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
# print("===================")
# auth2.printDetails()
# print("===================")
# auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
# auth3.printDetails()

############################### Task 12  ###############################
# class TaxiLagbe:
#     def __init__(self, number, area):
#         self.number = number
#         self.area = area
#         self.passenger = " "
#         self.taka = 0
#     def addPassenger(self, *passengers):
#         names = []
#         taka = 0
#         for i in range(len(passengers)):
#             temp = passengers[i].split("_")
#             if (len(self.passenger)+(i+1)) <= 4:
#                 print(f"Dear {temp[0]}! Welcome to TaxiLagbe")
#                 names.append(temp[0])
#                 taka += int(temp[1])
#             else:
#                 print("Taxi Full! No more passengers can be added")
#         self.taka += taka
#         if self.passenger == " ":
#             self.passenger = names
#         else:
#             self.passenger += names
    
#     def printDetails(self):
#         print("Trip info for Taxi number:", self.number)
#         print(f"This taxi can cover only {self.area} area")
#         print("Total passengers:", len(self.passenger), "\nPassenger lists:")
#         print(", ".join(self.passenger))
#         print("Total collected fare:", self.taka, "taka")

# # Write your code here
# # Do not change the following lines of code.
# taxi1 = TaxiLagbe('1010-01', 'Dhaka')
# print('-------------------------------')
# taxi1.addPassenger('Walker_100', 'Wood_200')
# taxi1.addPassenger('Matt_100')
# taxi1.addPassenger('Wilson_105')
# print('-------------------------------')
# taxi1.printDetails()
# print('-------------------------------')
# taxi1.addPassenger('Karen_200')
# print('-------------------------------')
# taxi1.printDetails()
# print('-------------------------------')
# taxi2 = TaxiLagbe('1010-02', 'Khulna')
# taxi2.addPassenger('Ronald_115')
# taxi2.addPassenger('Parker_215')
# print('-------------------------------')
# taxi2.printDetails()

######################### Task 13  #################################
# class Account:
#     def __init__(self, name = "default", taka = 0.0):
#         self.name = name
#         self.balance = taka

#     def details(self):
#         if self.name == "default":
#             print(self.balance)
#         else:
#             print(self.name)
#             print(self.balance)

# # Write your code here
# a1 = Account()
# print(a1.details())
# print("------------------------")
# a1.name = "Oliver"
# a1.balance = 10000.0
# print(a1.details())
# print("------------------------")
# a2 = Account("Liam")
# print(a2.details())
# print("------------------------")
# a3 = Account("Noah",400)
# print(a3.details())
# print("------------------------")
# a1.withdraw(6930)
# print("------------------------")
# a2.withdraw(600)
# print("------------------------")
# a1.withdraw(6929)
