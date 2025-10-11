a = [7, 15, 3, 8, 12, 27, 25]
i = 0
while i < len(a):
    if a[i] % 3 == 0:
        print("Multiple of 3:", a[i])
        a[i] = "raghu"
    i += 1

print("Final list:", a)
