CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*?"
SHIFT = 7


def show_menu():
    print()
    print("Secret Message Security Tool")
    print("1. Encode Message")
    print("2. Decode Message")
    print("3. Check Password Strength")
    print("4. Exit")
    print()


def encode_message(message):
    result = ""
    for ch in message:
        if ch in CHARSET:
            index = CHARSET.find(ch)
            new_index = (index + SHIFT) % len(CHARSET)
            result = result + CHARSET[new_index]
        else:
            result = result + ch
    return result


def decode_message(message):
    result = ""
    for ch in message:
        if ch in CHARSET:
            index = CHARSET.find(ch)
            new_index = (index - SHIFT) % len(CHARSET)
            result = result + CHARSET[new_index]
        else:
            result = result + ch
    return result


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "4":
            print("Goodbye")
            break
        elif choice == "1":
            message = input("Enter message to encode: ")
            if message == "":
                print("Message cannot be empty")
            else:
                encoded = encode_message(message)
                print("Secret code: " + encoded)
        elif choice == "2":
            code = input("Enter secret code to decode: ")
            if code == "":
                print("Secret code cannot be empty")
            else:
                decoded = decode_message(code)
                print("Original message: " + decoded)
        elif choice == "3":
            print("Coming soon")
        else:
            print("Invalid choice please try again")


if __name__ == "__main__":
    main()
