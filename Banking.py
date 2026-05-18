
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
    


# mainline

def main_line():
    person = input("Enter your name: ")
    while True:
        if person.title() in accounts:
            d_or_w = input("Would you like to withraw or deposit? (w/d) ")
            if d_or_w == "d":
                deposit_num = int(input("How much would you like to deposit? "))
                if deposit_num > 0:
                    print(f"Old balance: {accounts[person.title()].balance}")
                    accounts[person.title()].deposit(deposit_num)
                    print(f"New balance: {accounts[person.title()].balance}")
                else:
                    print("Invalid number")
                    return
            elif d_or_w == "w":
                withdraw_num = int(input("How much would you like to withdraw? "))
                if withdraw_num > 0 and withdraw_num <= accounts[person.title()].balance:
                    print(f"Old balance: {accounts[person.title()].balance}")
                    accounts[person.title()].withdraw(withdraw_num)
                    print(f"New balance: {accounts[person.title()].balance}")
                else:
                    print("Invalid number or insufficient funds")
                    return
            else:
                print("invalid input")
                return
            
            get_interest = float(input("What is your interest rate?(%) "))
            if 100 > get_interest > 0:
                print(f"Old balance: {accounts[person.title()].balance}")
                print("-"*30)
                print(accounts[person.title()].add_interest(get_interest / 100))
                print("-"*30)
                print(f"New balance: {accounts[person.title()].balance}")
                return


        else:
            print("Invalid name")
            return

def accounts():
    global Jack, Snorbo, Blimbo, Test, accounts_dict
    Jack = Account(235761, 720, "Jack")

    Snorbo = Account(79191, 520, "Snorbo")

    Blimbo = Account(10101, 1200, "Blimbo")

    Test = Account(91935, 100, "Test")

    accounts_dict = {"Jack": Jack, "Snorbo": Snorbo, "Blimbo": Blimbo, "Test": Test}


accounts()
print()
main_line()

while break_ != "y" or break_ != "n":
    break_ = input("Would you like to continue?(y/n): ")
    if break_ == "y":
        break
    else:
        main_line()
