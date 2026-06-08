# Fig 5 - AES Performance Testing - SecureVault Week 4
# Testing AES speed across different key sizes and message lengths

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import time

def aes_test(message, key):
    start = time.time()
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = cipher.iv
    enc_time = time.time() - start

    start = time.time()
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher2.decrypt(encrypted), AES.block_size)
    dec_time = time.time() - start

    success = message == decrypted.decode()
    return enc_time, dec_time, success, len(encrypted)

print("=" * 55)
print("   SecureVault - AES Performance Testing")
print("=" * 55)

messages = [
    ("Short  ", "SecureVault 2025"),
    ("Medium ", "Kali Linux AES Cryptography Testing BIT4138"),
    ("Long   ", "Advanced Cryptography SecureVault System " * 10),
]

for key_bits in [128, 256]:
    key = get_random_bytes(key_bits // 8)
    print(f"\n[AES-{key_bits}]")
    print(f"{'Message':<10} {'Size':>6} {'Enc(ms)':>10} {'Dec(ms)':>10} {'Status':>8}")
    print("-" * 50)
    for label, msg in messages:
        enc_t, dec_t, ok, size = aes_test(msg, key)
        print(f"{label} {len(msg):>6} chars {enc_t*1000:>8.4f}ms {dec_t*1000:>8.4f}ms {'OK' if ok else 'FAIL':>6}")

print("\nConclusion: AES-256 provides stronger security than")
print("AES-128 with minimal performance difference.")
print("Status: Performance testing complete.")