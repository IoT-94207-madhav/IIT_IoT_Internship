# String Methods Demonstration Program

s = "  Hello Python Programming  "
s2 = "12345"
s3 = "hello123"
s4 = "HELLO"
s5 = "   "

print("Original String:", s)

# 1. Case Conversion
print("\n--- Case Conversion ---")
print("upper():", s.upper())
print("lower():", s.lower())
print("capitalize():", s.capitalize())
print("title():", s.title())
print("swapcase():", s.swapcase())

# 2. Checking / Validation Methods
print("\n--- Checking Methods ---")
print("isalpha():", "Hello".isalpha())
print("isdigit():", s2.isdigit())
print("isalnum():", s3.isalnum())
print("islower():", "hello".islower())
print("isupper():", s4.isupper())
print("isspace():", s5.isspace())

# 3. Searching & Finding
print("\n--- Searching Methods ---")
print("find('Python'):", s.find("Python"))
print("index('Hello'):", s.index("Hello"))
print("count('o'):", s.count("o"))
print("startswith('  Hello'):", s.startswith("  Hello"))
print("endswith('  '):", s.endswith("  "))

# 4. String Modification
print("\n--- Modification Methods ---")
print("strip():", s.strip())
print("lstrip():", s.lstrip())
print("rstrip():", s.rstrip())
print("replace():", s.replace("Python", "Java"))

# 5. Splitting & Joining
print("\n--- Split & Join ---")
words = s.split()
print("split():", words)
print("join():", "-".join(words))
print("rsplit():", s.rsplit(" ", 2))

# 6. Alignment & Padding
print("\n--- Alignment Methods ---")
print("center():", "Hi".center(10, "*"))
print("ljust():", "Hi".ljust(10, "-"))
print("rjust():", "Hi".rjust(10, "-"))
print("zfill():", "25".zfill(5))

# 7. Formatting
print("\n--- Formatting ---")
print("format():", "Sum of {} and {} is {}".format(10, 20, 30))
print("f-string:", f"Sum of 5 and 6 is {5+6}")

# 8. Encoding & Decoding
print("\n--- Encoding & Decoding ---")
encoded = "hello".encode()
print("encode():", encoded)
print("decode():", encoded.decode())

# 9. Other Useful Methods
print("\n--- Other Methods ---")
print("len():", len(s))
print("max():", max("abcXYZ"))
print("min():", min("abcXYZ"))

print("\n--- End of String Methods Demo ---")
