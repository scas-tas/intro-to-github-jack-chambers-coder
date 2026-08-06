"""def encode(message, shift) -> str:
    result = ""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                result += chr((ord(letter) - 65 + shift) % (90 - 65 + 1)+65)
            else:
                result += chr((ord(letter) - 97 + shift) % (122 - 97 + 1)+97)      
        else:
            result += letter
    return result
def decode(message, shift) -> str:
    return encode(message, -shift)
"""

def encode(message: str, shift: int) -> str:
    return "".join(chr((ord(c) - (65 if c.isupper() else 97) + shift) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in message)

def decode(message: str, shift: int) -> str:
    return encode(message, -shift)

print(encode('Hello', 3))
print(encode('Hello, World!', 3))
print(decode('Khoor', 3))
print(encode('xyz', 3))
print(decode('abc', 3))