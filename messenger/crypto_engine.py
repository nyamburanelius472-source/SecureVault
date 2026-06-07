# SecureVault Messenger - Crypto Engine
# This is the brain that combines all ciphers together
# Flow: Message → Caesar → AES → RSA protects the AES key

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# ===== STEP 1: CAESAR PRE-SCRAMBLER =====
# Scrambles message before AES encryption
def caesar_scramble(text, shift=7):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_unscramble(text, shift=7):
    return caesar_scramble(text, -shift)

# ===== STEP 2: AES MESSAGE ENCRYPTION =====
# Encrypts the scrambled message using AES-256
def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    padded = pad(plaintext.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded)
    return cipher.iv, encrypted

def aes_decrypt(iv, encrypted, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
    return decrypted.decode()

# ===== STEP 3: RSA KEY PROTECTION =====
# RSA encrypts the AES key so only receiver can unlock it
def rsa_encrypt_key(aes_key, public_key_path):
    with open(public_key_path, 'r') as f:
        public_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(public_key)
    return base64.b64encode(cipher.encrypt(aes_key)).decode()

def rsa_decrypt_key(encrypted_key, private_key_path):
    with open(private_key_path, 'r') as f:
        private_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(base64.b64decode(encrypted_key))

# ===== FULL ENCRYPTION PIPELINE =====
def full_encrypt(message, public_key_path):
    # Step 1: Caesar scramble
    scrambled = caesar_scramble(message)
    
    # Step 2: Generate random AES key and encrypt
    aes_key = get_random_bytes(32)
    iv, encrypted_msg = aes_encrypt(scrambled, aes_key)
    
    # Step 3: RSA protect the AES key
    protected_key = rsa_encrypt_key(aes_key, public_key_path)
    
    return {
        "protected_key": protected_key,
        "iv": base64.b64encode(iv).decode(),
        "message": base64.b64encode(encrypted_msg).decode()
    }

# ===== FULL DECRYPTION PIPELINE =====
def full_decrypt(package, private_key_path):
    # Step 1: RSA recover the AES key
    aes_key = rsa_decrypt_key(package["protected_key"], private_key_path)
    
    # Step 2: AES decrypt the message
    iv = base64.b64decode(package["iv"])
    encrypted_msg = base64.b64decode(package["message"])
    scrambled = aes_decrypt(iv, encrypted_msg, aes_key)
    
    # Step 3: Caesar unscramble
    original = caesar_unscramble(scrambled)
    return original

print("Crypto Engine loaded successfully.")
print("Caesar + AES + RSA pipeline ready.")