def fibosum(n):
    n1 = 0
    n2 = 1
    sum = 0
    for i in range(n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        sum = sum + n1
    return sum
print ("Sum of the First 5 terms of the Fibonacci series: ", fibosum(5))
print ("Sum of the First 5 terms of the Fibonacci series: ", fibosum(10))