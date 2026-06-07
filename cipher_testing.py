# Fig 5 - Cipher Testing Results - SecureVault Week 2

from caesar import caesar_encrypt, caesar_decrypt
from vigenere import vigenere_encrypt, vigenere_decrypt

print("=" * 50)
print("   SecureVault - Cipher Security Testing")
print("=" * 50)

# Test 1: Caesar with multiple shifts
print("\n[TEST 1] Caesar Cipher - Multiple Shifts")
message = "DataSecurity"
for shift in [3, 7, 13]:
    enc = caesar_encrypt(message, shift)
    dec = caesar_decrypt(enc, shift)
    print(f"Shift {shift:2d} | Encrypted: {enc} | Decrypted: {dec}")

# Test 2: Vigenere with different keys
print("\n[TEST 2] Vigenere Cipher - Different Keys")
message = "DataSecurity"
for key in ["KEY", "VAULT", "SECUREVAULT"]:
    enc = vigenere_encrypt(message, key)
    dec = vigenere_decrypt(enc, key)
    print(f"Key: {key:12s} | Encrypted: {enc} | Decrypted: {dec}")

# Test 3: Security weakness demonstration
print("\n[TEST 3] Caesar Weakness - Brute Force")
encrypted = caesar_encrypt("AttackAtDawn", 5)
print(f"Intercepted message: {encrypted}")
print("Trying all 25 shifts...")
for shift in range(1, 26):
    attempt = caesar_decrypt(encrypted, shift)
    if attempt == "AttackAtDawn":
        print(f"CRACKED at shift {shift}: {attempt}")

print("\nConclusion: Caesar cracked in 25 attempts. Vigenere requires")
print(f"26^5 = {26**5:,} attempts for a 5-letter key. Far stronger.")