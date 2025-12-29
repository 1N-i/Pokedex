import requests

def create_data(search_type, search): #Sends data to the functions that called it
    url_search = f"https://pokeapi.co/api/v2/{search_type}/{search}" #Link PokeAPI
    requested = requests.get(url_search)
    if requested.status_code == 404:
        print(f"Error: '{search}' not found") #Finish if nothing was found
        return "error"
    return requested.json()

#-------------------------------------------------------------
def data_verification(options): #Data verification
    while True:
        try:
            action = int(input("Action: "))
            if action not in options:
                raise ValueError
            return action

        except ValueError:
            print("Invalid action\n")

#-------------------------------------------------------------
def search_id_or_name(search): #Search Pokémon by name or ID
    data = create_data("pokemon", search)
    if data == "error":
        return

    print(f"\nID: {data["id"]}") #ID
    print(f"Pokémon: {data["name"]}") #Name

    type1 = data["types"][0]["type"]["name"]
    type2 = data["types"][-1]["type"]["name"]

    if type1 == type2: #Mono-type
        print(f"Type: {type1}")

    else: #Dual-type
        print(f"Type: {type1}")
        print(f"Type: {type2}")

    while True:
        print("\nSelect: \n1- See moves \n2- See abilities \n3- End search")
        action = data_verification([1, 2, 3])

        if action == 1: #Show moves
            print(f"\nMoves that {data["name"]} can learn:")
            for attack in data["moves"]:
                print(attack["move"]["name"])

        if action == 2: #Show hability
            print(f"\nAbilities that {data["name"]} can have:")
            for ability in data["abilities"]:
                print(ability["ability"]["name"])

        if action == 3: #End search
            print(f"\nEnding search on '{data["name"]}'")
            break

#-------------------------------------------------------------
def search_type(search): #Search specific type
    search = search_message = search.lower()
    data = create_data("type", search)
    if data == "error":
        return

    while True:
        print(f"\nSelect: \n1- See {search_message} type pokémon \n2- See {search_message} type moves")
        print(f"3- See {search_message} type chart \n4- End search")
        action = data_verification([1, 2, 3, 4])

        if action == 1: #See pokémon
            print(f"\n{search_message} type pokémon:")
            for pokemon in data["pokemon"]:
                print(pokemon["pokemon"]["name"])

        if action == 2: #See types
            pass

        if action == 3: #See type chart
            pass

        if action == 4: #End search
            print(f"Ending search on '{search_message}'")
            break

#-------------------------------------------------------------
def search_move(search): #Search a move
    data = create_data("move", search)
    if data == "error":
        return
    
    #To Do

#-------------------------------------------------------------
def search_ability(search):  #Search ability
    search = search_message = search.lower()
    search = search.replace(" ", "-")

    data = create_data("ability", search)
    if data == "error":
        return

    for ability in data["effect_entries"]:
        if ability["language"]["name"] == "en":
            print(f"\nEffect: \n{ability["effect"].replace("\n\n", "\n")}")
            print(f"\nShort version: \n{ability["short_effect"].replace("\n\n", "\n")}")

    while True:
        print("\nSelect: \n1- See Pokémon with this ability \n2- End search")
        action = data_verification([1, 2])

        if action == 1:
            print(f"\nPokémon with '{search_message}' naturally:")
            for pokemon in data["pokemon"]:
                if pokemon["is_hidden"] == False:
                    print(f"{pokemon["pokemon"]["name"]}")
                
            print(f"\nPokémon with '{search_message}' as a hidden ability:")
            for pokemon in data["pokemon"]:
                if pokemon["is_hidden"] == True:
                    print(f"{pokemon["pokemon"]["name"]}")

        if action == 2: #End search
            print(f"Ending search on '{search_message}'")
            break