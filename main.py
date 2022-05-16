from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


memo = {}
def fib(X):
	try:
		return memo[X]
	except:
		if X <=1 :
			memo[X] = X
			return X
		else:
			memo[X] = fib(X-1) + fib(X-2)
			return memo[X]

N = int(input())

for i in range(N):
	X = int(input())
	a = fib(X)
	print ("fib({0}) = {1:.0f} calls = {2}".format(X, 2*F(X+1)-2, a))
	