S = input()

count = 0

for s in S:
    if s == "w":
        count += 2
    else:
        count += 1

print(count)