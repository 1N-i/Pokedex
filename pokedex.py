from pokemon import id_or_name
from ability import search_ability
from type import search_type

while True:
    print("\nSelect: \n1- Search by name or ID")
    print("2- Search hability \n3- Search by type \n4- Finish Program \n")
    options = [1, 2, 3, 4]

    try:
        e = int(input("Action: "))
        if e not in options:
            raise ValueError

    except ValueError:
        print("\nInvalid action\n")
        continue

    if e == 1: #Search Pokémon by name or ID
        search1 = input("Name or ID: ")
        id_or_name(search1)

    if e == 2: #Search specific ability
        search2 = input("Ability name: ")
        search_ability(search2)

    if e == 3: #Search specific type
        search3 = input("Type: ")
        search_type(search3)

    if e == 4:
        print("Ending program...") #End
        break