
break_ = ""


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
        return f"Interest added: {interest_added}"

class Savings(Account):
    def __init__(self, number, balance, owner):
        super().__init__(number, balance, owner)
    
    def withdraw(self, amount):
        if amount < 100:
            print("Must withdraw above 100")
        else:
            self.balance -= amount

class Term_deposit(Account):
    def __init__(self, number, balance, owner, time):
        super().__init__(number, balance, owner)
        self.time = time
    
    def withdraw(self, amount):
        if self.time < 365:
            print("INVALID - Must be invested for longer")
        else:
            self.balance -= amount
    
    def deposit(self, amount):
        if self.time < 365:
            print("INVALID - Must be invested for longer")
        else:
            self.balance += amount

# mainline

def main_line():
    person = input("Enter your name: ")
    while True:
        if person.title() in accounts_dict:
            d_or_w = input("Would you like to withraw or deposit? (w/d) ")
            if d_or_w == "d":
                deposit_num = int(input("How much would you like to deposit? "))
                if deposit_num > 0:
                    print(f"Old balance: {accounts_dict[person.title()].balance}")
                    accounts_dict[person.title()].deposit(deposit_num)
                    print(f"New balance: {accounts_dict[person.title()].balance}")
                else:
                    print("Invalid number")
                    return
            elif d_or_w == "w":
                withdraw_num = int(input("How much would you like to withdraw? "))
                if withdraw_num > 0 and withdraw_num <= accounts_dict[person.title()].balance:
                    print(f"Old balance: {accounts_dict[person.title()].balance}")
                    accounts_dict[person.title()].withdraw(withdraw_num)
                    print(f"New balance: {accounts_dict[person.title()].balance}")
                else:
                    print("Invalid number or insufficient funds")
                    return
            else:
                print("invalid input")
                return
            
            get_interest = float(input("What is your interest rate?(%) "))
            if 100 > get_interest > 0:
                print(f"Old balance: {accounts_dict[person.title()].balance}")
                print("-"*30)
                print(accounts_dict[person.title()].add_interest(get_interest / 100))
                print("-"*30)
                print(f"New balance: {accounts_dict[person.title()].balance}")
                return


        else:
            print("Invalid name")
            return

def accounts():
    global Jack, Snorbo, Blimbo, Test, accounts_dict, Jack_S, Snorbo_T
    Jack = Account(235761, 720, "Jack")

    Snorbo = Account(79191, 520, "Snorbo")

    Blimbo = Account(10101, 1200, "Blimbo")

    Test = Account(91935, 100, "Test")

    Jack_S = Savings(235762, 10000, "Jack")

    Snorbo_T = Term_deposit(79192, 15000, "Snorbo", 50)

    accounts_dict = {"Jack": Jack, "Snorbo": Snorbo, "Blimbo": Blimbo, "Test": Test, "Jack_S": Jack_S, "Snorbo_T": Snorbo_T}


accounts()
print()
main_line()

while break_ != "y" and break_ != "n":
    break_ = input("Would you like to continue?(y/n): ")
    if break_ == "y":
        break
    else:
        main_line()
