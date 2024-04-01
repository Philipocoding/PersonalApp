entry = True

while entry:
    answer = input("Login (1) or register(2) - ")
    if answer == "1":
        entry = False
        User.Login()
        break
    if answer == "2":
        User.Register()
        entry = False
        break


    