# Fig 4 - RC4 Stream Cipher Simulation - SecureVault Week 3
# RC4 works like a deck of cards being shuffled using a key
# Then cards are drawn one by one to encrypt each character

def rc4_setup(key):
    # Initialize deck of 256 cards in order
    S = list(range(256))
    j = 0
    key_bytes = [ord(c) for c in key]
    
    # Shuffle deck using the key
    for i in range(256):
        j = (j + S[i] + key_bytes[i % len(key_bytes)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def rc4_encrypt(plaintext, key):
    S = rc4_setup(key)
    i = j = 0
    result = []
    
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream_byte = S[(S[i] + S[j]) % 256]
        encrypted_byte = ord(char) ^ keystream_byte
        result.append(encrypted_byte)
    return result

def rc4_decrypt(encrypted_bytes, key):
    S = rc4_setup(key)
    i = j = 0
    result = ""
    
    for byte in encrypted_bytes:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream_byte = S[(S[i] + S[j]) % 256]
        result += chr(byte ^ keystream_byte)
    return result

# Test
message = "SecureVault Stream Cipher"
key = "VAULT2025"

encrypted = rc4_encrypt(message, key)
decrypted = rc4_decrypt(encrypted, key)

print("=" * 50)
print("   SecureVault - RC4 Stream Cipher Simulation")
print("=" * 50)
print(f"\nOriginal  : {message}")
print(f"Key       : {key}")
print(f"\nEncrypted bytes: {encrypted}")
print(f"Hex values     : {[hex(b) for b in encrypted]}")
print(f"\nDecrypted : {decrypted}")
print(f"\nMatch: {'SUCCESS' if message == decrypted else 'FAILED'}")
print("\nStatus: RC4 stream cipher operational.")