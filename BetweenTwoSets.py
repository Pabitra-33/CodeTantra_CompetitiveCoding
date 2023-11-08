input();
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
for i in range(1, 101):
    if all(i%x == 0 for x in a) and all(x%i == 0 for x in b):
        result += 1
print(result)