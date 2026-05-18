class Account:
    def __init__(self, number, balance, owner):
        self.number = number
        self.balance = balance
        self.owner = owner
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def add_interest(self, interest):
        interest_added = self.balance * interest
        self.balance += interest_added
        return interest_added
    


# mainline

Jack = Account(235761, 720, "Jack")

Snorbo = Account(79191, 520, "Snorbo")

Blimbo = Account(10101, 1200, "Blimbo")

counter = 0

accounts = {"Jack": Jack, "Snorbo": Snorbo, "Blimbo": Blimbo}
for people in [Jack, Snorbo, Blimbo]:
    counter += people.balance
print(f"Total bank amount: {counter} ")

print()

person = input("Enter your name: ")
if person.title() in accounts:
    d_or_w = input("Would you like to withraw or deposit? (w/d) ")
    if d_or_w == "d":
        deposit_num = int(input("How much would you like to deposit? "))
        if deposit_num > 0:
            print(f"Old balance: {accounts[person.title()].balance}")
            accounts[person.title()].deposit(deposit_num)
            print(f"New balance: {accounts[person.title()].balance}")
        else:
            raise Exception("Invalid number")
    elif d_or_w == "w":
        withdraw_num = int(input("How much would you like to withdraw? "))
        if withdraw_num > 0 and withdraw_num <= accounts[person.title()].balance:
            print(f"Old balance: {accounts[person.title()].balance}")
            accounts[person.title()].withdraw(withdraw_num)
            print(f"New balance: {accounts[person.title()].balance}")
        else:
            raise Exception("Invalid number or not enough money in account")
    else:
        raise Exception("invalid input")
    
    get_interest = float(input("What is your interest rate?(%) "))
    if 100 > get_interest > 0:
        print(f"Old balance: {accounts[person.title()].balance}")
        print(accounts[person.title()].add_interest(get_interest / 100))
        print(f"New balance: {accounts[person.title()].balance}")
        print("Interest added: {s}")
        


else:
    raise Exception("Invalid name")

