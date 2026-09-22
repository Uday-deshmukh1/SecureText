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
        choice = input("Enter your choice: ")
        if choice == "4":
            print("Goodbye")
            break
        elif choice in ("1", "2", "3"):
            print("Coming soon")
        else:
            print("Invalid choice please try again")


if __name__ == "__main__":
    main()
