# Basic Calculator 🧮

This is a simple Python program that performs the four basic arithmetic operations:

- Addition ➕  
- Subtraction ➖  
- Multiplication ✖️  
- Division ➗

## 🚀 How It Works

The calculator:

1. Asks the user to enter two numbers.
2. Prompts the user to choose an operation (add, subtract, multiply, divide).
3. Calls the corresponding function.
4. Displays the result.

## 🧠 Functions Included

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
