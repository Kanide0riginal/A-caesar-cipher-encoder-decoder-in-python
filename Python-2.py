#!/usr/bin/env python3
import sys
import string
 
 
def shift_char(char: str, shift: int) -> str:
    """Shift a single character by `shift` positions, preserving case."""
    if char in string.ascii_lowercase:
        base = ord('a')
        return chr((ord(char) - base + shift) % 26 + base)
    elif char in string.ascii_uppercase:
        base = ord('A')
        return chr((ord(char) - base + shift) % 26 + base)
    else:
        return char
 
 
def caesar_encode(text: str, shift: int) -> str:
    """Encode text using a Caesar cipher with the given shift."""
    return ''.join(shift_char(c, shift) for c in text)
 
 
def caesar_decode(text: str, shift: int) -> str:
    """Decode text that was encoded with the given shift."""
    return ''.join(shift_char(c, -shift) for c in text)
 
 
def brute_force(text: str) -> None:
    """Print all 25 possible decodings, useful when the shift is unknown."""
    for shift in range(1, 26):
        print(f"Shift {shift:2d}: {caesar_decode(text, shift)}")
 
 
def interactive_mode() -> None:
    print("=== Caesar Cipher Encoder/Decoder ===")
    print("1) Encode")
    print("2) Decode")
    print("3) Brute-force decode (try all shifts)")
    choice = input("Choose an option (1/2/3): ").strip()
 
    text = input("Enter text: ")
 
    if choice == "3":
        brute_force(text)
        return
 
    try:
        shift = int(input("Enter shift value (integer): ").strip())
    except ValueError:
        print("Error: shift must be an integer.")
        sys.exit(1)
 
    if choice == "1":
        print("Encoded:", caesar_encode(text, shift))
    elif choice == "2":
        print("Decoded:", caesar_decode(text, shift))
    else:
        print("Invalid choice.")
        sys.exit(1)
 
 
def main() -> None:
    args = sys.argv[1:]
 
    if not args:
        interactive_mode()
        return
 
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)
 
    mode = args[0].lower()
 
    if mode == "brute" and len(args) == 2:
        brute_force(args[1])
        return
 
    if len(args) != 3:
        print(__doc__)
        sys.exit(1)
 
    mode, text, shift_str = args
    try:
        shift = int(shift_str)
    except ValueError:
        print("Error: shift must be an integer.")
        sys.exit(1)
 
    if mode == "encode":
        print(caesar_encode(text, shift))
    elif mode == "decode":
        print(caesar_decode(text, shift))
    else:
        print(f"Unknown mode: {mode}")
        print(__doc__)
        sys.exit(1)
 
 
if __name__ == "__main__":
    main()