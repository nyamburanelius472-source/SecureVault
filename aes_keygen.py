# Fig 2 - AES Key Generation Process - SecureVault Week 4
# AES supports 128, 192 and 256 bit keys
# Longer key = more combinations = harder to crack

from Crypto.Random import get_random_bytes
import base64
import hashlib

def generate_key(size_bits):
    key = get_random_bytes(size_bits // 8)
    return key

def key_from_password(password, size_bits):
    # Converts a human password into a proper AES key
    return hashlib.sha256(password.encode()).digest()[:size_bits // 8]

print("=" * 50)
print("   SecureVault - AES Key Generation")
print("=" * 50)

for bits in [128, 192, 256]:
    key = generate_key(bits)
    print(f"\n[{bits}-bit Key]")
    print(f"Raw bytes : {key.hex()}")
    print(f"Base64    : {base64.b64encode(key).decode()}")
    print(f"Length    : {len(key)} bytes = {len(key)*8} bits")
    print(f"Possible combinations: 2^{len(key)*8} = astronomically large")

# Password derived key
password = "SecureVault2025"
derived = key_from_password(password, 256)
print(f"\n[Password-Derived Key]")
print(f"Password  : {password}")
print(f"Derived   : {derived.hex()}")
print(f"Length    : {len(derived)*8} bits")
print("\nStatus: Key generation complete.")