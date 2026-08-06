def encode(message, shift) -> str:
    lower_min = 97
    lower_max = 122
    upper_min = 65
    upper_max = 90

    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                num = ord(letter) - upper_min
                num = (num + shift) % upper_max
                print(chr(num+upper_min), end="")
            else:
                num = ord(letter) - lower_min
                #print(f"test no 1: {num}")
                num = (num + shift) % (lower_max - lower_min)
                #print(f"test no 2: {num}")
                print(chr(num+lower_min), end="")
            
        else:
            print(letter, end="")
    print()
 
def decode(message, shift) -> str:
    return

encode('Hello', 3)