# Calculate powers in recursive method:

# Define calculate powers function
def calculate_powers(base, power):
    if power != 0:
        return base * calculate_powers(base, power - 1)
    else:
        return 1

# Get the user input of base and power
try:
    entered_base = int(input("Enter the base number: "))
    entered_power = int(input("Enter the power: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()
except:
    print("Something went wrong. Exiting the program.")
    exit()

# Call the function
result = calculate_powers(entered_base, entered_power)

# Print the result
print(f"{entered_base}^{entered_power} = {result}")
