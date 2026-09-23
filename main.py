handleliste = []

while True:
    print("\n1. Legg til vare")
    print("2. Se handleliste")
    print("3. Fjern vare")
    print("4. Avslutt")

    valg = input("Velg: ")

    if valg == "1":
        vare = input("Skriv inn vare: ")
        handleliste.append(vare)

    elif valg == "2":
        print("Handleliste:")
        for vare in handleliste:
            print("-", vare)

    elif valg == "3":
        vare = input("Hvilken vare vil du fjerne? ")
        if vare in handleliste:
            handleliste.remove(vare)
        else:
            print("Varen finnes ikke")

    elif valg == "4":
        break

    else:
        print("Ugyldig valg")