class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def introduce(self):
        print(f"I'm {self.name}. A {self.type} pokemon")


class FirePokemon(Pokemon):
    def __init__(self, name, type, special_move):
        Pokemon.__init__(self, name, type)  # Call Pokemon directly
        self.special_move = special_move

    def introduce(self):
        super().introduce()
        print(f"My special move is {self.special_move}")

class GhostPokemon(Pokemon):
    def __init__(self, name, type, special_move):
        Pokemon.__init__(self, name, type)  # Call Pokemon directly
        self.special_move = special_move
    
    def introduce(self):
        super().introduce()
        print(f"My special move is {self.special_move} ghost")

class FireGhostPokemon(FirePokemon, GhostPokemon):
    def __init__(self, name, type, special_move):
        # Initialize both parent classes explicitly
        FirePokemon.__init__(self, name, type, special_move)
        GhostPokemon.__init__(self, name, type, special_move)

    def attack(self):
        print(f"attacking {self.special_move}")


pikachu = Pokemon("Pikachu", "electric")

pikachu.introduce()

charizard = FirePokemon("Charizard", "fire", "fire blast")

charizard.introduce()

gengar = FireGhostPokemon("Gengar", "ghost", "shadow claw")

gengar.introduce()

