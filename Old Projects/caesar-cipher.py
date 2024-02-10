def encode(message, shift):
    for i,m in enumerate(message):
        if message[i].islower():
            coded_message.append(chr((ord(message[i]) - ord("a") + shift) % 26 + ord("a")))
        elif message[i].isupper():
            coded_message.append(chr((ord(message[i]) - ord("A") + shift) % 26 + ord("A")))
        else:
            coded_message.append(message[i])

def decode(message, shift):
    message = list(message.split(" "))
    word_list = list(word)
    shifts = 0
    decoded = False
    while decoded == False:
        for letters, value in enumerate(word_list):
            if value.islower():
                word_list[letters] = chr((ord(value) - ord("a") + 1) % 26 + ord("a"))
            elif value.isupper():
                word_list[letters] = chr((ord(value) - ord("A") + 1) % 26 + ord("A"))
        shifts += 1
        final_word = "".join(word_list)
        for index, words in enumerate(message):
            if final_word == words:
                decoded = True
                return shifts
            else:
                decoded = False

selection = ""

while selection != "q":
    coded_message = []
    shifts = []
    selection = input("\n[e] Encode \n[d] Decode\n[q] quit  ")

    if selection.lower() == 'e':
        message = input("Enter a message: ")
        shift = int(input("Enter a shift: "))
        encode(message,shift)

    if selection.lower() == "d":
        message = input("Enter a message: ")
        word = input("Enter a word that is in the message: ")
        shifts = decode(message,word) 
        message = list(message)
        for i in message:
            if i.islower():
                coded_message.append(chr((ord(i) - ord("a") - shifts) % 26 + ord("a")))
            elif i.isupper():
                coded_message.append(chr((ord(i) - ord("A") - shifts) % 26 + ord("A")))
            else:
                coded_message.append(i)
        print("The message is:  ", end="")

    print("".join(coded_message))