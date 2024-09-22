def convert_length(value, from_unit, to_unit):
    # Dictionary to store conversion factors for length units
    length_units = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.34
    }
    # Check if the input units are valid
    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("Invalid length unit")
    
    # Convert the input value to meters and then to the target unit
    meters = value * length_units[from_unit]
    return meters / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    # Dictionary to store conversion factors for weight units
    weight_units = {
        'grams': 1,
        'kilograms': 1000,
        'milligrams': 0.001,
        'pounds': 453.592,
        'ounces': 28.3495
    }
    # Check if the input units are valid
    if from_unit not in weight_units or to_unit not in weight_units:
        raise ValueError("Invalid weight unit")
    
    # Convert the input value to grams and then to the target unit
    grams = value * weight_units[from_unit]
    return grams / weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    # Convert temperature based on input and output units
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
    raise ValueError("Invalid temperature unit")

def main():
    print("Welcome to the Unit Converter!")
    
    while True:
        # Prompt user to select conversion type
        print("\nSelect conversion type:")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")
        
        if choice == '1':
            # Length conversion
            from_unit = input("Enter from unit: ").strip().lower()
            to_unit = input("Enter to unit: ").strip().lower()
            value = float(input("Enter value: "))
            try:
                result = convert_length(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result} {to_unit}")
            except ValueError as e:
                print(e)
        
        elif choice == '2':
            # Weight conversion
            from_unit = input("Enter from unit: ").strip().lower()
            to_unit = input("Enter to unit: ").strip().lower()
            value = float(input("Enter value: "))
            try:
                result = convert_weight(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result} {to_unit}")
            except ValueError as e:
                print(e)
        
        elif choice == '3':
            # Temperature conversion
            from_unit = input("Enter from unit: ").strip().lower()
            to_unit = input("Enter to unit: ").strip().lower()
            value = float(input("Enter value: "))
            try:
                result = convert_temperature(value, from_unit, to_unit)
                print(f"{value} {from_unit} = {result} {to_unit}")
            except ValueError as e:
                print(e)
        
        elif choice == '4':
            # Exit the program
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
