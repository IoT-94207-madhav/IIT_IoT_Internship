#   if condition:
#       statement(s)

#   if condition:
#       statement(s)
#   else:
#       statement(s)

#   if condition:
#       statement(s)
#   elif condition:
#       statement(s)
#   else:
#       statement(s)

n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))

max = 0
if n1 == n2:
    max = n1
    print("n1 and n2 are equal")
elif n1 > n2:
    max = n1
    print("n1 is greater")
else:
    max = n2
    print(f"n2 is greater")

