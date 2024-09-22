def ohms_law_calculator():
    choice = input("What do you want to calculate? Voltage (V), Current (I), or Resistance (R)? ")

    if choice.upper() == "V":
        current = float(input("Enter the current (I): "))
        resistance = float(input("Enter the resistance (R): "))
        result = current * resistance
        print(f"The voltage is {result} volts")
    elif choice.upper() == "I":
        voltage = float(input("Enter the voltage (V): "))
        resistance = float(input("Enter the resistance (R): "))
        if resistance == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = voltage / resistance
            print(f"The current is {result} amps")
    elif choice.upper() == "R":
        voltage = float(input("Enter the voltage (V): "))
        current = float(input("Enter the current (I): "))
        if current == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = voltage / current
            print(f"The resistance is {result} ohms")
    else:
        print("Invalid choice. Please try again.")

ohms_law_calculator()