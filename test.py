import random

# lis = [2, 0, 2, 4]
lis = []
for i in range(4):
    lis.append(random.choice([0, 2, 2, 4]))

print(lis)

for c in range(3):
    for x in range(c+1, 4):
        if lis[x] != 0:
            if lis[c] == 0:
                lis[c] = lis[x]
                lis[x] = 0
            elif lis[c] == lis[x]:
                lis[c] *= 2
                lis[x] = 0
                break
            elif lis[c] != lis[x]:
                break

print(lis)


