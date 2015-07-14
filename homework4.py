import random
l = [random.randrange(0,100)for n in range(0,200)]
try:
    num1 = int(raw_input("please enter number from 0-90"))
    counum=[]

    for i, numbers in enumerate(l):
        if(num1==numbers):
            counum.append(i)
    print len(counum), "index: ", ",".join(map(str,counum))
    if num1<0 or num1>90:
        print("only numbers from 0-90 allowed")
    elif num1 not in l:
        print "try again"
except ValueError:
    print "only numbers allowed"

