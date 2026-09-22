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
    missing = []
    if len(password) >= 8:
        score = score + 1
    else:
        missing.append("minimum length 8")
    if has_upper:
        score = score + 1
    else:
        missing.append("uppercase letter")
    if has_lower:
        score = score + 1
    else:
        missing.append("lowercase letter")
    if has_number:
        score = score + 1
    else:
        missing.append("number")
    if has_special:
        score = score + 1
    else:
        missing.append("special character")
    if score >= 5:
        strength = "STRONG"
    elif score >= 3:
        strength = "MEDIUM"
    else:
        strength = "WEAK"
    return strength, missing


def read_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        print()
        return ""
    except KeyboardInterrupt:
        print()
        print("Goodbye")
        return None


def is_valid_encoded_text(text):
    for ch in text:
        if ch != " " and ch not in CHARSET:
            return False
    return True


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
        else:
            print("Invalid choice please try again")


if __name__ == "__main__":
    main()
