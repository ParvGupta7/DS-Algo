# In this one, we just do Head Recursion and try to make Recursion Tree.

# Ques: 1 to n using Head Recursion.

def head(n):
    if n == 0:
        return
    head(n-1)
    print(n)

head(5)

# Lets say n = 5, then it runs head(5), which is waiting for head(4) to complete, which waits for head(3) and so on till base-case.
# Then head(1) completes itself so head(2) can complete itself, similarly till head(5) completes itself.

'''
Recursion Tree:

Head(5)
   |
Head(4)
   |
Head(3)
   |
Head(2)
   |
Head(1)
   |
Head(0) Base-Condition.
   |
Head(1) Completes itself for 2
   |
Head(2) Completes itself for 3
   |
Head(3) Completes itself for 4
   |
Head(4) Completes itself for 5
   |
Head(5) Completes the entire program (being the initial call)


'''
    
    
