import random
import string

def generate_password(length=12):
    """Generate a strong and secure random password."""
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure minimum length requirements for each character set
    min_lowercase = 1
    min_uppercase = 1
    min_digits = 1
    min_special = 1

    # Ensure the total length of password is at least 'length'
    min_length = min_lowercase + min_uppercase + min_digits + min_special
    if length < min_length:
        raise ValueError(f"Password length must be at least {min_length}")

    # Generate random characters for each character set
    password = (
        ''.join(random.choices(lowercase_letters, k=min_lowercase)) +
        ''.join(random.choices(uppercase_letters, k=min_uppercase)) +
        ''.join(random.choices(digits, k=min_digits)) +
        ''.join(random.choices(special_characters, k=min_special)) +
        ''.join(random.choices(
            lowercase_letters + uppercase_letters + digits + special_characters,
            k=length - min_length
        ))
    )

    # Shuffle the password to make it more secure
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def main():
    print("Welcome to the Strong Password Generator!")
    while True:
        try:
            length = int(input("Enter the length of the password you want to generate (default is 12): "))
            if length <= 0:
                print("Length must be a positive integer. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    try:
        password = generate_password(length)
        print(f"Your strong and secure random password is: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
