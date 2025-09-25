import json
import os
from player import Player
from dealer import Dealer

HIGHSCORE_FILE = "highscore.json"

class Game:
    def __init__(self):
        self.player = Player("Spelare")
        self.dealer = Dealer()
        self.highscore = {"player": 0, "dealer": 0}
        self.load_highscore()

    def load_highscore(self):
        if os.path.exists(HIGHSCORE_FILE):
            with open(HIGHSCORE_FILE, "r") as f:
                self.highscore = json.load(f)

    def save_highscore(self):
        with open(HIGHSCORE_FILE, "w") as f:
            json.dump(self.highscore, f)

    def play(self):
        print("🎲 Välkommen till Tärningsspelet 21! 🎲\n")
        while True:
            self.player.reset()
            self.dealer.reset()

            # Player turn
            while True:
                choice = input("Vill du [r]ulla eller [s]tanna? ").lower()
                if choice == "r":
                    value = self.player.roll()
                    print(f"Du slog {value}, total: {self.player.total}")
                    if self.player.total > 21:
                        print("Du fick över 21! Dealern vinner.")
                        self.highscore["dealer"] += 1
                        break
                elif choice == "s":
                    print(f"Du stannade på {self.player.total}")
                    break
                else:
                    print("Ogiltigt val, försök igen.")

            # Dealer turn
            if self.player.total <= 21:
                rolls = self.dealer.play()
                print(f"Dealern slog {rolls}, total: {self.dealer.total}")

                if self.dealer.total > 21:
                    print("Dealern fick över 21! Du vinner 🎉")
                    self.highscore["player"] += 1
                else:
                    if self.dealer.total > self.player.total:
                        print("Dealern vinner.")
                        self.highscore["dealer"] += 1
                    elif self.dealer.total < self.player.total:
                        print("Du vinner 🎉")
                        self.highscore["player"] += 1
                    else:
                        print("Oavgjort!")

            # Show score
            print(f"Ställning: Spelare {self.highscore['player']} - Dealer {self.highscore['dealer']}")

            # Play again
            again = input("Vill du spela igen? (j/n): ").lower()
            if again != "j":
                self.save_highscore()
                print("Spelet avslutas. Tack för att du spelade!")
                break

if __name__ == "__main__":
    game = Game()
    game.play()
