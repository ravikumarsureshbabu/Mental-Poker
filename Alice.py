from pokercards import cards
from crypto import encrypt, decrypt


encrypted_card_numbers = []

# connect to BoB
# get prime from Bob
# generate encryption key such that gcd(encryptionkey,prime) == 1 
# generate decryption key such that (encyptionkey)(decyptionkey) = 1 mod(prime)

key = None

for cardnumber in cards.keys():
    encrypted_card_numbers.append(encrypt(key,cardnumber))

print(encrypted_card_numbers)
