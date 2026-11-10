# Engineering Unit Converter
# ND1 Mechatronics Engineering - YabaTech
# Converts between common engineering units
#form Uche Markathony Somtoo 
#f/nd/25/3450010
# This list will store the history of all conversions
history = []

def show_menu():
    """Show the main menu to the user."""
    print("\n--- Engineering Unit Converter ---")
    print("1. mm to inches")
    print("2. Inches to mm")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. kg to lb")
    print("6. lb to kg")
    print("7. km/h to m/s")
    print("8. m/s to km/h")
    print("9. Metres to Feet (My Twist)")
    print("10. Litres to Gallons (My Twist)")
    print("11. Show History")
    print("12. Quit")

def get_number():
    """Ask the user for a number and check it is valid."""
    try:
        value = float(input("Enter the value to convert: "))
        return value
    except ValueError:
        # If user types a letter, show error instead of crashing
        print("Error: Please enter a number, not a letter.")
        return None

def convert(choice, value):
    """Do the conversion based on the user's choice."""
    if choice == 1:
        result = value / 25.4
        unit = "inches"
    elif choice == 2:
        result = value * 25.4
        unit = "mm"
    elif choice == 3:
        result = (value * 9/5) + 32
        unit = "°F"
    elif choice == 4:
        result = (value - 32) * 5/9
        unit = "°C"
    elif choice == 5:
        result = value * 2.20462
        unit = "lb"
    elif choice == 6:
        result = value / 2.20462
        unit = "kg"
    elif choice == 7:
        result = value / 3.6
        unit = "m/s"
    elif choice == 8:
        result = value * 3.6
        unit = "km/h"
    elif choice == 9:
        result = value * 3.28084
        unit = "feet"
    elif choice == 10:
        result = value * 0.264172
        unit = "gallons"
    else:
        return None

    # Save to history - this is my own twist
    history.append(f"{value} -> {round(result, 2)} {unit}")
    return result, unit

# Main program loop - keeps running until user quits
while True:
    show_menu()

    try:
        choice = int(input("Choose an option (1-12): "))
    except ValueError:
        print("Error: Please enter a number from 1 to 12.")
        continue

    if choice == 12:
        print("\n--- Your Conversion History ---")
        if len(history) == 0:
            print("No conversions done yet.")
        else:
            for item in history:
                print(item)
        print("Thank you for using the converter. Goodbye!")
        break

    elif choice == 11:
        print("\n--- Your Conversion History ---")
        if len(history) == 0:
            print("No conversions yet.")
        else:
            for item in history:
                print(item)

    elif choice >= 1 and choice <= 10:
        value = get_number()
        if value is None:
            continue
        answer = convert(choice, value)
        if answer:
            result, unit = answer
            print(f"Answer: {value} = {round(result, 2)} {unit}")

    else:
        print("Error: Please choose a number between 1 and 12.")
    
 