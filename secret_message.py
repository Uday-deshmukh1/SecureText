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
        if ch == " ":
            result = result + " "
        elif ch in CHARSET:
            index = CHARSET.find(ch)
            new_index = (index + SHIFT) % len(CHARSET)
            result = result + CHARSET[new_index]
        else:
            result = result + ch
    return result


def decode_message(message):
    result = ""
    for ch in message:
        if ch == " ":
            result = result + " "
        elif ch in CHARSET:
            index = CHARSET.find(ch)
            new_index = (index - SHIFT) % len(CHARSET)
            result = result + CHARSET[new_index]
        else:
            result = result + ch
    return result


def check_password_strength(password):
    score = 0
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False
    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_number = True
        elif ch in "!@#$%^&*?":
            has_special = True
    if len(password) >= 8:
        score = score + 1
    if has_upper:
        score = score + 1
    if has_lower:
        score = score + 1
    if has_number:
        score = score + 1
    if has_special:
        score = score + 1
    if score >= 5:
        return "STRONG"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "WEAK"


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
            password = input("Enter password to check: ")
            if password == "":
                print("Password cannot be empty")
            else:
                strength = check_password_strength(password)
                print("Password strength: " + strength)
        else:
            print("Invalid choice please try again")


if __name__ == "__main__":
    main()
