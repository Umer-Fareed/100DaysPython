#ceaser Cipher
import math

from Day7.Hangman import position
from art import logo
print(logo)
def ceaser(start_text,shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:

            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"The {cipher_direction}d text is {end_text}")

alphabet = ['a','b','c','d','e','f','g','h','i','j','k',
            'l','m','n','o',
            'p','q','r','s','t','u','v','w','x','y','z',
            'a','b','c','d','e','f','g','h','i','j','k',
            'l','m','n','o',
            'p','q','r','s','t','u','v','w','x','y','z']
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to "
                      "decrypt: \n")
    text = input("Type your text: \n").lower()
    shift=int(input("Type the shift number : \n"))
    shift=shift%26
    ceaser(start_text=text , shift_amount=shift,
            cipher_direction=direction)
    result=input("Type 'yes' if you want to go again. Otherwise "
          "type 'no'.\n")
    if result=="no":
        should_continue=False
        print("good bye ")
#Combine function names 'Ceaser'




#task1- create a function called 'encrypt' that take the 'text'
#and 'shift' as input
# def encrypt(plain_text,shift_text):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_text
#         new_letter = alphabet[new_position]
#         cipher_text+=new_letter
#     print(f"the encoded text is '{cipher_text}'")
#
#



# #decode text
# def decrypt(cipher_text , shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position= position-shift_amount
#         plain_text+=alphabet[new_position]
#     print(f"the decoded text is '{plain_text}'")
#
# #call the function and pass input
# if direction=="encode":
#     encrypt(plain_text=text, shift_text=shift)
# elif direction=="decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("enter the right keyword")










