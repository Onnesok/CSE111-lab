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




#############################################

class Student:
    def __init__(self) -> None:
        pass

# Write your code here

# Do not change the following lines of code.

s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()

