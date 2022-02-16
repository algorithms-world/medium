import math

def sieve_of_eratosthenes(n):
	arr =  [True for i in range(n+1)]
	arr[0] = arr[1] = False
	for i in range(2,int(math.sqrt(n))+1):
		if arr[i]:
			for j in range(i**2,n+1,i):
				arr[j] = False
	return [i for i, x in enumerate(arr) if x]
