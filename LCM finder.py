while True:
    i = 1
    num1 = int(input("enter in the first number "))
    num2 = int(input("enter in the second number "))
    ans1 = 0
    ans2 = 1
    while True:
        ans1 = num1*i
        ans2 = num2*i
        print("{0}:".format(i))
        print(ans1)
        print(ans2, "\n")
        if ans1%num2 == 0:
            ans3 = ans1
            break
        elif ans2%num1 == 0:
            ans3 = ans2
            break
        i+=1
    print("the LCM of", num1, "and", num2, "is", ans3)
    input()
