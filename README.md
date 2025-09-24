# 🎲 Spel 21

En förenklad textbaserad version av Blackjack där du möter datorn.
Målet är att komma så nära 21 poäng som möjligt utan att gå över.

## 📖 Spelbeskrivning

* Spelaren slår tärningen (1–6) tills hen väljer att stanna eller går över 21.

* Om spelaren får över 21 förlorar hen direkt.

* Dealern (datorn) slår automatiskt tills den når minst 17 poäng.

* Vinnaren är den som är närmast 21 utan att gå över.

* Vid lika poäng blir det oavgjort.

* Spelet håller även koll på highscore (antal vinster för spelare och dealer) genom att spara i en fil highscore.json.

## 📦 Installation

* Klona repot eller ladda ner koden:

    git clone https://github.com/emre89/SPEL_21.git

* Installera beroenden:

    pip install -r requirements.txt


📌 Enda externa paketet som krävs är pytest (för tester). Själva spelet använder bara standardbiblioteket.

## ▶️ Köra spelet

Från projektets rotmapp kör du:

    python -m game.game


⚠️ Viktigt: Kör alltid med -m, annars hittar Python inte paketet game.

## 🧪 Köra tester

Vi använder pytest för tester.
Från projektets rotmapp:

    pytest

Det kör alla tester i mappen tests/.

## 🏆 Highscore

Efter varje spelomgång uppdateras ställningen:

    Ställning: Spelare 2 - Dealer 1

Resultatet sparas i highscore.json och laddas automatiskt in nästa gång spelet startas.

## 📷 Exempel på körning
🎲 Välkommen till Tärningsspelet 21! 🎲

Vill du [r]ulla eller [s]tanna? r
Du slog 5, total: 5
Vill du [r]ulla eller [s]tanna? r
Du slog 6, total: 11
Vill du [r]ulla eller [s]tanna? s
Du stannade på 11
Dealern slog [6, 5, 4, 3], total: 18
Dealern vinner.
Ställning: Spelare 0 - Dealer 1
Vill du spela igen? (j/n): n
Spelet avslutas. Tack för att du spelade!
