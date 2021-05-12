# def recursiveMethod(n):
#   if n<1:
#     print("n is less than 1")
#   else:
#     recursiveMethod(n-1)
#     print(n)

# recursiveMethod(4)

# def fibonacci(n):
#   assert n >= 0 and int(n) == n, 'Fibonacci number cannot be a negative number or non integer.'
#   if n in [0,1]:
#     return n
#   else:
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(4))

# How to calculate GCD of 2 numbers
# if a =bq + r
# then gcd(a,b) = gcd(b,r)


# def gcd(a, b):
#   assert int(a) == a and int(b) == b, 'The numbers must be integers only'
#   if a < 0:
#     a = -1 * a
#   if b < 0:
#     b = -1 * b
#   if a == 0:
#     return b
#   if b == 0:
#     return a
#   #q = a // b
#   r = a % b

#   return gcd(b,r)

# print(gcd(288,16))
# print(gcd(16,288))


# My solution to converting decimal to binary
# def dec_to_binary(num, binary_code=[]):
#   assert int(num) == num, 'The numbers must be integers only'
#   quotient = int(num / 2)
#   remainder = num % 2
#   binary_code.insert(0,str(remainder))
#   if quotient == 0:
#     return "".join(binary_code)
#   return dec_to_binary(quotient, binary_code)

# print(dec_to_binary(123456789))

# #Video solution for converting decimal to binary

# def decimal_to_binary(n):
#   assert int(n) == n, 'The parameter must be an integer only'
#   if n == 0:
#     return 0
#   return n%2 + 10 * decimal_to_binary(int(n/2))

# print(decimal_to_binary(10))

# Factorial Recursion Practice

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))