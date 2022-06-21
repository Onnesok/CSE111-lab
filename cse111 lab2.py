########################  CSE11 LAB2  #############################
######################### Task 1  ################################

# class DataType:
#     def __init__(self, p_name, p_val):
#         self.name = p_name
#         self.value = p_val

# #Write your class code here
# data_type1 = DataType("Integer", 1234)
# print(data_type1.name)
# print(data_type1.value)
# print('=====================')
# data_type2 = DataType("String", "Hello")
# print(data_type2.name)
# print(data_type2.value)
# print('=====================')
# data_type3 = DataType("Float", 4.0)
# print(data_type3.name)
# print(data_type3.value)

########################  Task 2  ################################
# class Flower:
#     def __init__(self):
#         self.name = "Default name"
#         self.color = "Default color"
#         self.num_of_petal = 0

#     # def flower1(self, name, color, num_of_petal):
#     #     self.name = name
#     #     self.color = color
#     #     self.num_of_petal = num_of_petal

# #Write your class code here
# flower1 = Flower()
# flower1.name="Rose"
# flower1.color="Red"
# flower1.num_of_petal=6
# print("Name of this flower:", flower1.name)
# print("Color of this flower:",flower1.color)
# print("Number of petal:",flower1.num_of_petal)
# print("=====================")
# flower2 = Flower()
# flower2.name="Orchid"
# flower2.color="Purple"
# flower2.num_of_petal=4
# print("Name of this flower:",flower2.name)
# print("Color of this flower:",flower2.color)
# print ("Number of petal:",flower2. num_of_petal)
# #@@@@@@@@@@@@@@@@@@@@@@@@@@  sub task 2 and 3 @@@@@@@@@@@@@@@@@@@@@@@@@

# f1 = flower1
# f2 = flower2
# print(f1)
# print(f2)
# if f1 == f2:
#     print("they are same")
# else:
#     print("they are different")



#################### Task 3  ################################
# class Joker:
#     def __init__(self, name, power, is_he_psycho):
#         self.name = name
#         self.power = power
#         self.is_he_psycho = is_he_psycho

# #Write your class code here
# j1 = Joker('Heath Ledger', 'Mind Game', False)
# print(j1.name)
# print(j1.power)
# print(j1.is_he_psycho)
# print("=====================")
# j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
# print(j2.name)
# print(j2.power)
# print(j2.is_he_psycho)
# print("=====================")
# if j1 == j2:
#  print('same')
# else:
#  print('different')
# j2.name = 'Heath Ledger'
# if j1.name == j2.name:
#  print('same')
# else:
#  print('different')
# #Write your code for 2,3 here
# print("first if/else block prints different because it's memory address is different")
# print("second if/else block prints same because j1.name and j2.name is same")



########################  Task 4  #################################

# class Pokemon:
#     def __init__(self, pokemon1_name, pokemon2_name, pokemon1_power, pokemon2_power, damage_rate):
#         self.pokemon1_name = pokemon1_name
#         self.pokemon2_name = pokemon2_name
#         self.pokemon1_power = pokemon1_power
#         self.pokemon2_power = pokemon2_power
#         self.damage_rate = damage_rate


# #Write your code for class here
# team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
# print('=======Team 1=======')
# print('Pokemon 1:',team_pika.pokemon1_name,
# team_pika.pokemon1_power)
# print('Pokemon 2:',team_pika.pokemon2_name, 
# team_pika.pokemon2_power)
# pika_combined_power = (team_pika.pokemon1_power + 
# team_pika.pokemon2_power) * team_pika.damage_rate
# print('Combined Power:', pika_combined_power)
# #Write your code for subtask 2,3,4 here

# team_bulb = Pokemon("bulbasaur", "squirtle", 80, 70, 9)
# print('=======Team 2=======')
# print('Pokemon 1:',team_bulb.pokemon1_name,
# team_bulb.pokemon1_power)
# print('Pokemon 2:',team_bulb.pokemon2_name, 
# team_bulb.pokemon2_power)
# bulb_combined_power = (team_bulb.pokemon1_power + 
# team_bulb.pokemon2_power) * team_bulb.damage_rate
# print('Combined Power:', bulb_combined_power)


############################# Task 5 #########################

# class Player:
#     def __init__(self):
#         self.name = "Default name"
#         self.jersy_number = "Default number"
#         self.position = 0

# # Write Your Class Code Here
# player1 = Player()
# player1.name = "Ronaldo"
# player1.jersy_number = 9
# player1.position = "Striker"
# print("Name of the Player:", player1.name)
# print("Jersey Number of player:", player1.jersy_number)
# print("Position of player:", player1.position)
# print("===========================")
# player2 = Player()
# player2.name = "Neuer"
# player2.jersy_number = 1
# player2.position = "Goal Keeper"
# print("Name of the player:", player2.name)
# print("Jersey Number of player:", player2.jersy_number)
# print("Position of player:", player2.position)

#######################  Task 6 #############################

