# String Slicing Demonstration

s = input("Enter a string: ")

print("\nOriginal String:", s)

# Basic slicing
print("\n--- Basic Slicing ---")
print("s[0:5] :", s[0:5])
print("s[:5]  :", s[:5])
print("s[2:]  :", s[2:])
print("s[:]   :", s[:])

# Negative indexing
print("\n--- Negative Indexing ---")
print("s[-5:] :", s[-5:])
print("s[:-2] :", s[:-2])
print("s[-6:-1]:", s[-6:-1])

# Step slicing
print("\n--- Step Slicing ---")
print("s[::2] :", s[::2])
print("s[1::2]:", s[1::2])
print("s[2:8:2]:", s[2:8:2])

# Reverse string
print("\n--- Reverse String ---")
print("s[::-1]:", s[::-1])

# Extracting specific parts
print("\n--- Extracting Parts ---")
print("First character :", s[0])
print("Last character  :", s[-1])
print("Middle part     :", s[1:-1])

print("\n--- End of Slicing Demo ---")
