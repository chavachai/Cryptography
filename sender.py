import datetime
from os.path import exists

def caesar_cipher(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_message = ""
    for char in message:
        if char.lower() in alphabet:
            char_index = alphabet.index(char.lower())
            encrypted_index = (char_index + key) % 26
            if char.isupper():
                encrypted_message += alphabet[encrypted_index].upper()
            else:
                encrypted_message += alphabet[encrypted_index]
        else:
            encrypted_message += char
    return encrypted_message


def store_input_write(input, filename):
    if(not exists(filename)):
        open(filename, "x")
    with open(filename, "w") as file:
        file.write(input)
    
def store_input_append(input, filename):
    if(not exists(filename)):
        open(filename, "x")
    with open(filename, "a") as file:
        file.write(input+"\n")

def read_from_file(filename):
    if(not exists(filename)):
        open(filename, "x")
    with open(filename, "r") as file:
        text = file.read()
    return text

def encrypt_message(message, technique):
    if technique == "Caesar cipher":
        return caesar_cipher(message, 5)
    elif technique == "Vigenere cipher":
        return message
    elif technique == "AES":
        return message
    else:
        return message

technique = read_from_file("encryption_technique.txt")
userName = input("Enter your name: ")

if __name__ == "__main__":
    while(True):
        message = input("Enter a message: ")
        timestamp = datetime.datetime.now()
        concatenatedMessage = "["+userName+","+str(timestamp)+"]"+":"+message
        encrypted_message = encrypt_message(concatenatedMessage,technique)
        store_input_append(encrypted_message, "conversation.txt")
    