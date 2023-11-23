import random

print(random.random())
print(random.random())
print(random.random())

# print("\nseed")
# random.seed(0)
# print(random.random())
# print(random.random())
# print(random.random())

print("\nchoice")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["Alan", "Kate", "Dave", "Jo", "John"]

print(random.choice(numbers))
print(random.choice(names))

print("\nrandom in range (with duplicates)")
for i in range(10):
	print(random.choice(numbers))

print("\nrandom in range (without duplicates)")
for k in range(1):
	print(random.sample(names, 3))
