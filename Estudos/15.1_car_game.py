

car_action = ""
started = False

while True:
    car_action = input("> ").upper()
    if car_action == "START":
        if started:
            print("The car is already started")
        else:
            print("The car started")
            started = True
    elif car_action == "STOP":
        if not started:
            print("The car is already stop")
        else:
            started = False
            print("the car stop")
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