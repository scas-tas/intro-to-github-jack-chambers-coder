class Account:
    def __init__(self, number, balance, owner):
        self.number = number
        self.balance = balance
        self.owner = owner

# mainline

Jack = Account(235761, 7200000, "Jack")

Snorbo = Account(79191, 52, "Snorbo")

print(Jack.number)
print(Snorbo.balance)
print(Jack.owner)

Fail = Account(10101, 10, "Fail")
counter = 0

for people in [Jack, Snorbo, Fail]:
    counter += people.balance
print(counter)