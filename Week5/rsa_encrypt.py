# Fig 2 - RSA Public Key Encryption - SecureVault Week 5
# Anyone with the public key can encrypt a message
# Only the private key holder can read it

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def rsa_encrypt(message, public_key_path):
    with open(public_key_path, 'r') as f:
        public_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(message.encode())
    return base64.b64encode(encrypted).decode()

message = "SecureVault Confidential: BIT4138 RSA Test"
encrypted = rsa_encrypt(message, "public.pem")

print("=" * 50)
print("   SecureVault - RSA Public Key Encryption")
print("=" * 50)
print(f"\nOriginal message  : {message}")
print(f"Message length    : {len(message)} characters")
print(f"\nEncrypted (base64):")
print(encrypted)
print(f"\nEncrypted length  : {len(encrypted)} characters")
print("\nNote: Only the private key can decrypt this.")
print("Status: RSA encryption successful.")