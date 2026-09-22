# Secret Message Security Tool

A beginner-level Python project for encoding and decoding secret messages and checking password strength.

This is an educational encoding project. It is not a professional encryption system.

## What it does

The program runs in the terminal and gives three options:

1. Encode Message - turn a normal message into a secret code
2. Decode Message - turn a secret code back into the original message
3. Check Password Strength - rate a password as WEAK, MEDIUM, or STRONG

## Features

- Simple terminal menu that keeps running until you choose Exit
- Encode messages with uppercase letters, lowercase letters, numbers, spaces, and common symbols
- Decode any message that was encoded by this program
- Spaces are preserved during encoding and decoding
- Unsupported characters are kept unchanged instead of causing an error
- Password strength checker with missing requirement feedback
- Handles empty input, invalid menu choices, and invalid encoded input without crashing

## How the encoding works

The program uses one character set:

```
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*?
```

Each character has a position in this set. Encoding adds a fixed shift of 7 to the position. Decoding subtracts the same shift of 7.

Example:

```
A -> position 0
0 + 7 = 7
character at position 7 is H
so A becomes H
```

To decode:

```
H -> position 7
7 - 7 = 0
character at position 0 is A
so H becomes A
```

Because encoding adds the shift and decoding subtracts it, the process is fully reversible.

Spaces and unsupported characters are left unchanged so the original message can be rebuilt exactly.

## Password checking logic

The checker gives one point for each condition met:

1. Minimum length of 8 characters
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one number
5. At least one special character from `!@#$%^&*?`

Scoring:

- 0 to 2 points -> WEAK
- 3 to 4 points -> MEDIUM
- 5 points -> STRONG

The program also lists which requirements are missing.

## How to run

Make sure you have Python installed. Then run:

```
python secret_message.py
```

## Example usage

```
Secret Message Security Tool
1. Encode Message
2. Decode Message
3. Check Password Strength
4. Exit

Enter your choice: 1
Enter message to encode: Hello World
Secret code: Olssv dvysk

Enter your choice: 2
Enter secret code to decode: Olssv dvysk
Original message: Hello World

Enter your choice: 3
Enter password to check: Hello@123
Password strength: STRONG
All requirements are met

Enter your choice: 4
Goodbye
```

More test results:

| Original | Encoded |
|---|---|
| Hello | Olssv |
| Meet me at 5 PM | Tll0 tl h0 # WT |
| Python is fun! | W50ovu pz m1u* |
| 12345 | 89!@# |
| @Hello#2026 | ?OlssvA979$ |

## Limitations

- This is an educational encoding project, not real encryption
- The shift value is fixed and known, so anyone can decode the message
- Do not use this to protect real secrets or sensitive data
- No database, no API, no GUI, and no external libraries are used
- Characters outside the supported set are passed through unchanged

## Project structure

```
Secret-Message-Security/
  secret_message.py
  README.md
```
