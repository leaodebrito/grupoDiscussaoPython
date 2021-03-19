weight = input("What's your weight: ")
unity = input("(L)bs or (K)g: ")


# ".upper()" makes the string  
if unity.upper() == "L":
    pounds = float(weight) * 0.45
    print(f"You're {pounds} pounds ")
elif unity.upper() == "K":
    kilos = float(weight) / 0.45
    print(f"You're {kilos} kilos")
else:
    print("what unity is that?")