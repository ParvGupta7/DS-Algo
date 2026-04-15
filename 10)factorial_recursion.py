# Ques: Find Factorial of a number using Recursion
# For this we do n to 1, so base-case == 1.

def Factorial(n):
    if n==1:
        return 1
    return n*Factorial(n-1)

print(Factorial(4))


# Time complexity = O(n) (Number of stack calls)
# Space complexity = O(n) (Each Stack frame creates its own copy at a time.)

