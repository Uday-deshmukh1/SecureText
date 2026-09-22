from utils import CHARSET


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
