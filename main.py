memo = {}
def fib(X, calls):
	calls[0]+=1
	try:
		return memo[X]
	except:
		#calls[0]+=1
		if X <=1 :
			#alls[0]+=1
			memo[X] = X
			return X
		else:
			#calls[0]+=1
			memo[X] = fib(X-1, calls) + fib(X-2, calls)
			return memo[X]

N = int(input())

for i in range(N):
	calls = [0]
	X = int(input())
	a = fib(X, calls,)
	print (f"{calls[0]} {a}")
	print(memo)
	