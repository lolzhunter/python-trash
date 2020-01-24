import decimal
from pathlib import Path

confirm = 0
num = int(input("to how many decimal places? "))
counter = num * 3
counter1 = 1
decision = input('''do you want to use previous results to help calculate faster?
type "yes" if you do, press enter if you don't ''')
if decision == "yes":
    txtfile = int(input("which txt file to go off of? put in the number "))
    txt = Path('golden ratio to {0}th decimal place.txt'.format(txtfile)).read_text()
    txt = txt.replace('\n', '')
with decimal.localcontext() as ctx:
    ctx.prec = num+1
    if decision == "yes":
        number = txt
    else:
        number = 2
    while confirm != 1:
        checker = number
        num2 = decimal.Decimal(1) / decimal.Decimal(number)
        number = decimal.Decimal(num2) + decimal.Decimal(1)
        if checker == number:
            break
        elif counter1 == counter:
            confirm = 1
        print("{0}: {1}\n".format(counter1, number))
        counter1 = counter1 + 1
lol = counter1 / num
print(lol)
f = open("golden ratio to {0}th decimal place.txt".format(num), "a")
f.write("{0}".format(number))
f.close()
input()
