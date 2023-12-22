import random
import string

def generate_password(length=12, uppercase=True, digits=True, symbols=True):
    # Define character sets based on complexity options
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if uppercase else ''
    digit_chars = string.digits if digits else ''
    symbol_chars = string.punctuation if symbols else ''

    # Combine character sets
    all_chars = lowercase_chars + uppercase_chars + digit_chars + symbol_chars

    # Ensure the password length is at least 4 characters
    length = max(length, 4)

    # Generate the password
    password = random.sample(all_chars, length)
    password = ''.join(password)

    return password

def main():
    print("Password Generator")
    print("------------------")

    # Get user input for password options
    length = int(input("Enter the password length: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate and print the password
    password = generate_password(length, uppercase, digits, symbols)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
