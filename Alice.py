from pokercards import cards
from crypto import encrypt, decrypt, generate_keys
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(BUFFER_SIZE)
prime = int(data.decode())
en_key, de_key = generate_keys(prime)

encrypted_card_numbers = []

# connect to BoB
# get prime from Bob
# generate encryption key such that gcd(encryptionkey,prime) == 1 
# generate decryption key such that (encyptionkey)(decyptionkey) = 1 mod(prime)

for cardnumber in cards.keys():
    encrypted_card_numbers.append(encrypt(cardnumber, en_key, prime))

print(encrypted_card_numbers)


for each in encrypted_card_numbers:
    print(decrypt(each, de_key, prime), end = " ")


