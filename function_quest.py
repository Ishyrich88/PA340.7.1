# The Mighty Calculator
def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero!"

# Test the calculator functions
result = add_numbers(5, 3)
print("The sum is:", result)

result = subtract_numbers(10, 4)
print("The difference is:", result)

result = multiply_numbers(6, 2)
print("The product is:", result)

result = divide_numbers(15, 0)
print("The quotient is:", result)

# The Quest for Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Prompt the user for a number and display the corresponding Fibonacci number
number = int(input("\nEnter a number to find its Fibonacci sequence: "))
print(f"The Fibonacci number at position {number} is: {fibonacci(number)}")

# The Cryptic Decoder
def decode_message(encoded_message, cipher):
    decoded_message = ""
    for letter in encoded_message:
        decoded_message += cipher.get(letter, letter)  # Map encoded letter to plain letter
    return decoded_message

# Example cipher for simple substitution
cipher = {
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 
    'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 
    'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 
    'y': 'b', 'z': 'a'
}

# Prompt the user for an encoded message and display the decoded message
message = input("\nEnter an encoded message to decode: ")
print("Decoded message:", decode_message(message, cipher))

# The Magical Email Validator
import re

def validate_email(email):
    # Regular expression pattern for validating email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    return False

# Prompt the user for an email address and validate it
email = input("\nEnter an email address to validate: ")
if validate_email(email):
    print("Valid email address!")
else:
    print("Invalid email address!")
