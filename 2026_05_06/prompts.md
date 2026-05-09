| Poziom | Treść Promptu | Wynik AI |
| :--- | :--- | :--- |
| **Słaby** | "zrób średnią ocen python" | Podaje jedną linijkę kodu. Często brak obsługi pustej listy (błąd dzielenia przez zero). |
| **Średni** | "Napisz funkcję w Pythonie, która przyjmuje listę liczb i zwraca średnią. Wyjaśnij jak działa." | Kod jest poprawny, ale komentarze są techniczne i trudne dla początkującego. |
| **Mistrzowski** | "Działaj jako nauczyciel liceum. Napisz funkcję liczącą średnią ocen z listy. Użyj Chain of Thought: najpierw wyjaśnij matematyczny wzór, potem napisz kod z obsługą błędu dla pustej listy, a na końcu skomentuj każdą linię jak dla 16-latka." | AI tłumaczy logikę, zabezpiecza kod przed błędami i uczy programistycznego myślenia. |

### Wnioski z eksperymentu
1. **Precyzja roli:** Nadanie AI roli (np. nauczyciela) drastycznie zmienia język odpowiedzi na bardziej zrozumiały.
2. **Chain of Thought:** Zmuszenie AI do wyjaśnienia logiki przed podaniem kodu sprawia, że rzadziej generuje ona "halucynacje" i błędy.
3. **Specyfikacja błędów:** W dobrym prompcie warto od razu zasugerować brzegowe przypadki (np. "co jeśli lista jest pusta?").