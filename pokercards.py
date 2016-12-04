
class Card:
    def __init__(self, number, suite):
        self.number = number
        self.suite = suite

numbers = list(range(1,14))
suites = ["Spades", "Hearts", "Diamonds", "Clubs"]
cards = {}
card_num = 1
for suite in suites:
    for num in numbers:
        cards[card_num] = Card(num,suite)
        card_num += 1





