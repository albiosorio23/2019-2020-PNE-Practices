def fibon(n):
    n1 = 0
    n2 = 1
    for i in range (n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n1
print ("5th Fibonacci term:", fibon(5))
print ("10th Fibonacci term:", fibon(10))
print ("15th Fibonacci term:", fibon(15))
