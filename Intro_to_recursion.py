# Recursion, as we know is a function calling itself.


'''
def greet():
    print("Good morning!")
    def greet()

'''

# When a function is invoked, it gets pushed into a stack, and when all lines inside the function have executed, then that function call gets popped from the stack

# The above is a case of infinite recursion, hence we need a base case (stopping condition).
# In Python, if a function keeps on calling itself 987 times, the it throws an error "StackOverflow", although we can change that 987 limit if we want.

# Ques: Using recursion, we need to print "Parv" 4 times.


def Parv(count):
    if (count == 0):
        return 
    
    print("Parv")
    Parv(count-1)

# print(Parv(4))


# Note: Both Recursion and Loops are a form of iteration only and both can be used to solve the same problem.
#Memory wise, Recursion uses the Call Stack which grows with each call, whereas Loops use fixed variables and Recursion is better for 'branching' like problems

# Head and Tail Recursion:
# In Head recursion, the recursive call is made at the beginning (right after base case)
# In Tail recursion, recursive call is the last statement in the function.

#Ques: Try to print n to 1 using Recursion


def Tail(n):
    if n == 0:
        return
    print(n)
    Tail(n-1)

#print(Tail(10))


# Now lets try using Head Recursion:

def Head(n):
    if n == 0:
        return
    Head(n-1)
    print(n)

# What happens here ? Dry run it!
# So Head(5)->Head(4)->Head(3)->Head(2)->Head(1)->Head(0)(return)
# Now we know the first call was of Head(5) and that is incomplete, to complete it first Head(4) must run
# To complete Head(4) , Head(3) must run, and so on... so basically it print(1 to 5)
# Its okay, no need to break head, understanding this with dry run and intuition is sufficient for now.

# Technically, we cannot print n to 1 using Head Recursion, cuz we take input as 'n' and we immediately call Head(n-1) which takes it to 0 (base-case)
# Then it comes back completing Head(1), Head(2) and so on till the first call Head(5) is completed and CallStack (simply stack) is empty.

print(Head(5))

# In Tail, function finishes/completes itself, only then moves on to the next recursive call, it does this until base-case is met.
# Whereas in Head recursion, it keeps calling, then completes itself. Dry running is useful in understanding this.

# Im in a hurry rn, Bye!