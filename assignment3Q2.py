def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    else:
        return "Invalid Credentials"

# Allow 3 attempts
attempts = 3

for i in range(attempts):
    user = input("Enter username: ")
    pwd = input("Enter password: ")

    result = login(user, pwd)
    print(result)

    if result == "Login Successful":
        break
    else:
        remaining = attempts - (i + 1)
        if remaining == 0:
            print("Account Locked")
        else:
            print("Attempts left:", remaining)
            