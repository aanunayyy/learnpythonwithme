results = []

while True:
    num1 = int(input("Enter the number1: "))
    num2 = int(input("Enter the number2: "))
    print("Choose your operator:\n1) +\n2) -\n3) *\n4) /")
    operators = int(input("Enter choice: "))

    if operators == 1:
        res = num1 + num2
    elif operators == 2:
        res = num1 - num2
    elif operators == 3:
        res = num1 * num2
    elif operators == 4:
        if num2 != 0:
            res = num1 / num2
        else:
            print("Error: Cannot divide by zero.")
            continue
    else:
        print("Invalid operator.")
        continue

    # Store the result
    results.append(res)
    print("Result:", res)
    print("History:", results)

    # Option to continue or exit
    cont = input("Do you want to calculate again? (y/n): ")
    if cont.lower() != 'y':
        break
