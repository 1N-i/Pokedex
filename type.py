import requests

def search_type(search):
    search = search_message = search.lower()
    url_search = f"https://pokeapi.co/api/v2/type/{search}"
    requested = requests.get(url_search)
    if requested.status_code == 404:
        print(f"Error: '{search_message}' not found") #Finish if nothing was found
        return
    
    data = requested.json()

    while True: #Make data verification
        print(f"\nSelect: \n1- See {search_message} type pokémon \n2- See {search_message} type moves")
        print(f"3- See {search_message} type chart \n4- End search")
        a = int(input("Action: "))

        if a == 1: #See pokémon
            print(f"\n{search_message} type pokémon:")
            for pokemon in data["pokemon"]:
                print(pokemon["pokemon"]["name"])

        if a == 2: #See types
            pass

        if a == 3: #See type chart
            pass

        if a == 4: #End search
            print(f"Ending search on '{search_message}'")
            break

#search_type("ghosT")