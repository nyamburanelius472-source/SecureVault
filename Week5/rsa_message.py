# Fig 4 - Secure Message Transmission - SecureVault Week 5
# Simulating real secure communication between two parties
# Sender uses receiver's public key, receiver uses private key

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def encrypt_message(message, public_key_path):
    with open(public_key_path, 'r') as f:
        key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(key)
    return base64.b64encode(cipher.encrypt(message.encode())).decode()

def decrypt_message(encrypted, private_key_path):
    with open(private_key_path, 'r') as f:
        key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(base64.b64decode(encrypted)).decode()

messages = [
    "Transfer approved: KES 50,000",
    "Login token: BIT4138-SECURE-2025",
    "Confidential: Exam results released"
]

print("=" * 55)
print("   SecureVault - Secure Message Transmission")
print("=" * 55)

for i, msg in enumerate(messages, 1):
    encrypted = encrypt_message(msg, "public.pem")
    decrypted = decrypt_message(encrypted, "private.pem")
    status = "DELIVERED SECURELY" if msg == decrypted else "FAILED"
    print(f"\n[Message {i}]")
    print(f"Sent     : {msg}")
    print(f"Encrypted: {encrypted[:50]}...")
    print(f"Received : {decrypted}")
    print(f"Status   : {status}")

print("\nConclusion: All messages transmitted and")
print("decrypted successfully using RSA key pair.")