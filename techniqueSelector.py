from os.path import exists
import random
import rsa

encryption_techniques = ["Caesar cipher", "Vigenere cipher", "RSA", "AES"]

def encrypt_technique_using_rsa(message, public_key):
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    return encrypted_message

def store_input_write(input, filename):
    if(not exists(filename)):
        open(filename, "x")
    with open(filename, "w") as file:
        file.write(input)

def read_from_file(filename):
    if(not exists(filename)):
        open(filename, "x")
    with open(filename, "r") as file:
        text = file.read()
    return text

def choose_encryption_technique():
    return random.choice(encryption_techniques)

public_key = read_from_file("public_key.pem")
encryptedTechniqueName = encrypt_technique_using_rsa(choose_encryption_technique(),eval("rsa."+public_key))
store_input_write(repr(encryptedTechniqueName), "encrypted_technique.txt")