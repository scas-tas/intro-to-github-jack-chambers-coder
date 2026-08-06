def encode(message, shift) -> str:
    lower_min = 97
    lower_max = 122
    upper_min = 65
    upper_max = 90

    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                num = ord(letter)
                num += shift
                print(chr(num), end="")
            
        else:
            print(letter, end="")
    print()
 
def decode(message, shift) -> str:
    return


encode('Hello', 3)