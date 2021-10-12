def player_age():
    while True:
        Age = input("How old are you? ")
        try:
            checker = int(Age)
            if checker >= 18 :
                print("Nice to meet you!")
                break
            else:
                print("You're a bit young aren't you?")
        except ValueError:
            print("Amount must be a number, try again")
    return checker
player_age()