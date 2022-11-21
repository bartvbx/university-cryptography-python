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

    for i in message:
        if i in characters:
            index = characters.index(i)
            result += characters[(index + shift) % len(characters)]
        else:
            result += i
    
    print("Your encrypted/decrypted message: " + result)


if __name__ == "__main__":
    caesar_cipher()
