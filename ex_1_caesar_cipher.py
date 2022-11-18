characters = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż0123456789"

def caesar_cipher():
    print("Enter your message:")
    message = input()
    print("Enter desired shift value:")
    shift = int(input())
    print("Enter '1' for encryption or '0' for decryption:")
    encryption = bool(int(input()))
    
    if not encryption:
        shift = shift * (-1)

    result = ""

    for i in range(len(message)):
        if message[i].strip() == "":
            result += " "
            continue

        index = characters.index(message[i])
        
        try:
            result += characters[index + shift]
        except IndexError:
            result += characters[index + shift - len(characters)]
    
    print("Your encrypted/decrypted message: " + result)


if __name__ == "__main__":
    caesar_cipher()
