# CSES Range Xor Queries - Accepted
# Solution by: Robert Nagy h375338@stud.u-szeged.hu 

n, k = [int(num) for num in input().split(" ")] # List comprehension
nums = [int(num) for num in input().split(" ")]
prefixXor = [nums[0]] * n # Prefix sum (actually prefix xor in this case)
for i in range(1, n):
    prefixXor[i] = prefixXor[i-1] ^ nums[i]

ans = [0] * k
while k > 0:
    [start, end] = [int(num) for num in input().split(" ")]
    if start == 1:
        ans[-k] = prefixXor[end - 1]
    else:
        ans[-k] = (prefixXor[end - 1] ^ prefixXor[max(start - 2, 0)]) #The inverse operation of XOR is itself
    k -= 1

for num in ans:
    print(num)

