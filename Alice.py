from pokercards import cards
from crypto import encrypt, decrypt, generate_keys
from Utils import *

import socket
import pickle


TCP_IP = '127.0.0.1'
TCP_PORT = 5002
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

# connect to BoB
conn, addr = s.accept()


# get prime from Bob
prime = receive(conn)

# generate encryption key such that gcd(encryptionkey,prime) == 1 
# generate decryption key such that (encyptionkey)(decyptionkey) = 1 mod(prime)
en_key, de_key = generate_keys(prime)

# encrypt the cards
encrypted_card_numbers = []
for cardnumber in cards.keys():
    encrypted_card_numbers.append(encrypt(cardnumber, en_key, prime))

# send encrytped cards to Bob
send(conn, encrypted_card_numbers)

# receive my crads
mycards = receive(conn)

# receive bob cards
bobcards = receive(conn)

# decrypt my cards
for index, card in enumerate(mycards):
	mycards[index] = decrypt(card, de_key, prime)

# decrypt bob cards
for index, card in enumerate(bobcards):
	bobcards[index] = decrypt(card, de_key, prime)

# send bob cards to bob
send(conn, bobcards)

print("My Cards are")
printCards(mycards, cards)




conn.close()
s.close()

