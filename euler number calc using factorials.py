import decimal
import time
num = int(input("to how many decimal places? "))
b = 1
i = 1
start_time = time.time()
with decimal.localcontext() as ctx:
    ctx.prec = num+1
    e = decimal.Decimal(1)/decimal.Decimal(1)
    while True:
        b = decimal.Decimal(i) * decimal.Decimal(b)
        check = e
        e+=decimal.Decimal(1) / decimal.Decimal(b)
        if check == e:
            break
        i+=1
        print("{0}!: {1}\n".format(i, e))
end_time = time.time()
print(end_time - start_time)
f = open("{0}.txt".format(num), "w")
f.write("{0}".format(e))
f.close()
input()
