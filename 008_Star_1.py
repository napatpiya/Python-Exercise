x = int(input("Input: "))

for i in range(x):
    y = i + 1
    print("*"*y)

print("")

y = x
for i in range(x):
    print("*"*y)
    y -= 1

print("")