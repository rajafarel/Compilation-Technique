def pythagoras_calculator():
    print("Calculate sides A, B, and C with C being the hypotenuse")
    question = input("Which side would you like to calculate (A, B, C)?: ").upper()

    if question == "A":
        b = int(input("Enter B value: "))
        c = int(input("Enter C value: "))
        a = c ** 2 - b ** 2
        print("The answer for A is", a)

    elif question == "B":
        a = int(input("Enter A value: "))
        c = int(input("Enter C value: "))
        b = c ** 2 - a ** 2
        print("The answer for B is", b)

    elif question == "C":
        a = int(input("Enter A value: "))
        b = int(input("Enter B value: "))
        c = (a ** 2 + b ** 2) ** 0.5
        print("The answer for C is", c)

    else:
        print("Invalid input. Please enter A, B, or C.")


pythagoras_calculator()
