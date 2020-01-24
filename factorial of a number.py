while True:
    num = int(input("enter in what number you want to factorize "))
    d = 1
    for i in range(1, num+1):
        d*=i
        print("{0}: {1}\n".format(i, d))
        
        
