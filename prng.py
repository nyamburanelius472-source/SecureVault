# Fig 2 - Pseudorandom Sequence Output - SecureVault Week 3
# LCG = Linear Congruential Generator
# Formula: next = (multiplier * current + increment) % modulus
# Like a mathematical recipe that keeps producing new numbers

def lcg(seed, multiplier, increment, modulus, length):
    sequence = []
    current = seed
    for _ in range(length):
        current = (multiplier * current + increment) % modulus
        sequence.append(current)
    return sequence

# Standard parameters used in real systems
seed = 42
multiplier = 1664525
increment = 1013904223
modulus = 2**32

sequence = lcg(seed, multiplier, increment, modulus, 10)

print("=" * 45)
print("   SecureVault - Pseudorandom Sequence Output")
print("=" * 45)
print(f"\nSeed       : {seed}")
print(f"Multiplier : {multiplier}")
print(f"Modulus    : {modulus:,}")
print(f"\nGenerated 10 pseudorandom numbers:")
for i, num in enumerate(sequence):
    print(f"  Position {i+1}: {num}")
print(f"\nSmallest : {min(sequence):,}")
print(f"Largest  : {max(sequence):,}")
print(f"Range    : {max(sequence) - min(sequence):,}")
print("\nStatus: Pseudorandom sequence generated successfully.")