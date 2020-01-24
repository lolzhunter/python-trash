text = input("what do you want the text files to contain? ")
textcount = int(input("how many lines per text file do you want this message to be in? "))
count = int(input("how many files do you want to create containing this text? "))
half = count/2
half = round(half)
amount = textcount*count
count+=1
print('''there will be {0} "{1}" in total, press any key to continue...'''.format(amount, text))
input()
print("working on it...")
for i in range(1, count):
    f = open("massive waste of space number {0}.txt".format(i), "w")
    if i == half:
        print("halfway there!")
    for i in range(textcount):
        f.write("{0}: {1}\n".format(i+1, text))
    f.close()
print("done!")
input()
