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


def gcd(a, b):
  assert int(a) == a and int(b) == b, 'The numbers must be integers only'
  if a < 0:
    a = -1 * a
  if b < 0:
    b = -1 * b
  if a == 0:
    return b
  if b == 0:
    return a
  #q = a // b
  r = a % b

  return gcd(b,r)

print(gcd(288,16))
print(gcd(16,288))
