import random


def pokaz_statystyki(historia_prob):
    """
    Funkcja generująca podsumowanie gry.
    Argument 'historia_prob' to lista zawierająca liczbę strzałów z każdej partii.
    """
    if not historia_prob:
        print("Brak danych do wyświetlenia statystyk.")
        return

    liczba_gier = len(historia_prob)
    suma_prob = sum(historia_prob)
    srednia = suma_prob / liczba_gier
    najlepszy_wynik = min(historia_prob)  # Im mniej prób, tym lepiej!

    print("\n--- 📊 TWOJE STATYSTYKI ---")
    print(f"Rozegrane partie: {liczba_gier}")
    print(f"Łączna liczba strzałów: {suma_prob}")
    print(f"Średnia liczba prób na grę: {srednia:.2f}")
    print(f"Twój rekord (najmniej prób): {najlepszy_wynik}")
    print("---------------------------\n")


def gra():
    historia = []
    print("Witaj w grze! Pomyślałem liczbę od 1 do 100.")

    while True:
        tajna_liczba = random.randint(1, 100)
        proby = 0
        zgadnieta = False

        print("\nNowa runda! Zgadnij co to za liczba.")

        while not zgadnieta:
            try:
                strzal = int(input("Twój typ: "))
                proby += 1

                if strzal < tajna_liczba:
                    print("Za mało! Spróbuj wyżej.")
                elif strzal > tajna_liczba:
                    print("Za dużo! Celuj niżej.")
                else:
                    print(f"🎯 BRAWO! Odgadłeś za {proby}. razem.")
                    historia.append(proby)
                    zgadnieta = True
            except ValueError:
                print("Hej, to nie jest liczba! Tracisz próbę przez nieuwagę. 😉")

        jeszcze_raz = input("Chcesz zagrać kolejną rundę? (t/n): ").lower()
        if jeszcze_raz != 't':
            break

    pokaz_statystyki(historia)
    print("Dzięki za grę!")


# Start gry
if __name__ == "__main__":
    gra()