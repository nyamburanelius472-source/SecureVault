# Fig 4 - Decryption Results - SecureVault Week 4
# Proving that only the correct key can decrypt the message
# Wrong key = garbage output = data protected

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    padded = pad(plaintext.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded)
    return cipher.iv, encrypted

def aes_decrypt(iv, encrypted, key):
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
        return decrypted.decode()
    except Exception:
        return "DECRYPTION FAILED - Wrong key rejected"

message = "Nairobi Kenya Cryptography 2025"
correct_key = get_random_bytes(32)
wrong_key = get_random_bytes(32)

iv, encrypted = aes_encrypt(message, correct_key)

print("=" * 50)
print("   SecureVault - Decryption Results")
print("=" * 50)
print(f"\nOriginal  : {message}")
print(f"\nEncrypted : {encrypted.hex()[:50]}...")

print(f"\n[Attempt 1] Correct key:")
result1 = aes_decrypt(iv, encrypted, correct_key)
print(f"Result    : {result1}")

print(f"\n[Attempt 2] Wrong key:")
result2 = aes_decrypt(iv, encrypted, wrong_key)
print(f"Result    : {result2}")

print("\nConclusion: AES only decrypts with the exact original key.")
print("Status: Decryption validation complete.")