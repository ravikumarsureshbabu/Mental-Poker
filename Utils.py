from random import *

import pickle


BUFFER_SIZE = 1024

def send(conn, data):
	data = pickle.dumps(data)
	conn.send(data)

def receive(conn):
	data = conn.recv(BUFFER_SIZE)
	data = pickle.loads(data)
	return data

def pick5cards(cards):
	pickedcards = []
	for i in range(0,5):
		card = choice(cards)
		cards.remove(card)
		pickedcards.append(card)
	return pickedcards

def printCards(cards, deck):
	for cardnumber in cards:
		print("Card Number :" + str(deck[cardnumber].number) + ", Suite :" + deck[cardnumber].suite )