# class Country:
#     def __init__(self):
#         self.name = "Bangladesh"
#         self.continent = "Asia"
#         self.capital = "Dhaka"
#         self.fifa_ranking = 187

    
# # Write your Class Code here
# country = Country()
# print('Name:',country.name)
# print('Continent:',country.continent)
# print('Capital:',country.capital)
# print('Fifa Ranking:',country.fifa_ranking)
# print('===================')
# country.name = "Belgium"
# country.continent = "Europe"
# country.capital = "Brussels"
# country.fifa_ranking = 1
# print('Name:',country.name)
# print('Continent:',country.continent)
# print('Capital:',country.capital)
# print('Fifa Ranking:',country.fifa_ranking)


#######################  Task 7  ###########################

# class DemonSlayer:
#     def __init__(self, name, style, number_of_technique, kill):
#         self.name = name
#         self.style = style
#         self.number_of_technique = number_of_technique
#         self.kill = kill
        
        
# # Write your Class Code here
# tanjiro = DemonSlayer("Tanjiro", "Water Breathing", 10, 10)
# print('Name:',tanjiro.name)
# print('Fighting Style:',tanjiro.style)
# print(f'Knows {tanjiro.number_of_technique} technique(s) and has killed {tanjiro.kill} demon(s)')
# print('===================')
# zenitsu = DemonSlayer("Zenitsu", "Thunder Breathing", 1, 4)
# print('Name:',zenitsu.name)
# print('Fighting Style:',zenitsu.style)
# print(f'Knows {zenitsu.number_of_technique} technique(s) and has killed {zenitsu.kill} demon(s)')
# print('===================')
# inosuke = DemonSlayer("Inosuke", "Beast Breathing", 5, 7)
# print('Name:',inosuke.name)
# print('Fighting Style:',inosuke.style)
# print(f'Knows {inosuke.number_of_technique} technique(s) and has killed {inosuke.kill} demon(s)')
# print('===================')
# print(f'{tanjiro.name}, {zenitsu.name}, {inosuke.name} knows total {tanjiro.number_of_technique + zenitsu.number_of_technique + inosuke.number_of_technique} techniques')
# print(f'They have killed total {tanjiro.kill + zenitsu.kill + inosuke.kill} demons')

############################ Task 8  ############################

# class box:
#     def __init__(self, list):
#         height, width, breadth = list
#         print("Creating a Box!")
#         self.height = height
#         self.width = width
#         self.breadth = breadth
#         print(f"Volume of the box is {height * width * breadth} cubit units")

# #Write your class code here
# print("Box 1")
# b1 = box([10,10,10])
# print("=========================")
# print("Height:", b1.height)
# print("Width:", b1.width)
# print("Breadth:", b1.breadth)
# print("-------------------------")
# print("Box 2")
# b2 = box((30,10,10))
# print("=========================")
# print("Height:", b2.height)
# print("Width:", b2.width)
# print("Breadth:", b2.breadth)
# b2.height = 300
# print("Updating Box 2!")
# print("Height:", b2.height)
# print("Width:", b2.width)
# print("Breadth:", b2.breadth)
# print("-------------------------")
# print("Box 3")
# b3 = b2
# print("Height:", b3.height)
# print("Width:", b3.width)
# print("Breadth:", b3.breadth)

######################### Task 9  ##########################

# class buttons:
#     def __init__(self, word, spaces, border):
#         self.word = word
#         self.spaces = spaces
#         self.border = border

#         temp = (len(self.border)*2) + (len(self.word)) + (2*self.spaces)
#         print(f"{self.word} Button Specifications:")
#         print("Button name:", self.word)
#         print("Number of the border characters for the top and the bottom:", temp)
#         print("Number of spaces between the left side border and the first character of the button name:", self.spaces)
#         print("Number of spaces between the right side border and the last character of the button name:", self.spaces)
#         print("Characters representing the borders:", self.border)
#         print(temp*self.border)
#         print(self.border+self.spaces*"#"+self.word+self.spaces*"#"+self.border)
#         print(temp*self.border)
# #Write your class code here
# word = "CANCEL"
# spaces = 10
# border = 'x'
# b1 = buttons(word, spaces, border)
# print("=======================================================")
# b2 = buttons("Notify",3, '!')
# print("=======================================================")
# b3 = buttons('SAVE PROGRESS', 5, '$')

##########################  Task 10   ###########################

# class Wadiya():
#     def __init__(self):
#         self.name = 'Aladeen'
#         self.designation = 'President Prime Minister Admiral General'
#         self.num_of_wife = 100
#         self.dictator = True

# wadiya = Wadiya()
# print("Part 1:")
# print("Name of President:", wadiya.name)
# print("Designation:", wadiya.designation)
# print("Number of wife:", wadiya.num_of_wife)
# print("Is he/she a dictator:", wadiya.dictator)
# print("Part 2:")
# wadiya.name = "Donald Trump"
# wadiya.designation = "President"
# wadiya.num_of_wife = 1
# wadiya.dictator = "False"
# print("Name of President:", wadiya.name)
# print("Designation:", wadiya.designation)
# print("Number of wife:", wadiya.num_of_wife)
# print("Is he/she a dictator:", wadiya.dictator)

# print("previous information lost")