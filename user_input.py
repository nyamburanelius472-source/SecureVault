# Fig 4 - User Input Validation Interface - SecureVault Week 2

from caesar import caesar_encrypt, caesar_decrypt
from vigenere import vigenere_encrypt, vigenere_decrypt

print("=" * 45)
print("     SecureVault - Cipher Selection Menu")
print("=" * 45)

# Step 1: Get message from user
message = input("\nEnter your message: ")

# Step 2: Ask which cipher
print("\nChoose cipher:")
print("1. Caesar Cipher")
print("2. Vigenere Cipher")
choice = input("Enter 1 or 2: ")

# Step 3: Run chosen cipher
if choice == "1":
    encrypted = caesar_encrypt(message, 7)
    decrypted = caesar_decrypt(encrypted, 7)
    print("\n--- Caesar Cipher Result ---")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

elif choice == "2":
    key = input("Enter your keyword (letters only): ")
    encrypted = vigenere_encrypt(message, key)
    decrypted = vigenere_decrypt(encrypted, key)
    print("\n--- Vigenere Cipher Result ---")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")

else:
    print("Invalid choice. Please enter 1 or 2.")