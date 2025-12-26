import requests

def id_or_name(search):
    url_busca = f"https://pokeapi.co/api/v2/pokemon/{search}" #Link PokeAPI
    requested = requests.get(url_busca)
    if requested.status_code == 404:
        raise NameError ("Pokémon inexistente") #Finaliza caso não encontre nada

    data = requested.json()
    print(f"Pokémon: {data["name"]}")
    print(f"Type: {data["types"][0]["type"]["name"]}")
    print(f"Type: {data["types"][-1]["type"]["name"]}")

id_or_name("blastoise")