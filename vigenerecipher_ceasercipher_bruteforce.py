import time

MAX_KEY_SIZE = 26

# VIGENERE CIPHER -- ENCRYPT-DECRYPT

def vigenereEnc():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_string = ""
    enc_key = ""
    enc_string = ""

    enc_key = input("Please enter encryption key:  ")
    enc_key = enc_key.lower()

    input_string = input("Please enter a string of text: ")
    input_string = input_string.lower()

    string_length = len(input_string)

    expanded_key = enc_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        expanded_key = expanded_key + enc_key
        expanded_key_length = len(expanded_key)

    key_position = 0

    for letter in input_string:
        if letter in alphabet:
            position = alphabet.find(letter)
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            new_position = position + key_character_position
            if new_position > 26:
                new_position = new_position - 26
            new_character = alphabet[new_position]
            enc_string = enc_string + new_character
        else:
            enc_string = enc_string + letter
    return (enc_string)


def vigenereDec():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_string = ""
    dec_key = ""
    dec_string = ""

    dec_key = input("Please enter encryption key: ")
    dec_key = dec_key.lower()

    input_string = input("Please enter a string of text: ")
    input_string = input_string.lower()

    string_length = len(input_string)

    expanded_key = dec_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        expanded_key = expanded_key + dec_key
        expanded_key_length = len(expanded_key)

    key_position = 0

    for letter in input_string:
        if letter in alphabet:
            position = alphabet.find(letter)
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            new_position = position - key_character_position
            if new_position > 26:
                new_position = new_position + 26
            new_character = alphabet[new_position]
            dec_string = dec_string + new_character
        else:
            dec_string = dec_string + letter
    return (dec_string)


# CEASER CIPHER -- ENCRYPT-DECRYPT-BRUTE FORCE
def getModeCeaser():
    while True:
        print("-----------     MENU      ------------")
        print("--                                  --")
        print("--          Encrypt          ---> E --")
        print("--          Decrypt          ---> D --")
        print("--          Brute Force      ---> B --")
        print("--          Menü             ---> Q --")
        print("--                                  --")
        print("--------------------------------------")
        mode = input("Choose function :  ").lower()
        if mode in 'encrypt e decrypt d brute b quit q'.split():
            return mode[0]
        else:
            print("You entered the wrong option. Please check..\n")

def getMessage():
    print('Please enter your message:')
    return input()

def getKey():
    while True:
        print('Please enter your key number (1-% s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

def CeaserLoop():
    while True:
        mode = getModeCeaser()
        if mode[0] == 'q':
            print("Returning to the menu...")
            time.sleep(1)
            print("Choose function:  ")
            break
        message = getMessage()
        if mode[0] == 'e':
            key = getKey()
            print(getTranslatedMessage(mode, message, key))
            time.sleep(1)
            continue
        if mode[0] == 'd':
            key = getKey()
            print(getTranslatedMessage(mode, message, key))
            time.sleep(1)
            continue
        if mode[0] == 'b':
            key = 0
            for key in range(1, MAX_KEY_SIZE + 1):
                print(key," ---> ", getTranslatedMessage('decrypt', message, key))
            time.sleep(1)
            continue

def getModeVigenere():
    while True:
        print("--------------------------------------")
        print("--         VIGENERE CIPHER          --")
        print("--------------------------------------")
        print("-----------     MENU      ------------")
        print("--                                  --")
        print("--             Encrypt       ---> E --")
        print("--             Decrypt       ---> D --")
        print("--             Menu          ---> Q --")
        print("--                                  --")
        print("--------------------------------------")
        mode = input("Choose function :  ").lower()
        if mode in 'encrypt e decrypt d brute b quit q'.split():
            return mode[0]
        else:
            print("You entered the wrong option. Please check.. \n")

def VigenereLoop():
    while True:
        mode = getModeVigenere()
        if mode[0] == 'q':
            print("Returning to the menu...")
            time.sleep(1)
            print("Choose function :  ")
            break
        if mode[0] == 'e':
            print(vigenereEnc())
            time.sleep(1)
            continue
        if mode[0] == 'd':
            print(vigenereDec())
            time.sleep(1)
            continue

def ChooseAlgorithm():
    while True:
        print("--------------------------------------")
        print("--      VIGENERE CIPHER  --> V      --")
        print("--      CEASER CIPHER    --> C      --")
        print("--      QUIT             --> Q      --")
        print("--------------------------------------")
        mode = input("Choose function :  ").lower()
        if mode in 'vigenere v ceaser c quit q'.split():
            return mode[0]
        else:
            print("You entered the wrong option. Please check..\n")


while True:
    mode = ChooseAlgorithm()
    if mode[0] == 'q':
        print("Exiting to the program...")
        time.sleep(1)
        print("Logged out..")
        break
    if mode[0] == 'v':
        VigenereLoop()
        time.sleep(1)
        continue
    if mode[0] == 'c':
        CeaserLoop()
        time.sleep(1)
        continue

