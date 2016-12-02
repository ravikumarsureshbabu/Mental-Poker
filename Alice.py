from pokercards import cards
from crypto import encrypt, decrypt


encrypted_card_numbers = []
key = None

for cardnumber in cards.keys():
    encrypted_card_numbers.append(encrypt(key,cardnumber))

print(encrypted_card_numbers)
