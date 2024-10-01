'''
A teacher named Mrs. Rivera who loved making math fun for her students. 
One day, a student named Mia asked how to calculate powers, like (2^7). 
Mrs. Rivera explained, “Imagine you need to multiply 2 by itself seven times. 
We can solve this using a python code utilizing  special method called recursion 
to solve this,” Can you help the class of Mrs. Rivera by providing the recursive 
method to calculate powers?
'''

# pseudocode

# code here
# Get user input of base and power
entered_base = int(input("Enter the base number: "))
entered_power = int(input("Enter the power: "))

# Define calculate powers function
def calculate_powers(base, power):
    if power != 0:
        return base * calculate_powers(base, power - 1)
    else:
        return 1

# Call the function
result = calculate_powers(entered_base, entered_power)
# Print the result
print(f"{entered_base}^{entered_power} = {result}")
