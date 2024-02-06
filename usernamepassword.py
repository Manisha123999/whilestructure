def login():
    correct_username = "Manisha"
    correct_password = "Manisha123"
    attempts = 0

    while attempts < 5:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == correct_username and password == correct_password:
            print("Welcome!")
            return
        attempts += 1
        print("Access denied. Please try again.")

    print("Maximum login attempts exceeded. Access denied.")
login()