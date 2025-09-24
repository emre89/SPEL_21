from game.player import Player
from game.dealer import Dealer

# Testar att Player kan slå en tärning och totalen uppdateras
def test_player_roll_increases_total():
    player = Player("Test")
    initial_total = player.total
    value = player.roll()
    assert 1 <= value <= 6
    assert player.total == initial_total + value

# Testar att Dealer spelar tills minst 17
def test_dealer_plays_until_17():
    dealer = Dealer()
    rolls = dealer.play()
    assert dealer.total >= 17
    assert all(1 <= r <= 6 for r in rolls)

# Testar att reset sätter tillbaka totalen
def test_reset_resets_score():
    player = Player("Test")
    player.roll()
    assert player.total > 0
    player.reset()
    assert player.total == 0
