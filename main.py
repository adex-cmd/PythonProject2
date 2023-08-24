def login():
    print("Login to our store:")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open('users.txt', 'r') as f:
        for line in f:
            u, p = line.strip().split()
            if u == username and p == password:
                print("Login successful")
                return
    print("Invalid username or password")


def sign_up():
    print("Sign up to our store:")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    confirm_password = input("Confirm your password: ")

    if password != confirm_password:
        print("Passwords do not match")
        return

    with open('users.txt', 'a') as f:
        f.write(f"{username} {password}\n")
        print("Sign up successful")


while True:
    print("""
    Login / Sign up
    """)
    choice = input("Enter your choice: ")
    if choice.lower() == "login":
        login()
        break
    elif choice.lower() == "sign up":
        sign_up()
        break
    else:
        print("Invalid choice")
