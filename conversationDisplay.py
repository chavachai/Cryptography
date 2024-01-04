import rsa
from os.path import exists
import base64
import os

def decrypt_message_using_rsa(ciphertext, private_key):
    decrypted_message = rsa.decrypt(base64.b64decode(base64.b64encode(ciphertext).decode()), private_key).decode()
    return decrypted_message

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

def decrypt_message(ciphertext, technique):
    if technique == "Caesar cipher":
        return ciphertext
    elif technique == "Vigenere cipher":
        return ciphertext
    elif technique == "AES":
        return ciphertext
    else:
        return ciphertext

if(os.path.exists("public_key.pem")):
    os.remove("public_key.pem")
if(os.path.exists("conversation.txt")):
    os.remove("conversation.txt")
if(os.path.exists("encrypted_technique.txt")):
    os.remove("encrypted_technique.txt")

(public_key, private_key) = rsa.newkeys(2048)
store_input_write(repr(public_key), "public_key.pem")

while(True):
    encrypted_technique = read_from_file("encrypted_technique.txt")
    decryptedTechniqueName = ""
    if(encrypted_technique!=""):
        decryptedTechniqueName = decrypt_message_using_rsa(eval(encrypted_technique), private_key)
    encrypted_conversation = read_from_file("conversation.txt")
    decryptedConversation = ""
    if(encrypted_conversation!=""):
        decryptedConversation = decrypt_message(encrypted_conversation, decryptedTechniqueName)
        os.system('cls')
    print(decryptedConversation)