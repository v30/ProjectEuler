# Pythagoras: a2 + b2 = c2

# There exists exactly one Pythagorean triplet for which a + b + c = 1000
result = []

for i in range(500):
    for j in range(500):
        for k in range(500):
            # print(f"{i} {j} {k}")
            iSqr = i * i
            jSqr = j * j
            kSqr = k * k
            if iSqr + jSqr == kSqr:
                print()
                result.append([i, j, k])

product = 0
for trip in result:
    if trip[0] + trip[1] + trip[2] == 1000:
        product = trip[0] * trip[1] * trip[2]
print(product)
