characters = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż0123456789"

def vigenere_cipher():
    print("Enter your message:")
    message = input()
    print("Enter your key:")
    key = input()
    print("Enter '1' for encryption or '0' for decryption:")
    encryption = bool(int(input()))

    result = ""

    for i in range(len(message)):
        if message[i].strip() == "":
            result += " "
            continue

        message_symbol = characters.index(message[i])
        key_symbol = characters.index(key[i % len(key)])

        if encryption:
            value = (message_symbol + key_symbol) % len(characters)
        else:
            value = (message_symbol - key_symbol) % len(characters)

        result += characters[value]

    print("Your encrypted/decrypted message: " + result)


if __name__ == "__main__":
    vigenere_cipher()
