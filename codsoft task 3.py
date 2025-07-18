import random
import string

def generate_password(length,use_upper=True, use_lower=True,use_digits=True, use_symbols=True):
    characters =''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if not characters:
        return "Please select at least one character type!"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("=== PASSWORD GENERATOR ===")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Length must be greater  than 0.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    print("Select charactre types to include in the password:")
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ") == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    password = generate_password(length,use_upper, use_lower, use_digits, use_symbols)
    print("\nGenerated Password:",password)
if __name__ == "__main__":
    main()
