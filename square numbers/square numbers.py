num = 0
count = int(input("bruh "))
count2 = count
count = count+1
for i in range(count):
    f = open("{0}.txt".format(count2), "a")
    num2 = num**2
    print("{0}: {1}\n".format(num, num2))
    num = num+1
    f.write("{0}: {1}\n\n".format(num, num2))
    f.close()
input()
