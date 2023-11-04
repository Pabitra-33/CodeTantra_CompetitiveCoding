number = int(input())
temp = number
reverse = 0
while number > 0:
    rem = number%10
    reverse = reverse*10+rem
    number = number // 10

if(temp == number):
    print("True")
else:
    print("False")