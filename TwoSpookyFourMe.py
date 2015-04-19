#2spooky4me
#The code below was written in Python 3.4

def TwoSpookyFourMe(n, loops = -1):
	"""
	Collatz Conjecture
	Function takes an integer greater than or equal to 1 called n
	returns number of repetitions needed to transform n into 1 via recursion
	Optional argument "loops" needed for loop counter through recursion
	"""
	loops = loops + 1					#counter starts at -1; upon every recursive statement, add 1 to loop
	if n<1 or n%1!=0:					#if n does not satisfy being an integer greater than or equal to 1
		return None						#return None, as to tell that something went wrong in the recursion OR initial input was unsatisfactory
	if n<=1 or n%1!=0:					#if n equals 1
		return loops					#return the integer value of loops
	elif n%2==1:						#else if n is odd
		return TwoSpookyFourMe(3*n + 1, loops)		#return the result of the function for 3*n+1, and the value of loops is preserved by making it an argument
	else:								#else (only other case being n is even)
		return TwoSpookyFourMe(n/2, loops)			#return the result of the function for n/2, and the value of loops is preserved by making it an argument

print(TwoSpookyFourMe(56543513513131))	#result is 294
