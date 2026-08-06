lower_min = 97
lower_max = 122
upper_min = 65
upper_max = 90
def encode(message, shift) -> str:
    result = ""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                num = ord(letter) - upper_min
                num = (num + shift) % (upper_max - upper_min + 1) # new number % range
                result += chr(num+upper_min)
            else:
                num = ord(letter) - lower_min
                num = (num + shift) % (lower_max - lower_min + 1) # new number % range
                result += chr(num+lower_min)      
        else:
            result += letter
    return result
def decode(message, shift) -> str:
    return encode(message, -shift)

print(encode('Hello', 3))
print(encode('Hello, World!', 3))
print(decode('Khoor', 3))
print(encode('xyz', 3))
print(decode('abc', 3))