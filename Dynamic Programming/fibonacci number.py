def fibonacci(n):
    fibonaccilist=[0,1]
    for i in range(2,n+1):
        fibonaccilist.append(-1)
    if n<0:
        return 'invalid'
    elif n<=1:
        return n
    else:
        if fibonaccilist[n-1]==-1:
            fibonaccilist[n-1]=fibonacci(n-1)
        if fibonaccilist[n-2]==-1:
            fibonaccilist[n-2]=fibonacci(n-2)

        fibonaccilist[n]=fibonaccilist[n-1]+fibonaccilist[n-2]
        return fibonaccilist[n]

n=int(input())
print("The",n,"th fibonacci number is ",fibonacci(n-1))