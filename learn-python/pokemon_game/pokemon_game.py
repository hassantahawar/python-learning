from pokemons import player_pokemons, computer_pokemons
from random import choice
from sys import exit

# both players will choose a pokemon, status will be false if pokemon dies
# when dead, replace with next one. player loses if all pokemon dead


def hit_moves(available_moves, current_pokemon, current_computer_pokemon):
    choose_hit_move = input("Hit Move: ")
    hit_move = next(
        (
            move
            for move in available_moves
            if move["name"].lower() == choose_hit_move.lower() and move["pp"] > 0
        ),
        None,
    )
    available_computer_moves = current_computer_pokemon["moves"]
    hit_computer_move = choice(available_computer_moves)
    if hit_move is None:
        hit_moves(available_moves, current_pokemon, current_computer_pokemon)
    else:
        print(f"{current_pokemon["name"]} used {hit_move["name"]}")
        print(f"{current_computer_pokemon["name"]} used {hit_computer_move["name"]}")
        if current_computer_pokemon["hp"] > 4 and current_pokemon["hp"] > 4:
            if current_pokemon["lvl"] > current_computer_pokemon["lvl"]:
                current_computer_pokemon["hp"] -= hit_move["damage"]
                if current_computer_pokemon["hp"] <= 0:
                    current_computer_pokemon["status"] = False
                    print(f"{current_computer_pokemon["name"]} fainted.")
                    battle()
                current_pokemon["hp"] -= hit_computer_move["damage"]
                if current_pokemon["hp"] <= 0:
                    current_pokemon["status"] = False
                    print(f"{current_pokemon["name"]} fainted.")
                    battle()
            else:
                current_pokemon["hp"] -= hit_computer_move["damage"]
                if current_pokemon["hp"] <= 0:
                    current_pokemon["status"] = False
                    print(f"{current_pokemon["name"]} fainted.")
                    battle()
                current_computer_pokemon["hp"] -= hit_move["damage"]
                if current_computer_pokemon["hp"] <= 0:
                    current_computer_pokemon["status"] = False
                    print(f"{current_computer_pokemon["name"]} fainted.")
                    battle()
            print(f"opponent Pokemon: {current_computer_pokemon}")
            print(f"your Pokemon: {current_pokemon}")
            print(f"Your Available Moves {available_moves}")
        elif current_computer_pokemon["hp"] <= 0:
            current_computer_pokemon["status"] = False
            print(f"{current_computer_pokemon["name"]} fainted.")
            battle()
        elif current_pokemon["hp"] <= 0:
            current_pokemon["status"] = False
            print(f"{current_pokemon["name"]} fainted.")
            battle()
        else:
            return


def battle():
    print("POKEMON GAME".center(25, "#"))
    available_player_pokemon = [
        pokemon for pokemon in player_pokemons if pokemon["hp"] > 0
    ]
    available_computer_pokemon = [
        pokemon for pokemon in computer_pokemons if pokemon["hp"] > 0
    ]
    if len(available_computer_pokemon) == 0:
        exit("player won!")
    elif len(available_player_pokemon) == 0:
        exit("player won!")
    print("Your Pokemons")
    for pokemon in available_player_pokemon:
        print(pokemon["name"].ljust(18, ".") + str(pokemon["hp"]).rjust(5) + "HP")
    choose_pokemon = input(f"Choose your pokemon:")
    current_pokemon = next(
        (
            pokemon
            for pokemon in available_player_pokemon
            if pokemon["name"].lower() == choose_pokemon.lower()
            and pokemon["status"] is True
        ),
        None,
    )
    if current_pokemon is None:
        return battle()
    print(
        f"You Chose: {current_pokemon["name"].ljust(18, ".")} {str(current_pokemon["hp"]).rjust(5)}HP"
    )
    current_computer_pokemon = choice(available_computer_pokemon)
    print(
        f"Computer chose: {current_computer_pokemon["name"].ljust(16, ".")} {str(current_computer_pokemon["hp"]).rjust(5)}HP"
    )
    all_moves = current_pokemon["moves"]
    available_moves = [moves for moves in all_moves if moves["pp"] > 0]
    print(available_moves)
    while (
        current_computer_pokemon["status"] is True and current_pokemon["status"] is True
    ):
        hit_moves(available_moves, current_pokemon, current_computer_pokemon)


battle()
