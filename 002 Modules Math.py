import math

# for name in dir(math):
# 	print(name, end="\t")

# ceil(), floor(), trunnc()
# print(math.ceil(3.6))
# print(math.floor(3.6))
# print(math.trunc(3.6))

print("\nceil()")

# ceil()
print(math.ceil(3.1))
print(math.ceil(3.505))
print(math.ceil(3.945))
print(math.ceil(3.0))
print(math.ceil(-3.4))

print("\nfloor()")

# floor()
print(math.floor(3.1))
print(math.floor(3.505))
print(math.floor(3.945))
print(math.floor(3.0))
print(math.floor(-3.4))

print("\ntrunc()")

# trunc()
print(math.trunc(3.1))
print(math.trunc(3.505))
print(math.trunc(3.945))
print(math.trunc(3.0))
print(math.trunc(-3.4))

print("\nfactorial()")

# factorial()
# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24
print(math.factorial(3))
print(math.factorial(4))

print("\nsqrt()")

# sqrt()
print(math.sqrt(16))
print(math.sqrt(100))

print("\nhypot()")

# hypot()
print(math.hypot(3, 4))