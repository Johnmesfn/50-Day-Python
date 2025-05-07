from math import sqrt
import ast

# Function from File 1
def divide_or_square(num):
    """
    If num is divisible by 5, return its square root.
    Otherwise, return num modulo 5.
    """
    if num % 5 == 0:
        return sqrt(num)
    else:
        return num % 5

# Function from File 2
def longest_value(dict):
    """
    Return the longest value in a dictionary.
    """
    return max(dict.values(), key=len)

def main():
    print("Select an option:")
    print("1. Run divide_or_square from File 1")
    print("2. Run longest_value from File 2")
    
    try:
        choice = int(input("Enter your choice (1 or 2): "))
        
        if choice == 1:
            try:
                num = int(input("Please enter a number: "))
                result = divide_or_square(num)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        elif choice == 2:
            try:
                dict_input = input("Please enter a dictionary (e.g., {'a': 'apple', 'b': 'banana'}): ")
                dict = ast.literal_eval(dict_input)
                result = longest_value(dict)
                print(f"The longest value is: {result}")
            except (SyntaxError, ValueError):
                print("Invalid input. Please enter a valid dictionary.")
        
        else:
            print("Invalid choice. Please choose 1 or 2.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the choice.")

if __name__ == "__main__":
    main()
