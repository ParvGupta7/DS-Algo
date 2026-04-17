#Fibonacci series, starts with 0 and 1, and next number is the sum of previous two numbers.
#Eg- 0,1,1,2,3,5,8,13,21....



# Ques: What is the value of nth fibonacci number. (indexed from 0)
# Eg- n = 4 -> 2

# Tried this myself:

n = int(input("Enter n: "))

def fibonacci_loop(n):
    a = 0
    b = 1
    
    i = 0
    while(i<n):

        if i == 0:
            #print(i)
            i+=1
        elif i==1:
            #print(i)
            i+=1
        else:
            c = a+b
            a = b
            b = c
            #print(c)
            i+=1
    return c

#print(fibonacci_loop(n))

#Time complexity : Linear, O(n)
# Space complexity: O(1), inside loop no new variables are created, only existing ones are updated.

#Now, try using Recursion:
# Try to get the flow, like in factorial we have f(5) = 5 x f(4)

# So here in fibonacci we have: f(4) = f(3) + f(2) , simple enough
# Or we can say: f(n) = f(n-1) + f(n-2)
def fibonacci_recursion(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2) # Simply add !
    

# Time complexity: We know, for every stack frame, there are 2 calls being made...so O(2^n)
# Space complexity: O(2^n), as for all the stack frames holding their own 'n'.


print(fibonacci_recursion(n))
    

# For Leetcode 509 Using recursion :
'''
class solution:
    def func(self,num):
        if num==0 or num==1:
            return num
        return self.func(num-1) + self.func(num-2)
    def fib(self,n:int)->int:
        answer = self.func(n)
        return answer


'''
# Try leetcode problem without recursion!
    




