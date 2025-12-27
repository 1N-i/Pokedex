import requests

def search_ability(search):
    search = search_message = search.lower()
    search = search.replace(" ", "-")
    url_search = f"https://pokeapi.co/api/v2/ability/{search}"
    requested = requests.get(url_search)
    if requested.status_code == 404:
        print(f"Error: '{search_message}' not found") #Finish if nothing was found
        return
    
    data = requested.json()

    for ability in data["effect_entries"]:
        if ability["language"]["name"] == "en":
            print(f"\nEffect: \n{ability["effect"].replace("\n\n", "\n")}")
            print(f"\nShort version: \n{ability["short_effect"].replace("\n\n", "\n")}")

    while True: #Make data verification
        print("\nSelect: \n1- See Pokémon with this ability \n2- End search")
        a = int(input("Action: "))

        if a == 1:
            print(f"\nPokémon with '{search_message}' naturally:")
            for pokemon in data["pokemon"]:
                if pokemon["is_hidden"] == False:
                    print(f"{pokemon["pokemon"]["name"]}")
                
            print(f"\nPokémon with '{search_message}' as a hidden ability:")
            for pokemon in data["pokemon"]:
                if pokemon["is_hidden"] == True:
                    print(f"{pokemon["pokemon"]["name"]}")

        if a == 2: #End search
            print(f"Ending search on '{search_message}'")
            break