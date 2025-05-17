import random
import string

def generate_password(length):
    if length < 4:
        return "Password length must be at least 4 characters."

    # One character from each category
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # Remaining characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = [random.choice(all_chars) for _ in range(length - 4)]

    # Combine and shuffle
    password_list = [upper, lower, digit, special] + remaining_chars
    random.shuffle(password_list)
    return ''.join(password_list)

# Main program
length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print("Generated Password:", password)
