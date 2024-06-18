import random
import string

S1 = string.ascii_lowercase
S2 = string.ascii_uppercase
S3 = string.digits
S4 = string.punctuation

def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    char_pool = S1
    if use_upper:
        char_pool += S2
    if use_digits:
        char_pool += S3
    if use_symbols:
        char_pool += S4

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in S4 for c in password)
    
    categories = [has_upper, has_lower, has_digit, has_symbol]
    score = sum(categories)

    if len(password) >= 8:
        return "Strong Password"
    elif len(password) <= 5:
        return "Weak Passowrd"
    elif score > 5 and score < 8 :
        return "Moderate Password"
    else:
        return "Weak Password"

def main():
    print("Welcome to your Password Generator!")

    length = int(input("Enter the your desired password length: "))
    use_upper = input("Do you want to include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Do you want to include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Do you want to include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    strength = password_strength(password)
    
    print(f"the Generated Password is: {password}")
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
