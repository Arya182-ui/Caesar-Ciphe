def encrypt(text, shift):
    return ''.join(chr((ord(c) - (65 if c.isupper() else 97) + shift) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for c in text)

def decrypt(text, shift):
    return encrypt(text, -shift)

def brute_force_decrypt(text):
    return {shift: decrypt(text, shift) for shift in range(1, 26)}
