class Account:
    def __init__(self, number, balance, owner):
        self.number = number
        self.balance = balance
        self.owner = owner
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount


# mainline

Jack = Account(235761, 7200000, "Jack")

Snorbo = Account(79191, 52, "Snorbo")

Blimbo = Account(10101, 10, "Blimbo")

counter = 0

accounts = {"Jack": Jack, "Snorbo": Snorbo, "Blimbo": Blimbo}
for people in [Jack, Snorbo, Blimbo]:
    counter += people.balance
print(f"Total bank amount: {counter} ")


person = input("Enter your name: ")
if person in accounts:
    d_or_w = input("Would you like to withraw or deposit? (w/d)")
    if d_or_w == "d":
        deposit_num = int(input("How much would you like to deposit? "))
        if deposit_num > 0:
            print(f"Old balance: {accounts[person].balance}")
            accounts[person].deposit(deposit_num)
            print("New balance: {person.balance}")
        else:
            raise Exception("Invalid number")
    elif d_or_w == "w":
        withdraw_num = int(input("How much would you like to withdraw? "))
        if withdraw_num > 0:
            print(f"Old balance: {accounts[person].balance}")
            accounts[person].withdraw(withdraw_num)
            print(f"New balance: {accounts[person].balance}")
        else:
            raise Exception("Invalid number")
    else:
        raise Exception("invalid input")

else:
    raise Exception("Invalid name")
