import string
import secrets

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    characters = letters + digits

    password_chars = []

    password_chars.append(secrets.choice(digits))

    for i in range(length - 1):
        password_chars.append(secrets.choice(characters))

    # Shuffle so the guaranteed number isn't always in the same position
    secrets.SystemRandom().shuffle(password_chars)

    password = ''.join(password_chars)
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Invalid Data")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid Data")

if __name__ == "__main__":
    main()