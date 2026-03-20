import hashlib

def encrypt(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_password():
    website = input("Enter Website: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    encrypted = encrypt(password)

    with open("passwords.txt", "a") as f:
        f.write(f"{website},{username},{encrypted}\n")

    print("Saved Successfully ✅")

def view_passwords():
    with open("passwords.txt", "r") as f:
        for line in f:
            print(line.strip())

while True:
    print("\n1. Save Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        save_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        break
import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits + "@#$%"
    password = ''.join(random.choice(chars) for _ in range(10))
    print("Generated Password:", password)
