
print("-"*30)

names = ["Alex", "Alexandra", "Ben", "Benjamin", "Cat", "Catherine", "Dan"]
short_names = [name for name in names if len(name) <= 5]
print(short_names)

print("-"*30)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)

print("-"*30)

sentence = "I love learning Python"
words = sentence.split()
reversed_words = words[::-1]
reversed_sentence = " ".join(reversed_words)
print(reversed_sentence)

print("-"*30)