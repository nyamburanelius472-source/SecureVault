# Fig 3 - RSA Private Key Decryption - SecureVault Week 5
# Only the private key can unlock what the public key locked
# Proving asymmetric encryption works correctly

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from rsa_encrypt import rsa_encrypt
import base64

def rsa_decrypt(encrypted_b64, private_key_path):
    with open(private_key_path, 'r') as f:
        private_key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(private_key)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_b64))
    return decrypted.decode()

message = "SecureVault Confidential: BIT4138 RSA Test"
encrypted = rsa_encrypt(message, "public.pem")
decrypted = rsa_decrypt(encrypted, "private.pem")

print("=" * 50)
print("   SecureVault - RSA Private Key Decryption")
print("=" * 50)
print(f"\nEncrypted (first 60 chars): {encrypted[:60]}...")
print(f"\nDecrypted message : {decrypted}")
print(f"Match             : {'SUCCESS' if message == decrypted else 'FAILED'}")
print("\nConclusion: Private key successfully unlocked")
print("the message encrypted with the public key.")
print("Status: RSA decryption complete.")