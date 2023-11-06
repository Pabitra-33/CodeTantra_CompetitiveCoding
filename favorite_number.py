def is_Tracys_favorite_number(num):
    def get_next_number(n):
        total = 0
        while n > 0:
            total = total + (n%10) **2
            num = num//10
        return total

    while n! = 1 and n not in(89,145,42,20,4,16,37,58):
        num = get_next_number(num)

    return num == 1

number = int(input())
if is_Tracys_favorite_number(number):
    print("Yes")
else:
    print("No")
