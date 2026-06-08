# Fig 5 - Encryption Performance Results - SecureVault Week 3
# Testing how fast and reliable our stream cipher is
# across different message sizes and key lengths

import time
from rc4 import rc4_encrypt, rc4_decrypt

def performance_test(message, key):
    start = time.time()
    encrypted = rc4_encrypt(message, key)
    encrypt_time = time.time() - start
    
    start = time.time()
    decrypted = rc4_decrypt(encrypted, key)
    decrypt_time = time.time() - start
    
    success = message == decrypted
    return encrypt_time, decrypt_time, success

print("=" * 55)
print("   SecureVault - Stream Cipher Performance Testing")
print("=" * 55)

# Test different message sizes
tests = [
    ("Short message", "SecureVault", "VAULT"),
    ("Medium message", "Kali Linux Cryptography System Testing 2025", "SECURE"),
    ("Long message", "Advanced Cryptography BIT4138 " * 10, "SECUREVAULT"),
]

for name, message, key in tests:
    enc_time, dec_time, success = performance_test(message, key)
    print(f"\n[{name}]")
    print(f"Message length : {len(message)} characters")
    print(f"Key used       : {key}")
    print(f"Encrypt time   : {enc_time*1000:.4f} ms")
    print(f"Decrypt time   : {dec_time*1000:.4f} ms")
    print(f"Integrity check: {'PASSED' if success else 'FAILED'}")

print("\n" + "=" * 55)
print("Conclusion: RC4 encrypts and decrypts consistently")
print("regardless of message length. Stream ciphers process")
print("data character by character making them fast and")
print("suitable for real-time secure communication.")