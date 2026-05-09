import json
import os


def wczytaj_oceny(nazwa_pliku="oceny.json"):
    """Odczytuje dane z JSON. Jeśli plik nie istnieje, zwraca pustą listę."""
    if not os.path.exists(nazwa_pliku):
        return []
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def zapisz_oceny(dane, nazwa_pliku="oceny.json"):
    """Zapisuje listę słowników do pliku JSON w czytelnym formacie."""
    with open(nazwa_pliku, "w", encoding="utf-8") as f:
        json.dump(dane, f, indent=4, ensure_ascii=False)


def pokaz_ranking(lista):
    """Sortuje uczniów od najlepszej oceny do najgorszej i wyświetla listę."""
    if not lista:
        print("Brak danych do stworzenia rankingu!")
        return

    # Kluczowa poprawka AI: Sortowanie z użyciem funkcji lambda
    # reverse=True sprawia, że najwyższe oceny są na górze
    ranking = sorted(lista, key=lambda x: x['ocena'], reverse=True)

    print("\n--- 🏆 AKTUALNY RANKING ---")
    for i, uczen in enumerate(ranking, 1):
        # Formatowanie wyrównuje kolumny (np. :<10)
        print(f"{i}. {uczen['imie']:<10} | Ocena: {uczen['ocena']}")


# --- PRZYKŁAD UŻYCIA ---
if __name__ == "__main__":
    # Przykładowe dane wejściowe
    uczniowie = [
        {"imie": "Marek", "ocena": 4},
        {"imie": "Zuzia", "ocena": 6},
        {"imie": "Kacper", "ocena": 3},
        {"imie": "Ola", "ocena": 5}
    ]

    # Zapisujemy, odczytujemy i wyświetlamy
    zapisz_oceny(uczniowie)
    dane_z_pliku = wczytaj_oceny()
    pokaz_ranking(dane_z_pliku)
