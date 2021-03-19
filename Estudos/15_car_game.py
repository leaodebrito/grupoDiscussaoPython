
car_action = ""

while car_action != "QUIT":
    car_action = input("> ").upper()
    if car_action == "START":
        print("The car has started")
    elif car_action == "STOP":
        print("the car has stop")
    elif car_action == "QUIT":
        print("Quiting game")
        break
    elif car_action == "HELP":
        print("""
        Start - Starts the car
        Stop - Stops the car
        Quit - quit game
        """)
    else:
        print("I don't understand")