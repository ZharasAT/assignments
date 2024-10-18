# a = 23
# b = 7
#
# q, r = divmod(a, b)
# print("Quotient: ", q)
# print("Remainder: ", r)

a = 23
b = 7

quotient = a // b

if a / b == a // b:
    print("Quotient: ", quotient)
    print("Remainder: without remainder")

elif a / b > a // b:
    print("Quotient: ", quotient)
    print("Remainder: ", a - quotient * b)