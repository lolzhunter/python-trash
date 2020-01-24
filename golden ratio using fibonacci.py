def fib():
  a,b = 1, 1
  while True:
    yield "{}".format(a)
    a, b = b, a + b
place = int(input("how many decimal places? "))
previous = 0
count = 0
checker = 0
import decimal
import time
start_time = time.time()
with decimal.localcontext() as ctx:
  ctx.prec = place+1
  for item in fib():
    if count != 0:
      item = decimal.Decimal(item)
      previous = decimal.Decimal(previous)
      golden = decimal.Decimal(item)/decimal.Decimal(previous)
      if checker == golden:
        break
      checker = golden
      print("{0}: {1}\n".format(count, golden))
    previous = item
    count+=1
end_time = time.time()
print(end_time - start_time)
input()
