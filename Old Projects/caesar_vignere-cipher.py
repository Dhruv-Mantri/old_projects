def encode():
    mode = input("[1] Caesar Ciphar\n[2] Vigenere Cipher  ")
    if mode == '1':
        message = input("Enter a message to encode: ")
        shift = int(input("Enter a shift: "))
        for i,m in enumerate(message):
            if message[i].islower():
                coded_message.append(chr((ord(message[i]) - ord("a") + shift) % 26 + ord("a")))
            elif message[i].isupper():
                coded_message.append(chr((ord(message[i]) - ord("A") + shift) % 26 + ord("A")))
            else:
                coded_message.append(message[i])
    elif mode == '2':
        vigenere()

def decode(message, known_word):
    message = list(message.split(" "))
    word_list = list(known_word)
    shifts = 0
    while True:
        for letters, value in enumerate(word_list):
            if value.islower():
                word_list[letters] = chr((ord(value) - ord("a") + 1) % 26 + ord("a"))
            elif value.isupper():
                word_list[letters] = chr((ord(value) - ord("A") + 1) % 26 + ord("A"))
        shifts += 1
        final_word = "".join(word_list)
        for index, words in enumerate(message):
            if final_word == words:
                return shifts

def vigenere():
    rotation_direction = 1
    if selection.lower() == 'd':
        rotation_direction = -1
    message = list(input("Enter a message: "))
    key = input("Enter a key: ")
    key_final = list(key*((len(message)//len(key))+1))
    spaces = []
    for i, m in enumerate(message):
        if m in [" ",'.',',','?','!','/','@','#','$','%','&','(',')',"'",'"',"-","+",'=']:
            spaces.append(i)
    for i in spaces:
        key_final.insert(int(i), " ")
    for i,m in enumerate(message):
        if message[i].islower():
            key_final[i] = key_final[i].lower()
            coded_message.append(chr((ord(message[i]) - ord("a") + rotation_direction*(ord(key_final[i]) - ord("a"))) % 26 + ord("a")))
        elif message[i].isupper():
            key_final[i] = key_final[i].upper()
            coded_message.append(chr((ord(message[i]) - ord("A") + rotation_direction*(ord(key_final[i]) - ord("A"))) % 26 + ord("A")))
        else:
            coded_message.append(message[i])

selection = ""

while selection != "q":
    coded_message = []
    shifts = []
    selection = input("\n[e] Encode \n[d] Decode\n[q] quit  ")

    if selection.lower() == 'e':
        encode()
        print("The encoded message is:  ", end="")

    elif selection.lower() == "d":
        mode = input("[1] Caesar Ciphar\n[2] Vigenere Cipher  ")
        if mode == '1':
            message = input("Enter a message to decode: ")
            word = input("Enter a word that is in the message: ")
            shifts = decode(message,word)
            for i in message:
                if i.islower():
                    coded_message.append(chr((ord(i) - ord("a") - shifts) % 26 + ord("a")))
                elif i.isupper():
                    coded_message.append(chr((ord(i) - ord("A") - shifts) % 26 + ord("A")))
                else:
                    coded_message.append(i)
            print("The rotation was: "+ str(shifts))
        elif mode == '2':
            vigenere()
        print("The decoded message is:  ", end="")

    print("".join(coded_message))