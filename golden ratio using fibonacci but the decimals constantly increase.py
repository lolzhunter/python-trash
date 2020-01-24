def fib():
  a,b = 1, 1
  while True:
    yield "{}".format(a)
    a, b = b, a + b
place2 = int(input("how many decimal places? "))
previous = 0
count = 0
checker = 0
place = 0
import decimal
import time
start_time = time.time()
with decimal.localcontext() as ctx:
  for item in fib():
    if count != 0:
      ctx.prec = place+1
      item = decimal.Decimal(item)
      previous = decimal.Decimal(previous)
      golden = decimal.Decimal(item)/decimal.Decimal(previous)     
      if checker == golden:
        if place != place2:
          place+=1
          place3 = place-1
          print("{0}: {1}\n".format(place3, golden))
        else:
          print("{0}: {1}\n".format(place, golden))
          break
      checker = golden
    previous = item
    count+=1
end_time = time.time()
print(end_time - start_time)
print("took {0} iterations".format(count-1))
f = open("{0} golden ratio.txt".format(place2), "w")
f.write("{0}".format(golden))
f.close()
input()
