# Encryption and Decryption Output Comparison - SecureVault Week 2

from caesar import caesar_encrypt, caesar_decrypt
from vigenere import vigenere_encrypt, vigenere_decrypt

message = "Cryptography Protects Digital Systems"

print("=" * 50)
print("   SecureVault - Encryption Output Comparison")
print("=" * 50)

# Caesar
caesar_enc = caesar_encrypt(message, 7)
caesar_dec = caesar_decrypt(caesar_enc, 7)
print("\n--- Caesar Cipher ---")
print(f"Original : {message}")
print(f"Encrypted: {caesar_enc}")
print(f"Decrypted: {caesar_dec}")

# Vigenere
vig_enc = vigenere_encrypt(message, "VAULT")
vig_dec = vigenere_decrypt(vig_enc, "VAULT")
print("\n--- Vigenere Cipher ---")
print(f"Original : {message}")
print(f"Encrypted: {vig_enc}")
print(f"Decrypted: {vig_dec}")

print("\n--- Comparison ---")
print(f"Caesar produced : {len(set(caesar_enc.replace(' ','')))} unique characters")
print(f"Vigenere produced: {len(set(vig_enc.replace(' ','')))} unique characters")
print("\nVigenere produces more character variety = stronger encryption")