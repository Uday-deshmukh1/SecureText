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
