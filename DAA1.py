"""
The Fibonacci series is a sequence in which each number is the sum of the previous two numbers.
The sequence starts with: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Mathematical recurrence relation:F(n)=F(n-1)+F(n-2) ... with base conditions F(0)=0, F(1)=1
"""

def iterative_fib(n):
    if n<0:
        return "Incorrect input"
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b

def recursive_fib(n):
    if n<=1:
        return n
    return recursive_fib(n-1)+recursive_fib(n-2)


n=int(input("enter the no of terms u want in fiboncci seriess:"))
print("Iterative Fibonacci:")
iterative_fib(n)

print("\nRecursive Fibonacci:")
for i in range(n):
    print(recursive_fib(i), end=" ")
