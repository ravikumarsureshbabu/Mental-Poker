from random import *
from pokercards import cards
from Utils import *
from crypto import decrypt

class Response:
	def __init__(self):
		self.response = None
		self.amount = None
		self.total = None

def didIwin(me, other, mycards, othercards, socket, de_key, prime):
	chance = False
	o_de_key = None
	if me == "Bob":
		chance = True
	
	if chance:
		send(socket, de_key)
		o_de_key = receive(socket)
	else:
		o_de_key = receive(socket)
		send(socket, de_key)

	# decrypt the Bobs cards
	for index, card in enumerate(othercards):
		othercards[index] = decrypt(card, o_de_key, prime)

	print(other + "'s cards are :")
	printCards(othercards, cards)
	myscore  = getscore(mycards)
	otherscore = getscore(othercards)
	print("My score : " + str(myscore))
	print( other + "'s score : " + str(otherscore))
	if myscore > otherscore:
		return True
	else:
		return False

def getscore(cards_for_score):
	d = {	"Spades" : 1, 
			"Hearts" : 2, 
			"Diamonds" : 3, 
			"Clubs"  : 4
			}
	score = 0
	for card in cards_for_score:
		score += cards[card].number
		score += d[cards[card].suite]

	return score

def playmyturn(socket, otheraised):
	print("Your Turn!")
	inp = input("F/f for fold , R/r for raise [ > "+ str(otheraised) +"]:")
	r = Response()
	if inp == "f" or inp == "F":
		r.response = "fold"
		send(socket,r)
		return "f", 0
	elif inp == "r" or inp == "R":
		r.response = "raise"
		while True:
			inp = input("Enter the amount greater than " + str(otheraised) + " :")
			r.amount = int(inp)
			if r.amount > otheraised:
				break
		send(socket,r)
		return "r", r.amount

def waitforturn(other, socket):
	print(other + "'s Turn, waiting for response ...")
	r = receive(socket)
	if r.response == "fold":
		return "f", 0
	elif r.response == "raise":
		return "r", r.amount


def printcard(cardnumber):
	print("-----------------------------------")
	print("Card number : " + str(cards[cardnumber].number) + " ,Suite : " + cards[cardnumber].suite )
	print("-----------------------------------")

def playPoker(mycards, othercards, me, other, socket, de_key, prime):
	cardnumber = 0
	print("Your first 2 Cards are :")
	# show first two cards 
	printcard(mycards[cardnumber])
	cardnumber += 1
	printcard(mycards[cardnumber])
	cardnumber += 1
	myturn = True
	if me == "Bob":
		myturn = False
	firsttime = True
	gamestatus = "playing"
	myBet = 0 
	otherBet = 0
	othersraise = 0
	while True:
		if myturn:
			if not firsttime:
				print("Your Next card is :")
				printcard(mycards[cardnumber])
				cardnumber += 1
			decision, amount =  playmyturn(socket, othersraise)
			if decision == "f":
				gamestatus = "fold"
				break
			else:
				myBet += amount
				print("Your total Bet is :" + str(myBet))
				print("----------------------------------")
			myturn = False
			firsttime = False
		else:
			if me == "Bob" and cardnumber == 5:
				gamestatus = "end"
				break
			decision, amount = waitforturn(other,socket)
			if decision == "f":
				gamestatus = "otherfolded"
				break
			else:
				othersraise = amount
				otherBet += amount
				print(other + " raised "+ str(amount)  + ", " + other + "'s total bet is :" + str(otherBet) )
			if me == "Alice" and cardnumber == 5:
				gamestatus = "end"
				break
			myturn = True

	print("---------------------------------------")
	if gamestatus == "fold":
		print("You folded, You lose your bet amount of " + str(myBet))
	elif gamestatus == "end":
		print("Time for results !")
		if didIwin(me, other, mycards,othercards,socket, de_key, prime):
			print("I won the game and amount of " + str(otherBet))
		else:
			print("I lost the game and amount of " + str(myBet))
	elif gamestatus == "otherfolded":
		print(other + " folded ! You win :" + str(otherBet))

	print("Game Over")
	print("----------------------------------------")
	return