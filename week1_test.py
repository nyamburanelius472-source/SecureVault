from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = b"SecureVault BIT4138 - Environment Verified"
encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print("=== SecureVault Environment Test ===")
print(f"Original : {message.decode()}")
print(f"Encrypted: {encrypted.decode()}")
print(f"Decrypted: {decrypted.decode()}")
print("Status: All cryptography libraries working correctly.")