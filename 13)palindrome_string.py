# Ques: Check whether a string is palindrome or not.
# Eg- nitin

# Iterative approach: Using two pointers left and right

s = input("Enter string: ")
s = s.lower()


left = 0
right = len(s)-1 # Index of last element
'''
while(left<=right):
    if s[left]==s[right]:
        left+=1
        right=-1
    
    else:
        print("Not a palindrome")
        break
    print("Palindrome")
'''
# Time complexity: O(n/2) ~ O(n) since it loops till midway linearly depend on len(s)
# Space complexity: O(1)

# Now, Recursive Approach:
# Base case should be when left==right, then we stop, otherwise (s,left+1,right-1)
def func(s,left,right):
    if s == "": # I realised this part after writing entire logic... to handle empty string, otherwise it may crash.
        return False

    if left>=right and s[left]==s[right]:  # if we do left==right, then it fails for 'aa' or 'aaaa' (even length)
        return True
    
    if s[left]==s[right]:
        return func(s,left+1,right-1)
    
    return False # Genuine ques, when does it return False if base case is never reached lol....
    # It will return False if both the above conditions (if conditions are not satisfied, the only line remains is return False.)
    # So, basically it will check till the very end for a palindrome, and if any mismatch then return False.

print(func(s,left,right))


# The above code was written by me.
# Try Dry running this and re-writing for practice.

# Time complexity: Number of stack calls/frames w.r.t to len(s)... O(n/2)~O(n)
# Space complexity: every stack frame has its own copy of s,left,right.... so O(n/2)~ O(n) ...since it creates/stores the variables n/2 times the size of input (len(s)).

#So, we can say iterative approach is better for Space complexity.




