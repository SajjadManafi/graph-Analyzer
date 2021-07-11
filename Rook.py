from math import comb as nCr

print("")
print("Please Enter n:")
n = int(input())
print("")

polynomial = ""

for i in range(n+1):
    res = 1

    for j in range(i):
        res *= n-j

    if i != 0:
        polynomial = str(nCr(n,i) * res) + "x" + "^" + str(i) + " + " + polynomial

    else:
        polynomial = "1" + polynomial

print(polynomial)


print("")
