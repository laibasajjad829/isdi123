balance = 1000  # initial balance

def check_balance():
    print("Your current balance is:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Amount deposited successfully!")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Please collect your cash.")

# Main Program
while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        deposit(amount)

    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        withdraw(amount)

    elif choice == "4":
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice! Try again.")