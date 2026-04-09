# Eg- n = 20, factors = 1,2,4,5,10,20 
# Brute force is as follows:
n = int(input("Enter number: "))

'''
for i in range(1,n+1):
    if (n%i == 0):
        print(i)
'''
# No. of iterations is linearly dependent on input size 'n', so time complexity = O(n).
# To store the factors in a list, it will be O(k) Space complexity, where k is the number of factors of n.
# Better solution would be to iterate till n/2 
# Note (21 // 2 = 10), this is called floor division.

'''
for i in range(1,((n//2)+1)):
    if (n%i == 0):
        print(i)

print(n) # Cuz the number itself is also a factor.
'''
# This one also is linearly dependent on input 'n', just halves the iteration. Time complexity: O(n/2) ~ O(n).

# Optimal Solution: 

# Lets say n = 36, 
# First iteration, check if 36%1 == 0 ? Yes! ,Then do 36/1 = 36 ...(the quotient as well as divisor, both are factors)
# Second iter, 36%2 == 0 ? Yes, 36/2== 18 (So, 18 will also be a factor)
# Third iter,4th iter, 5th, and 6th iter do similarly.
# Basically, perform only root(n) number of iterations and you will get all the factors!
import math

result = []
for i in range(1,int(math.sqrt(n)+1)):
    if n%i==0:
        result.append(i)
        result.append(int(n/i))

result.sort() # O(nlogn)
print(result)

# Also linearly dependent on input, but iterates till root(n) only!
# Time complexity is O(root(n)), space complexity is O(k).

# we can try sorting the result list, so total time comp. = O(root(n)) + O(nlogn) 