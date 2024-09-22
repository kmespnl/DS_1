def temperature_converter():
    temperature = float(input("Enter a temperature: "))
    conversion_type = input("Do you want to convert from Celsius to Fahrenheit (C-F) or from Fahrenheit to Celsius (F-C)? ")

    if conversion_type.upper() == "C-F":
        result = temperature * 9/5 + 32
        print(f"{temperature}°C is equal to {result}°F")
    elif conversion_type.upper() == "F-C":
        result = (temperature - 32) * 5/9
        print(f"{temperature}°F is equal to {result}°C")
    else:
        print("Invalid conversion type. Please try again.")

temperature_converter()