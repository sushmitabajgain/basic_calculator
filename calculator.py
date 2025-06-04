# calculator.py

# Function to add two numbers
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

# Function to divide two numbers
def divide(a, b):
    """
    Return the result of dividing a by b.
    If b is zero, return an error message.
    """
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

# Main function to run the calculator
def calculator():
    """Display menu and perform the selected arithmetic operation."""
    
    # Display a welcome message
    print("\n📱 Basic Calculator")
    print("-----------------------")

    # Show available operations
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Ask user to select an operation
    choice = input("Enter your choice (1/2/3/4): ")

    # Check if the choice is valid
    if choice in ['1', '2', '3', '4']:
        try:
            # Get input numbers from user and convert to float
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            # If input is not a number, show error
            print("❌ Invalid input. Please enter numbers only.")
            return

        # Perform the chosen operation using the corresponding function
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        # Display the result
        print(f"✅ Result: {result}")
    else:
        # If choice is invalid
        print("❌ Invalid choice. Please select from 1 to 4.")

# Run the calculator only if this file is being run directly
if __name__ == "__main__":
    calculator()
