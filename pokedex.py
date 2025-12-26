

while True:
    print("Select: \n1- Search by name or ID")
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
        pass

    if e == 2: #Search specific hability
        pass

    if e == 3: #Search specific type
        pass

    if e == 4:
        print("Ending program...") #End
        break