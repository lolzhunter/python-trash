import decimal
place = int(input("to how many decimal places? "))
counter = 1
with decimal.localcontext() as ctx:
    test = decimal.Decimal(2)
    amount = decimal.Decimal(0.5)
    two = decimal.Decimal(2)
    while True:
        ctx.prec = counter
        answer = test**amount
        print("{0}: {1}\n".format(counter, answer))
        if counter == place:
            break
        counter+=1
output = answer**decimal.Decimal(two)
print(output)
f = open("the sqrt of 2 to {0}th decimal place.txt".format(place), "a")
f.write("{0}".format(answer))
f.close()
input()
