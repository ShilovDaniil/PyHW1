sideN = int(input())
sideM = int(input())
part = int(input())

if (part%sideN==0 or part%sideM==0) and sideN * sideM//(sideN * sideM)!=0:
    print("yes")
else:
    print("no")