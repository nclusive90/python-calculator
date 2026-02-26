def addiere(a, b):
    return a + b


def subtrahiere(a, b):
    return a - b


def multipliziere(a, b):
    return a * b


def dividiere(a, b):
    if b == 0:
        raise ZeroDivisionError("Division durch Null ist nicht erlaubt.")
    return a / b


def lese_zahl(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ungueltige Eingabe. Bitte eine Zahl eingeben.")


def zeige_menu():
    print("\nTaschenrechner")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")


def main():
    zeige_menu()
    auswahl = input("Waehle eine Rechenart (1-4): ").strip()

    if auswahl not in {"1", "2", "3", "4"}:
        print("Ungueltige Auswahl.")
        return

    zahl1 = lese_zahl("Erste Zahl eingeben: ")
    zahl2 = lese_zahl("Zweite Zahl eingeben: ")

    try:
        if auswahl == "1":
            ergebnis = addiere(zahl1, zahl2)
            op = "+"
        elif auswahl == "2":
            ergebnis = subtrahiere(zahl1, zahl2)
            op = "-"
        elif auswahl == "3":
            ergebnis = multipliziere(zahl1, zahl2)
            op = "*"
        else:
            ergebnis = dividiere(zahl1, zahl2)
            op = "/"

        print(f"Ergebnis: {zahl1} {op} {zahl2} = {ergebnis}")
    except ZeroDivisionError as fehler:
        print(f"Fehler: {fehler}")


if __name__ == "__main__":
    main()
