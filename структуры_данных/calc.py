N, M = [int(i) for i in input().split()]
s = input()

digit, result = 0, []
for symbol in s:
    digit = (digit * 10 + int(symbol)) % M
    result.append(digit)

print(*result)


