#!/usr/bin/python3

import string
from tkinter import *

def encryptC():
  plainText= input("What is your plaintext? ")
  shift= int(input("what is your shift? "))
  cipherText=caesar(plainText, shift)
  print("Your cipher is: ", cipherText, " with a shift of ", shift )  

def decryptC():
  encryption=input("Enter in your encrypted code. ")
  encryption_shift=int(input("Enter in your encryption shift. "))

  cipherText1 = ""
  for c in encryption:
    if c.isalpha():
      stayInAlphabet1 = ord(c) - encryption_shift
    if stayInAlphabet1 > ord('z'):
      stayInAlphabet1 += 26
    finalLetter1 = chr(stayInAlphabet1)
    cipherText1 += finalLetter1

  print ("Your ciphertext is: ", cipherText1,"with negative shift of ",encryption_shift)

 

def caesar(plaintext, shift):
  
  for letter in plaintext:
    alphabet=string.ascii_letters
    shifted_alpahbet=alphabet[shift:] + alphabet[:shift]

  
  table=str.maketrans(alphabet, shifted_alpahbet)
  return plaintext.translate(table)


def  encryptV():
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  input_string = ""
  enc_key = ""
  enc_string = ""

  # Takes encrpytion key from user
  enc_key = input("Please enter encryption key: ")
  enc_key = enc_key.lower()

  # Takes string from user
  input_string = input("Please enter plain text: ")
  input_string = input_string.lower()

  # Lengths of input_string
  string_length = len(input_string)

  # Expands the encryption key to make it longer than the inputted string
  expanded_key = enc_key
  expanded_key_length = len(expanded_key)

  while expanded_key_length < string_length:
    # Adds another repetition of the encryption key
    expanded_key = expanded_key + enc_key
    expanded_key_length = len(expanded_key)

  key_position = 0

  for letter in input_string:
    if letter in alphabet:
      # cycles through each letter to find it's numeric position in the alphabet
      position = alphabet.find(letter)
      # moves along key and finds the characters value
      key_character = expanded_key[key_position]
      key_character_position = alphabet.find(key_character)
      key_position = key_position + 1
      # changes the original of the input string character
      new_position = position + key_character_position
      if new_position > 26:
        new_position = new_position - 26
      new_character = alphabet[new_position]
      enc_string = enc_string + new_character
    else:
      enc_string = enc_string + letter
  print("Your cipher is: ", enc_string, " with a encryption key of ", enc_key )


def decryptV():
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  input_string = ""
  dec_key = ""
  dec_string = ""

  # Takes encrpytion key from user
  dec_key = input("Please enter encryption key: ")
  dec_key = dec_key.lower()

  # Takes string from user
  input_string = input("Please enter encrypted text: ")
  input_string = input_string.lower()

  # Lengths of input_string
  string_length = len(input_string)

  # Expands the encryption key to make it longer than the inputted string
  expanded_key = dec_key
  expanded_key_length = len(expanded_key)

  while expanded_key_length < string_length:
    # Adds another repetition of the encryption key
    expanded_key = expanded_key + dec_key
    expanded_key_length = len(expanded_key)

  key_position = 0

  for letter in input_string:
    if letter in alphabet:
      # cycles through each letter to find it's numeric position in the alphabet
      position = alphabet.find(letter)
      # moves along key and finds the characters value
      key_character = expanded_key[key_position]
      key_character_position = alphabet.find(key_character)
      key_position = key_position + 1
      # changes the original of the input string character
      new_position = position - key_character_position
      if new_position > 26:
        new_position = new_position + 26
      new_character = alphabet[new_position]
      dec_string = dec_string + new_character
    else:
      dec_string = dec_string + letter
  print("Your cipher is: ", dec_string, " with a decryption key of ", dec_key )



menu=Tk()
menu.title("menu")
menu.geometry("300x300")
button1=Button(menu, text="Encrypt with Caesar Cipher.", command=encryptC)
button1.pack()

button2=Button(menu, text="Decrypt with Caesar Cipher.", command=decryptC)
button2.pack()

button3=Button(menu, text="Encrypt with Vigenère Cipher.", command=encryptV)
button3.pack()

button4=Button(menu, text="Decrypt with Vigenère Cipher.", command=decryptV)
button4.pack()

button5=Button(menu, text="exit", command=exit)
button5.pack()

menu.mainloop()
