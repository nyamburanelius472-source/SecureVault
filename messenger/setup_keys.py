# SecureVault Messenger - Key Setup
# Generates RSA key pair for the messenger
# Run this once before using the messenger

from Crypto.PublicKey import RSA

def setup_keys():
    print("=" * 50)
    print("   SecureVault Messenger - Key Setup")
    print("=" * 50)
    print("\nGenerating 2048-bit RSA key pair...")
    
    key = RSA.generate(2048)
    
    private_key = key.export_key().decode()
    public_key = key.publickey().export_key().decode()
    
    with open("messenger_private.pem", "w") as f:
        f.write(private_key)
    
    with open("messenger_public.pem", "w") as f:
        f.write(public_key)
    
    print("Private key saved: messenger_private.pem")
    print("Public key saved : messenger_public.pem")
    print("\nIMPORTANT:")
    print("Share messenger_public.pem with anyone who")
    print("wants to send you encrypted messages.")
    print("NEVER share messenger_private.pem with anyone.")
    print("\nStatus: Keys ready. You can now run messenger.py")

setup_keys()