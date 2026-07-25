# Multiplication Table Generator
print("=" * 50)
print("      MULTIPLICATION TABLE GENERATOR")
print("=" * 50)

# Input Statement
number = int(input("\nEnter a Number: "))

print("\nMultiplication Table of", number)

# For Loop
for i in range(1, 11):
    print(number, "x", i, "=", number * i)

# Exit Message
print("\nThank you for using the Multiplication Table Generator!")
