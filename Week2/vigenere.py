# Vigenere Cipher Implementation - SecureVault Week 2

def vigenere_encrypt(plaintext, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(ciphertext, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# Test
message = "Kali Linux Security Testing"
key = "VAULT"
encrypted = vigenere_encrypt(message, key)
decrypted = vigenere_decrypt(encrypted, key)

print("=== Vigenere Cipher ===")
print(f"Original : {message}")
print(f"Key      : {key}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")