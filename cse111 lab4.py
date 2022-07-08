##########################  Task 3  ############################
class Cat:
    def __init__(self, name = "White", work = "sitting"):
        self.name = name
        self.work = work
        print(self.name, "cat is", self.work)
    def printCat(self):
        pass
    def changeColor(self, color):
        self.name = color
        self.work = "sitting"
        print(self.name, "cat is", self.work)
        self.work = "jumping"
 #Write your code here 
c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()


