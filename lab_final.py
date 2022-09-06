
class Pokemon:
    def __init__(self,name,hp,characterType):
      self.__name = name
      self.__hp = hp
      self.__characterType = characterType
 
    def getHp(self):
      return self.__hp
  
    def getMoves(self):
      return "\nBasic move :" + "Quick Attack"
 
    def __str__(self):
      return "Name: " + self.__name + "\nHit points: " + str(self.__hp) + "\nCharacter Type: " + self.__characterType
 


class ElitePokemon(Pokemon):

    numberOfElitePokemon = 0

    def __init__(self, name, hp, characterType, weakness, moves):
        super().__init__(name, hp, characterType)
        self.weakness = weakness
        self.moves = moves
        ElitePokemon.numberOfElitePokemon += 1

    @staticmethod
    def createPokemon(name, moves):
        print("Unknown elite polemon detected")
        return ElitePokemon(name, 500, "unknown", "unknown", moves)
    def __add__(self, other):
        moves = [self.moves[1], other.moves[1]]
        hybrid = ElitePokemon("Unknown", self.getHp() + other.getHp(), "hybrid", "unknown", moves)
        return hybrid

    def getMoves(self):
        strg = super().getMoves()[1:]
        num = len(self.moves)
        if num > 0:
            strg += f"\nQuick: {self.moves[0]}"
            return strg
        else:
            strg += f"\nMain move: {self.moves[0]}"
            return strg

#Driver Code  
Corphish = ElitePokemon.createPokemon('Corphish',['Bubble beam'])
print('Number of elite Pokemon',ElitePokemon.numberOfElitePokemon )
print(Corphish)
print(Corphish.getMoves())
print('*****************')
Pikachu = ElitePokemon('Pikachu',150,'Electric','Water',['Thunder shock','Thunderbolt'])
print(Pikachu)
print('*****************')
Mewtwo = ElitePokemon('Mewtwo',180,'Psychic','Electric',['Psycho Cut','Ice Beam'])
print(Mewtwo)
print(Mewtwo.getMoves())
print('*****************')
Charizard = ElitePokemon('Charizard',110,'Fire','Rock',['Fire Spin','Overheat'])
print(Charizard)
print(Charizard.getMoves())
print('*****************')
Hybrid = Mewtwo + Charizard
print(Hybrid)
print(Hybrid.getMoves())
print('Number of elite Pokemon: ',ElitePokemon.numberOfElitePokemon )















# class PokemonBasic:
#     def __init__(self, name="Default", hp=0, weakness="None", type="Unknown"):
#         self.name = name
#         self.hit_point = hp
#         self.weakness = weakness
#         self.type = type

#     def get_type(self):
#         return "Main type: " + self.type

#     def get_move(self):
#         return "Basic move: " + "Quick Attack"

#     def __str__(self):
#         return (
#             "Name: "
#             + self.name
#             + ", HP: "
#             + str(self.hit_point)
#             + ", Weakness: "
#             + self.weakness
#         )


# class PokemonExtra(PokemonBasic):
#     def __init__(
#         self,
#         name="Defalut",
#         hp=0,
#         weakness=None,
#         type=None,
#         secondary=None,
#         *extra_moves,
#     ):
#         super().__init__(name, hp, weakness, type)
#         self.secondary = secondary
#         self.extra_moves = extra_moves

#         self.move_lst = list(self.extra_moves)
#         self.var1 = []
#         self.var2 = ""
#         for i in self.extra_moves:
#             self.var1 = list(i)
#         self.var2 += ", ".join(self.var1)

#     def get_type(self):
#         if self.secondary == None:
#             return f"Main type: {self.type}"
#         else:
#             return f"Main type: {self.type} Secondary type: {self.secondary}"

#     def get_move(self):
#         if len(self.extra_moves) == 0:
#             return "Basic move: Quick Attack"
#         else:
#             return f"Basic move: Quick Attack\nOther moves: {str(self.var2)}"


# print("\n------------Basic Info:--------------")
# pk = PokemonBasic()
# print(pk)
# print(pk.get_type())
# print(pk.get_move())
# print("\n------------Pokemon 1 Info:-------------")
# charmander = PokemonExtra("Charmander", 39, "Water", "Fire")
# print(charmander)
# print(charmander.get_type())
# print(charmander.get_move())
# print("\n------------Pokemon 2 Info:-------------")
# charizard = PokemonExtra(
#     "Charizard", 78, "Water", "Fire", "Flying", ("Fire Spin", "Fire Blaze")
# )
# print(charizard)
# print(charizard.get_type())
# print(charizard.get_move())