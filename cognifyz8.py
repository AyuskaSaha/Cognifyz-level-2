import re

def password_strength_checker(password):
    # Define the criteria for password strength
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Check all criteria
    if all([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria]):
        return "Strong"
    elif all([length_criteria, (lowercase_criteria or uppercase_criteria), digit_criteria]):
        return "Moderate"
    else:
        return "Weak"

def main():
    password = input("Enter a password to check its strength: ")
    strength = password_strength_checker(password)
    print(f"The password strength is: {strength}")

if __name__ == "__main__":
    main()
