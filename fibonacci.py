def fib(num):
  a,b = 0, 1
  for i in range(0, num):
    yield "{}:: {}".format(i + 1,a)
    a, b = b, a + b
number = int(input("put in number lmao "))
for item in fib(number):
  f = open("fibonacci{0}.txt".format(number), "a")
  f.write(item+"\n\n")
  f.close()
  print(item+"\n")
input()
    
