memo = {}
memoC = {}
#calls = 0
def fib(X):
	#global calls
	#calls+=1
	#calls[0]+=
	aux = 0
	aux +=1
	if X not in memo:
		if X <=1 :
			#alls[0]+=1
			memo[X] = X
			memoC[X] = 1
			return X
		else:
			#calls[0]+=1
			memo[X] = fib(X-1) + fib(X-2)
			aux += memoC.get(X-1) + memoC.get(X-2)
	memoC[X] = aux
	return memo[X]

N = int(input())

for i in range(N):
	X = int(input())
	calls = 0
	aux = 0
	'''if (X <= 1):
		calls = 1
	else:
		calls = 2 ** (X-1) '''
	a = fib(X)
	print ('fib ('+str(X)+') = ',calls,'calls =', a)
	print(memoC)
	#print(memo)
	