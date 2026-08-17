# A-caesar-cipher-encoder-decoder-in-python
A simple Python command-line tool for encoding and decoding text using the classic Caesar cipher — one of the oldest known encryption techniques, originally used by Julius Caesar to send secret military messages.
Caesar Cipher Encoder/Decoder

A simple Python command-line tool for encoding and decoding text using the classic Caesar cipher — one of the oldest known encryption techniques, originally used by Julius Caesar to send secret military messages.

What is a Caesar Cipher?

A Caesar cipher works by shifting each letter in a message a fixed number of positions down (or up) the alphabet. For example, with a shift of 3:

A -> D    B -> E    C -> F   ...

So HELLO encoded with a shift of 3 becomes KHOOR. Decoding simply reverses the shift. It's a foundational example in cryptography — easy to understand, but also easy to break, which makes it a great starting point for learning about encryption, brute-force attacks, and cybersecurity fundamentals.

Features
Encode — shift text forward to encrypt it
Decode — shift text backward to decrypt it (with a known shift)
Brute-force decode — tries all 25 possible shifts at once, useful when the shift value is unknown (this is how Caesar ciphers are broken in practice)
Preserves letter case (Hello stays capitalized correctly)
Leaves spaces, punctuation, and numbers untouched
Works both interactively (menu-driven) and via command-line arguments
Requirements
Python 3.x (no external libraries needed — uses only the standard library)
Usage
Interactive mode

Run the script with no arguments and follow the on-screen menu:

bash
python caesar_cipher.py
=== Caesar Cipher Encoder/Decoder ===
1) Encode
2) Decode
3) Brute-force decode (try all shifts)
Choose an option (1/2/3):
Command-line mode
bash
# Encode text with a shift of 3
python caesar_cipher.py encode "Hello, World!" 3
# -> Khoor, Zruog!

# Decode text with a shift of 3
python caesar_cipher.py decode "Khoor, Zruog!" 3
# -> Hello, World!

# Brute-force decode (unknown shift)
python caesar_cipher.py brute "Khoor, Zruog!"
# -> prints all 25 possible shifts so you can spot the readable one
Example
Choose an option (1/2/3): 1
Enter text: Attack at Dawn
Enter shift value (integer): 5
Encoded: Fyyfhp fy Ifbs
Choose an option (1/2/3): 3
Enter text: Khoor, Zruog!
Shift  3: Hello, World!   <-- readable result reveals the shift
Project Context

This script is part of a personal Cybersecurity learning project, exploring classic ciphers and cryptographic concepts as a foundation before moving on to more advanced encryption and security topics.

Possible Next Steps
Add a --file option to encode/decode entire text files
Implement a Vigenère cipher (multi-letter key version of Caesar)
Add frequency analysis to auto-detect the most likely shift in brute-force mode
Add unit tests
License

Free to use and modify for learning purposes.
