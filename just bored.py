import time
#time is imported so that we can measure how long it takes for the program to complete
i=1
a = 0
b = 0
#basically setting the numbers to zero for later
c = int(input("enter in how many times before the second number increases by one "))
#as in how big of a number before the counter goes up by one, like when it has been 60 seconds the minute goes up by 1
#the number also controls how high the counter can go before it stops
d = c*c+c*2
#special formula that I have assigned to d for later, basically figures out how many times it should calculate before the counter reaches its
#target number
f=open("results{0}.txt".format(c), "w")
#making a text file that the program will constantly output the results into and display the time taken at the bottom 
f.write("{0} {1}\n".format(a, b))
#starts off by outputing 0 0, as the program doesnt get a chance since from here its just adding 
startTime=time.time()
#starting the stopwatch
print(a, b)
#same thing except its outputing the 0 0 into the python console
for i in range(d):
#basically saying for this many times (d = how many times it needs to repeat before the counter gets to whatever number was typed in)
#I will do this, which is basically saying if a (first number)
#equals the number inputted then it will go back to 0 and put the counter (b) up by 1
#and if it doesnt equal number entered in it will go up by 1 until it reaches the number, and will keep doing this for a set ammount of time
#(using the formula earlier which calculates how many times it does this till counter has reached the required number) until its done it "d"
#ammount of times (d = how many times until the counter has reached the required number but I'm pretty sure you knew that)
    if a == c:
        a = 0
        b = b + 1
    else:
        a = a + 1
    print(a, b)
#print just means it will display its current progress every loop
    f.write("{0} {1}\n".format(a, b))
#similar butits outputing the results into a text file every time
endTime=time.time()
#once loop is complete it will end the stopwatch
finishtime = endTime-startTime
#figuring out how long it took start to finish
if finishtime>=120:
    mintime = finishtime/60
    print("this took")
    print(mintime, "minutes")
    print("to finish")
    f.write("this took {0} minutes to finish".format(mintime))
elif finishtime>=60 and finishtime<120:
    mintime = finishtime/60
    print("this took")
    print(mintime, "minute")
    print("to finish")
    f.write("this took {0} minute to finish".format(mintime))
elif finishtime>=7200:
    hourtime = finishtime/3600
    print("this took")
    print(hourtime, "hours")
    print("to finish")
    f.write("this took {0} hours to finish".format(hourtime))
elif finishtime>=3600 and finishtime<7200:
    hourtime = finishtime/3600
    print("this took")
    print(hourtime, "hour")
    print("to finish")
    f.write("this took {0} hour to finish".format(hourtime))
elif finishtime>=2 and finishtime<60:
    print("this took")
    print(finishtime, "seconds")
    print("to finish")
    f.write("this took {0} seconds to finish".format(finishtime))
elif finishtime<1:
    print("this took")
    print(finishtime, "of a second")
    print("to finish")
    f.write("this took {0} of a second to finish".format(finishtime))
else:
    print("this took")
    print(finishtime, "second")
    print("to finish")
    f.write("this took {0} second to finish".format(finishtime))
#now this wall of text is basically a bunch of if statements tring to figure out
#if its been going on for an hour, a minute or only a few seconds and will display the time in the correct format as the stopwatch
#only records in seconds, basically its a wall of code that displays the time in 2 hours instead of 7208.89373 seconds
f.close()
#closes the text file which in turn saves the results to be read later
