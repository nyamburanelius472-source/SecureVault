# SecureVault Messenger - Main Application
# End-to-End Encrypted Communication Terminal
# Combines Caesar + AES + RSA into one messenger

import json
import os
from datetime import datetime
from crypto_engine import full_encrypt, full_decrypt

def clear():
    os.system('clear')

def print_header():
    print("=" * 55)
    print("      SecureVault Messenger v1.0")
    print("      End-to-End Encrypted Terminal")
    print("=" * 55)

def send_message():
    print("\n--- SEND ENCRYPTED MESSAGE ---")
    sender = input("Your name: ")
    message = input("Type your message: ")
    
    print("\nEncrypting message...")
    print("Step 1: Caesar cipher scrambling...")
    print("Step 2: AES-256 encrypting...")
    print("Step 3: RSA protecting AES key...")
    
    package = full_encrypt(message, "messenger_public.pem")
    
    # Add metadata
    package["sender"] = sender
    package["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save to file (simulates sending)
    filename = f"message_{sender}_{datetime.now().strftime('%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(package, f, indent=2)
    
    print("\n" + "=" * 55)
    print("MESSAGE ENCRYPTED AND SENT SUCCESSFULLY")
    print("=" * 55)
    print(f"Sender    : {sender}")
    print(f"Timestamp : {package['timestamp']}")
    print(f"Saved to  : {filename}")
    print(f"\nEncrypted preview:")
    print(f"{package['message'][:60]}...")
    print("\nMessage is unreadable without the private key.")

def receive_message():
    print("\n--- RECEIVE AND DECRYPT MESSAGE ---")
    
    # Find available message files
    messages = [f for f in os.listdir('.') if f.startswith('message_') and f.endswith('.json')]
    
    if not messages:
        print("No encrypted messages found.")
        return
    
    print("\nAvailable encrypted messages:")
    for i, msg in enumerate(messages, 1):
        print(f"{i}. {msg}")
    
    choice = input("\nEnter message number to decrypt: ")
    
    try:
        filename = messages[int(choice) - 1]
        with open(filename, 'r') as f:
            package = json.load(f)
        
        print("\nDecrypting message...")
        print("Step 1: RSA recovering AES key...")
        print("Step 2: AES-256 decrypting...")
        print("Step 3: Caesar unscrambling...")
        
        decrypted = full_decrypt(package, "messenger_private.pem")
        
        print("\n" + "=" * 55)
        print("MESSAGE DECRYPTED SUCCESSFULLY")
        print("=" * 55)
        print(f"From      : {package['sender']}")
        print(f"Timestamp : {package['timestamp']}")
        print(f"Message   : {decrypted}")
        print("=" * 55)
        
    except Exception as e:
        print(f"Decryption failed: {e}")

def show_encryption_demo():
    print("\n--- LIVE ENCRYPTION DEMO ---")
    message = input("Enter any message to see encryption layers: ")
    
    from crypto_engine import caesar_scramble, aes_encrypt, get_random_bytes
    from Crypto.Random import get_random_bytes
    
    # Show each layer
    step1 = caesar_scramble(message)
    aes_key = get_random_bytes(32)
    iv, step2 = aes_encrypt(step1, aes_key)
    
    import base64
    print("\n" + "=" * 55)
    print("ENCRYPTION LAYERS REVEALED")
    print("=" * 55)
    print(f"Original  : {message}")
    print(f"After Caesar : {step1}")
    print(f"After AES    : {base64.b64encode(step2).decode()[:50]}...")
    print(f"\nEach layer adds protection.")
    print("Without all three keys, decryption is impossible.")

def main():
    clear()
    print_header()
    
    while True:
        print("\nMAIN MENU")
        print("1. Send encrypted message")
        print("2. Receive and decrypt message")
        print("3. Live encryption demo")
        print("4. Exit")
        
        choice = input("\nChoose option (1-4): ")
        
        if choice == "1":
            send_message()
        elif choice == "2":
            receive_message()
        elif choice == "3":
            show_encryption_demo()
        elif choice == "4":
            print("\nSecureVault Messenger closed.")
            print("All messages remain encrypted.")
            break
        else:
            print("Invalid choice. Enter 1, 2, 3 or 4.")

main()