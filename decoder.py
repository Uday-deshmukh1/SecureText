from utils import CHARSET, SHIFT


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
