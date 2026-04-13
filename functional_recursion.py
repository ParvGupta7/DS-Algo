# In this we will do Sum of 1 to n, using parameterized recursion.
# Now, we see we cannot do some count = 1, till n as some base condition.
# So, we would want sum (n to 1), so base condition should be till n == 0.

def summ(n):
    if n==0:
        return 0 # This will end the function and return 0, it wont check for -1,-2 and so on.
    return n + summ(n-1)
    

#print(summ(4))

# Dry Run: 
# summ(4) -> 4 + summ(3)
# summ(3) -> 3 + summ(2)
# summ(2)-> 2 + summ(1)
# summ(1)-> 1 + summ(0)
# summ(0)-> 0
# summ(1)->1, summ(2)->2+1=3, summ(3)->3+3=6, summ(4)->4+6=10

# Ques: Write a function with parameters (total=0,i,n) which does sum from "i to n".
# i to n, so i must be incremented until it reaches n, thats the base condition.


def function(total,i,n):
    if i > n:
        #print(total)
        return total
    #print(total)

    return total + function(total+1,i+1,n)
    
print(function(0,1,4))

# This worked, i tried to solve it somehow by running and dry running. It can be easily solved as well.


# For doing recursion stuff, yes we can try intuitively, also we can create a flow:
# Eg: f(10) = 10+9+8.....3+2+1 = 55
# Or, f(10) = 10 + f(9)
# f(9) = 9 + f(8)
# f(n) = n + f(n-1) this is exactly what we did in our first Ques.

# For Time Complexity: Check how many times the function was called.
# Lets say n = 4, then 4 times it was called, or maybe 5.... So linear time complexity ie O(n).
# For space complexity, consider the first Ques:

'''
every time summ(n-1) is called, the computer cannot finish the current function until the next one returns a value.
 To keep track of where it is, it pushes a Stack Frame onto the call stack. If n=5, you will have 6 frames on the stack n=5, 4, 3, 2, 1, and the base case 0).
 If n=100, you will have 101 frames.Since the number of stack frames grows linearly with the input n, 
 the space complexity is O(n).

 Or one could simply say, each new recursive step creates its own copy of the variables... so space complexity is O(n).

 
Each step has its own environment (stack frame).
Local variables and parameters are unique to that frame.

Note: Large objects like lists or dictionaries aren't usually copied automatically (for performance reasons).
because lists and dictionaries are mutable, you aren't passing a "copy" of the data into the recursive call—you are passing a reference (an address) to the original object in memory.

'''


    