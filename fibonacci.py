#This code was written in Python 3.4

def fibseries(x, series=False):		#generates a list of the fibonacci series from 0th term to xth term, and returns the xth term
						#fast because it's a very linear problem of addition. Terms get very long after x = 1000
						#optional argument "series" allows for return of list of fibonacci series
	fib = []			#list to hold the elements of the series
	i = 0 				#counter for the current term of the series
	while i <= x:		
		if i < 2:
			fib.append(1) 	#appends "1" to the series for i = 0 and i = 1
		else:
			fib.append(fib[i-1] + fib[i-2])		#appends the sum of the previous two terms as the current term
		i += 1
	if series:				#if optional argument is placed as True
		return fib 			#returns the fibonacci series as a list up to x
	else:					#by default, series is set to False
		return fib[x]		#returns the xth term

def fibnum(x):			#Recursive and simple form for finding a xth term of the fibonacci series.
						#Very slow due to several calls to itself
						#Do NOT call for large x values
	if x == 1 or x == 0:
		return 1
	else:
		return fibnum(x-1) + fibnum(x-2)

print(fibseries(100))			#prints the 100th term of the fibonacci series
#result> 573147844013817084101
fibonacciseries = fibseries(20, True) 
for i in fibonacciseries:
	if i == fibonacciseries[len(fibonacciseries)-1] and len(fibonacciseries)-1>0:	#incase the series is of the first two elements (1,1)
		print(i)
	else:
		print(i, end = ", ")		#returns each element of the fibonacci series, separated by a comma and a space, on one line
#result> 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946



