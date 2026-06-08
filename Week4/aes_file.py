# Fig 3 - File Encryption Demonstration - SecureVault Week 4
# Encrypting an actual file using AES
# Like putting a document in a locked safe

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import os

def encrypt_file(content, key):
    cipher = AES.new(key, AES.MODE_CBC)
    padded = pad(content.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded)
    return cipher.iv, encrypted

def decrypt_file(iv, encrypted, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
    return decrypted.decode()

# Create a sample text file
original_content = """SecureVault Confidential Document
Student: Nelius
Unit: BIT4138 Advanced Cryptography
Content: This file is protected using AES-256 encryption."""

with open("document.txt", "w") as f:
    f.write(original_content)

key = get_random_bytes(32)
iv, encrypted = encrypt_file(original_content, key)

with open("document.enc", "wb") as f:
    f.write(iv + encrypted)

decrypted = decrypt_file(iv, encrypted, key)

print("=" * 50)
print("   SecureVault - File Encryption Demo")
print("=" * 50)
print(f"\nOriginal file size : {len(original_content)} bytes")
print(f"Encrypted size     : {len(encrypted)} bytes")
print(f"\nOriginal content:\n{original_content}")
print(f"\nEncrypted (hex): {encrypted.hex()[:60]}...")
print(f"\nDecrypted content:\n{decrypted}")
print("\nStatus: File encrypted and decrypted successfully.")