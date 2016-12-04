from randon import *
from pokercards import cards
from Utils import *

class Response:
	def __init__(self):
		self.response 
		self.amount
		self.total

def playmyturn(socket)
	print("Your Turn!")
	inp = input("F/f for fold , R/r for raise :")
	r = Response()
	if inp == "f" or inp == "F":
		r.response = "fold"
		send(socket,r)
		retrun "f", 0
	elif inp == "r" or inp == "R"
		r.response = "raise"
		inp = input("Enter the amount :")
		r.amount = int(inp)
		send(socket,r)
		return "r", amount

def waitforturn(other, socket):
	print(other + "'s Turn, waiting for response")
	r = receive(socket)
	if r.response == "fold":
		return "f", 0
	elif r.response == "raise"
		return "r", r.amount


def printcard(cardnumber)
	print("Card number :" + cards[cardnumber].number + "Suite :" + cards[cardnumber].suite )

def playPoker(mycards, othercards, me, other, socket):
	cardnumber = 0
	print("Your Cards are :")
	# show first two cards 
	printcard(mycards[cardnumber])
	cardnumber += 1
	printcard(mycards[cardnumber])
	cardnumber += 1
	myturn = True
	if 0 == random(0,2):
		myturn = False
	firsttime = True
	gamestatus = "playing"
	myBet = 0 
	otherBet = 0

	while True:
		if myturn:
			if not firsttime:
				if cardnumber == 5:
					gamestatus = "end"
					break
				printcard(mycards[cardnumber])
				cardnumber += 1
			decision, amount =  playmyturn(socket):
			if decision == "f":
				gamestatus = "fold"
				break
			else
				myBet += amount
				print("Your total Bet is :" + myBet)
			myturn = False
		else:
			decision, amount = waitforturn(other,socket)
			if decision == "f":
				print(other + "folded ! You win :" + otherBet)
			else
				otherBet += amount
				print(other + "raised !" + other + "'s bet is :" + otherBet )
			myturn = True

	if gamestatus == "fold":
		print("You folded, You lose your bet amount of " + myBet)
	elif gamestatus == "end"
		print("Time for results !")
		if didIwin(mycards,othercards,socket):
			print("I won the game and amount of" + otherBet)
		else
			print("I lost the game and amount of" + myBet)

	print("Game Over")
	return