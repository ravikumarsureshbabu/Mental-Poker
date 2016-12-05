from pokercards import cards
from crypto import *
from Utils import *
from poker import playPoker

import socket
import pickle


TCP_IP = '127.0.0.1'
TCP_PORT = 5002
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to ALice
s.connect((TCP_IP, TCP_PORT))

# generate prime number
prime = generate_prime(10000,20000)

#send prime to Alice
send(s,prime)


# generate encryption key such that gcd(encryptionkey,prime) == 1 
# generate decryption key such that (encyptionkey)(decyptionkey) = 1 mod(prime)
en_key, de_key = generate_keys(prime)

# receive encrypted cards from Alice
encryted_card_numbers = receive(s)
#print(encryted_card_numbers)

# pick random 5 cards for me
mycards = pick5cards(encryted_card_numbers)
# pick random 5 cards for alice
alicecards = pick5cards(encryted_card_numbers)

# encrypt my cards
for i,card in enumerate(mycards):
	mycards[i] = encrypt(card, en_key, prime)

#send alice cards
send(s, alicecards)
#send my cards
send(s, mycards)

# receive my decrypted cards from alice
mycards = receive(s)

# decrypt my cards
for index, card in enumerate(mycards):
	mycards[index] = decrypt(card, de_key, prime)

#print("My Cards are")
#printCards(mycards, cards)


#playPoker(mycards, othercards, me, other, socket, de_key, prime)
playPoker(mycards, alicecards, "Bob", "Alice", s, de_key, prime)

s.close






