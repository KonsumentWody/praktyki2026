import math  # Importujemy moduł matematyczny, żeby mieć dostęp do pierwiastkowania


def oblicz_pierwiastek():
    """Funkcja obliczająca pierwiastek z obsługą błędów."""
    try:
        # Pobieramy liczbę od użytkownika
        liczba = float(input("Podaj liczbę do pierwiastkowania: "))

        # Sprawdzamy błąd logiczny: nie pierwiastkujemy liczb ujemnych (w zbiorze liczb rzeczywistych)
        if liczba < 0:
            return "Błąd: Nie można pierwiastkować liczby ujemnej!"

        wynik = math.sqrt(liczba)
        return f"Pierwiastek z {liczba} wynosi: {wynik:.2f}"

    except ValueError:
        # Obsługa błędu, gdy użytkownik wpisze np. tekst zamiast liczby
        return "Błąd: Musisz podać poprawną liczbę (użyj kropki zamiast przecinka)!"


def pokaz_menu():
    print("\n--- TWÓJ KALKULATOR AI ---")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Pierwiastkowanie")
    print("0. Wyjście")
    print("--------------------------")


# GŁÓWNA PĘTLA PROGRAMU
while True:
    pokaz_menu()
    wybor = input("Wybierz opcję (0-5): ")

    if wybor == "0":
        print("Dzięki za skorzystanie z kalkulatora! Do zobaczenia.")
        break  # Przerywa pętlę i kończy program

    if wybor == "5":
        print(oblicz_pierwiastek())
        continue  # Wracamy na początek pętli

    # Dla opcji 1-4 potrzebujemy dwóch liczb
    if wybor in ("1", "2", "3", "4"):
        try:
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))

            if wybor == "1":
                print(f"Wynik: {a + b}")
            elif wybor == "2":
                print(f"Wynik: {a - b}")
            elif wybor == "3":
                print(f"Wynik: {a * b}")
            elif wybor == "4":
                if b == 0:
                    print("Błąd: Nie dzielimy przez zero!")
                else:
                    print(f"Wynik: {a / b}")
        except ValueError:
            print("Błąd: To nie jest poprawna liczba!")
    else:
        if wybor != "5":  # Jeśli użytkownik wpisał np. "9"
            print("Nieprawidłowy wybór. Spróbuj ponownie.")