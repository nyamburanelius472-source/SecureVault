# Fig 1 - LFSR Generator Implementation - SecureVault Week 3
# LFSR = Linear Feedback Shift Register
# Think of it as a row of switches that keep flipping
# based on their previous positions, generating a sequence

def lfsr(seed, taps, length):
    state = seed
    sequence = []
    
    for _ in range(length):
        # Record current output bit (rightmost bit)
        output_bit = state & 1
        sequence.append(output_bit)
        
        # Calculate feedback by XORing tapped positions
        feedback = 0
        for tap in taps:
            feedback ^= (state >> tap) & 1
        
        # Shift register right and insert feedback at left
        state = (state >> 1) | (feedback << (max(taps)))
    
    return sequence

# Run LFSR with seed and tap positions
seed = 0b1011        # Starting state: 1011 in binary
taps = [3, 1]        # Which positions feed back into the register
length = 20          # How many bits to generate

sequence = lfsr(seed, taps, length)

print("=" * 45)
print("   SecureVault - LFSR Generator")
print("=" * 45)
print(f"\nSeed (starting state) : {bin(seed)} = {seed}")
print(f"Tap positions         : {taps}")
print(f"\nGenerated {length} bits:")
print("".join(map(str, sequence)))
print(f"\nAs numbers: {sequence}")
print(f"Zeros: {sequence.count(0)} | Ones: {sequence.count(1)}")
print("\nStatus: LFSR sequence generated successfully.")