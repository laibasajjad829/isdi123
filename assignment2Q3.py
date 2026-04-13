correct_password = "12345"

attempts = 3

for i in range(1, attempts + 1):
    password = input("Enter password: ")

    if password == correct_password:
        print("Access Granted")
        break
    else:
        remaining = attempts - i
        if remaining == 0:
            print("Account Locked")
        else:
            print("Wrong password! Attempts left:", remaining)