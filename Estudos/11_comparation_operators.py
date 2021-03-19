name = input(print("What's your name: "))

name_characters = len(name)

if name_characters < 3 or name_characters == 3:
    print("Name must be at least 3 characters")
elif name_characters > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")


print(len(name))
