# Fig 1 - AES Encryption Script - SecureVault Week 4
# AES = Advanced Encryption Standard
# Works like a combination lock with multiple spinning rotors
# Each rotor (round) scrambles data differently using the key

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    padded = pad(plaintext.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded)
    return base64.b64encode(cipher.iv + encrypted).decode()

def aes_decrypt(ciphertext, key):
    raw = base64.b64decode(ciphertext)
    iv = raw[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(raw[16:]), AES.block_size)
    return decrypted.decode()

# Generate secure 256-bit key
key = get_random_bytes(32)
message = "SecureVault AES Encryption Test 2025"

encrypted = aes_encrypt(message, key)
decrypted = aes_decrypt(encrypted, key)

print("=" * 50)
print("   SecureVault - AES Encryption Script")
print("=" * 50)
print(f"\nOriginal  : {message}")
print(f"Key size  : {len(key)*8} bits")
print(f"Encrypted : {encrypted}")
print(f"Decrypted : {decrypted}")
print(f"\nMatch: {'SUCCESS' if message == decrypted else 'FAILED'}")
print("\nStatus: AES encryption operational.")