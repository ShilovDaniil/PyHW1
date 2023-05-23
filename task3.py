ticket = int(input())

if (ticket%10+ticket//10%10+ticket//100%10) == (ticket//1000%10+ticket//10000%10+ticket//100000%10):
    print("Lucky!")
else:
    print("Try again :(")