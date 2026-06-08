# Caesar Cipher Implementation - SecureVault Week 2

def caesar_encrypt(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Test
message = "SecureVault Cryptography System"
shift = 7
encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("=== Caesar Cipher ===")
print(f"Original : {message}")
print(f"Shift    : {shift}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")