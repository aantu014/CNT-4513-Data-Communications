import string
#import some modules from flask
from flask import Flask, render_template, request, url_for


#Instantiate (create) our flask app object
app = Flask(__name__)
#debug mode so our browser doesn't cache (save) our page

#our index (main) page
@app.route('/')
def index():
    return render_template('index.html')


#encyption page
@app.route('/encryptCaesar', methods=['GET', 'POST'])
def encryptCaesar():
  #if the user is requesting the page via GET request, just return our webpage in html
  if request.method == 'GET':
    return render_template('index.html')
    #if the user POSTs us some data, let's encrypt it and return the encrypted message
  elif request.method == 'POST':
    try:  
      message = str(request.form["messageC"])
      key = int(request.form['keyC'])
      encryptedmessage =encryptC(message, key)
      return render_template('index.html', encrypted_messageC=encryptedmessage)
    except Exception as e:
      return render_template('index.html', encrypted_messageC="Please enter a valid message or key.")
        

#decryption page
@app.route('/decryptCaesar', methods=['GET', 'POST'])
def decryptCaesar():
  if request.method == 'GET':
    return render_template('index.html')
    #if the user POSTs us some data, let's encrypt it and return the encrypted message
  elif request.method == 'POST':
    try:
      cipher = str(request.form["cipherC"])
      unlock = int(request.form['unlockC'])
      decryptedmessage =decryptC(cipher, unlock)
      return render_template('index.html', decrypted_messageC=decryptedmessage)
    except Exception as e:
      return render_template('index.html', decrypted_messageC="Please enter a valid message or key.")           
   
#encyption page
@app.route('/encryptVigenère', methods=['GET', 'POST'])
def encryptVigenère():
  #if the user is requesting the page via GET request, just return our webpage in html
  if request.method == 'GET':
    return render_template('index.html')
  #if the user POSTs us some data, let's encrypt it and return the encrypted message
  elif request.method == 'POST':
    try:
      message = str(request.form["messageV"])
      key = str(request.form['keyV'])
      encryptedmessage =encryptV(message, key)
      return render_template('index.html', encrypted_messageV=encryptedmessage)
    except Exception as e:
      return render_template('index.html', encrypted_messageV="Please enter a valid message or key.")   
        

#decryption page
@app.route('/decryptVigenère', methods=['GET', 'POST'])
def decryptVigenère():
  if request.method == 'GET':
    return render_template('index.html')
  #if the user POSTs us some data, let's encrypt it and return the encrypted message
  elif request.method == 'POST':
    try:
      cipher = str(request.form["cipherV"])
      unlock = str(request.form['unlockV'])
      decryptedmessage =decryptV(cipher, unlock)
      return render_template('index.html',  decrypted_messageV=decryptedmessage)
    except Exception as e:
      return render_template('index.html', decrypted_messageV="Please enter a valid message or key.")           

def encryptC(plainText, shift):

  cipherText = caesar(plainText, shift)
  
  return cipherText 

def decryptC(encryption, encryption_shift):  
  cipherText1 = ""
  for c in encryption:
    if c.isalpha():
      stayInAlphabet1 = ord(c) - encryption_shift
    if stayInAlphabet1 > ord('z'):
      stayInAlphabet1 += 26
    finalLetter1 = chr(stayInAlphabet1)
    cipherText1 += finalLetter1
  
  return cipherText1


def caesar(plaintext, shift):
  
  for letter in plaintext:
    alphabet=string.ascii_letters
    shifted_alpahbet=alphabet[shift:] + alphabet[:shift]

  
  table=str.maketrans(alphabet, shifted_alpahbet)
  return plaintext.translate(table)

def  encryptV(input_string, enc_key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  enc_string = ""

  # Takes encrpytion key from user
  enc_key = enc_key.lower()

  # Takes string from user
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
  return enc_string


def decryptV(input_string, dec_key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  dec_string = ""

  # Takes encrpytion key from user
  dec_key = dec_key.lower()
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
  return dec_string


if __name__ == "__main__":
    app.run()
