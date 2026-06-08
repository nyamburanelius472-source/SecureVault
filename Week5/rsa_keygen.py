# Fig 1 - RSA Key Pair Generation - SecureVault Week 5
# RSA uses two mathematically linked keys
# Public key locks the message, private key unlocks it
# Like a mailbox - anyone can drop mail in, only you open it

from Crypto.PublicKey import RSA

def generate_rsa_keys(bits=2048):
    key = RSA.generate(bits)
    private_key = key.export_key().decode()
    public_key = key.publickey().export_key().decode()
    return private_key, public_key, key.n, key.e, key.d

private_key, public_key, n, e, d = generate_rsa_keys(2048)

with open("private.pem", "w") as f:
    f.write(private_key)
with open("public.pem", "w") as f:
    f.write(public_key)

print("=" * 50)
print("   SecureVault - RSA Key Pair Generation")
print("=" * 50)
print(f"\nKey size      : 2048 bits")
print(f"Public exponent (e) : {e}")
print(f"Modulus (n) first 60 digits: {str(n)[:60]}...")
print(f"\nPublic Key (first 3 lines):")
for line in public_key.split('\n')[:3]:
    print(line)
print(f"\nPrivate Key (first 3 lines):")
for line in private_key.split('\n')[:3]:
    print(line)
print(f"\nKeys saved to: public.pem and private.pem")
print("Status: RSA key pair generated successfully.")