from pokercards import cards
from crypto import encrypt, decrypt
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send("73".encode())

s.close
# connect to ALice
# generate prime number
# send it to Alice
# geberate encyption key
# generate decyption key 


