class BankAccount:
    accNumStart = 1000
    accList = []

    def __init__(self, name: str, money=0):
        BankAccount.accNumStart += 1
        self.accountNum = BankAccount.accNumStart
        self.name = name
        self.money = money
        BankAccount.accList.append(self)

    def deposit(self, amount):
        if amount > 0:
            self.money += amount
            print(f"Deposited ${amount}. New balance: ${self.money}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.money:
            self.money -= amount
            print(f"Withdrew ${amount}. New balance: ${self.money}")
        elif amount > self.money:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account Number: {self.accountNum}\nName: {self.name}\nBalance: ${self.money}")

# Main loop
while True:
    print("\nOptions:")
    print("1. Create Account")
    print("2. Display Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        name = input("Enter your name: ")
        account = BankAccount(name)
        print(f"Account created successfully. Your account number is {account.accountNum}")

    elif choice == 2:
        acc_num = int(input("Enter your account number: "))
        account = next((acc for acc in BankAccount.accList if acc.accountNum == acc_num), None)
        if account:
            account.display_balance()
        else:
            print("Invalid account number.")

    elif choice == 3:
        acc_num = int(input("Enter your account number: "))
        account = next((acc for acc in BankAccount.accList if acc.accountNum == acc_num), None)
        if account:
            amount_to_deposit = float(input("Enter amount to deposit: $"))
            account.deposit(amount_to_deposit)
        else:
            print("Invalid account number.")

    elif choice == 4:
        acc_num = int(input("Enter your account number: "))
        account = next((acc for acc in BankAccount.accList if acc.accountNum == acc_num), None)
        if account:
            amount_to_withdraw = float(input("Enter amount to withdraw: $"))
            account.withdraw(amount_to_withdraw)
        else:
            print("Invalid account number.")

    elif choice == 5:
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
