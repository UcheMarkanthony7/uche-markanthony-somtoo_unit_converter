# Engineering Unit Converter

## What it does
This program converts between common engineering units such as mm and inches, °C and °F, kg and lb, and km/h and m/s. The user picks an option from a menu, enters a value, and gets the answer with the correct unit. The program keeps running until the user chooses to quit.

## How to run it
Install Python 3, then run: python unit_converter.py

## Sample output
--- Engineering Unit Converter ---
1. mm to inches
2. Inches to mm
3. Celsius to Fahrenheit
...
Choose an option (1-12): 1
Enter the value to convert: 25.4
Answer: 25.4 = 1.0 inches

## My own twist
I added a Conversion History feature that saves every conversion and shows it when you quit or choose option 11. I also added two extra conversions that were not in the brief: Metres to Feet and Litres to Gallons.

## What I learned
I learned how to use functions, loops and if/elif/else to build a menu program. I also learned how to handle wrong input with try/except so the program does not crash when a user types a letter.
