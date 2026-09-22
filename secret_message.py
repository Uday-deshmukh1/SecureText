from encoder import encode_message
from decoder import decode_message
from password_checker import check_password_strength
from helpers import read_input, is_valid_encoded_text


def show_menu():
    print()
    print("Secret Message Security Tool")
    print("1. Encode Message")
    print("2. Decode Message")
    print("3. Check Password Strength")
    print("4. Exit")
    print()


def main():
    while True:
        show_menu()
        choice = read_input("Enter your choice: ")
        if choice is None:
            break
        if choice == "4":
            print("Goodbye")
            break
        elif choice == "1":
            message = read_input("Enter message to encode: ")
            if message is None:
                break
            if message == "":
                print("Message cannot be empty")
            else:
                encoded = encode_message(message)
                print("Secret code: " + encoded)
                print()
        elif choice == "2":
            code = read_input("Enter secret code to decode: ")
            if code is None:
                break
            if code == "":
                print("Secret code cannot be empty")
            elif not is_valid_encoded_text(code):
                print("Invalid encoded input please check your secret code")
            else:
                decoded = decode_message(code)
                print("Original message: " + decoded)
                print()
        elif choice == "3":
            password = read_input("Enter password to check: ")
            if password is None:
                break
            if password == "":
                print("Password cannot be empty")
            else:
                strength, missing = check_password_strength(password)
                print("Password strength: " + strength)
                if len(missing) > 0:
                    print("Missing requirements:")
                    for item in missing:
                        print("- " + item)
                else:
                    print("All requirements are met")
                print()
        else:
            print("Invalid choice please try again")


if __name__ == "__main__":
    main()
