# PESEL-tools
# by Piotr Kołaczek, v0.0.1

Program testuje numer PESEL i zwraca informacje o wykrytych błędach:
- ciąg na wejściu zawiera inne znaki, niż cyfry
- ciąg na wejściu ma długość inną, niż 11 znaków,
- ciąg na wejściu zawiera same zera (nie ma to sensu, ale daje poprawną sumę kontrolną)
- dzień ma numer większy, niż przypisany do danego miesiąca (z uwzględnieniem lat przestępnych)
- numer miesiąca jest zbyt duży
- błędna suma kontrolna

Program dekoduje i wyświetla: datę urodzenia, numer seryjny obywatela, płeć, obliczoną sumę kontrolną.
