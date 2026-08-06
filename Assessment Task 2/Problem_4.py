lower_min = 97
lower_max = 122
upper_min = 65
upper_max = 90


def encode(message, shift) -> str:
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                num = ord(letter) - upper_min
                num = (num + shift) % (upper_max - upper_min + 1) # new number % range
                print(chr(num+upper_min), end="")
            else:
                num = ord(letter) - lower_min
                num = (num + shift) % (lower_max - lower_min + 1) # new number % range
                print(chr(num+lower_min), end="")       
        else:
            print(letter, end="")
    print()
 
def decode(message, shift) -> str:
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                num = ord(letter) - upper_min
                num = (num - shift) % (upper_max - upper_min + 1) # new number % range
                print(chr(num+upper_min), end="")
            else:
                num = ord(letter) - lower_min
                num = (num - shift) % (lower_max - lower_min + 1) # new number % range
                print(chr(num+lower_min), end="")         
        else:
            print(letter, end="")
    print()

encode('Hello', 3)
encode('Hello, World!', 3)
decode('Khoor', 3)
encode('xyz', 3)
decode('abc', 3)