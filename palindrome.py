
# Write a program to Check whether an integer is a palindrome.


# 1234 % 10 = 4
# 1234 // 10 = 123 (Both are not same)

n = int(input("Enter a number: "))
temp = n
reverse = 0
while(n>0):
    last_digit = n%10 #7,6,5,4
    reverse = (reverse)*10 + last_digit #7, 76, 765, 7654
    n = n//10
print("Reverse = ",reverse)

def checkPalindrome(temp):
    if temp==reverse:
        return True
    else:
        return False
        
        
print(checkPalindrome(temp))

#  Time complexity is O(log10(n)), as number of iterations = number of digits.

# Space complexity is O(1), the variables inside loop like  'reverse' updates itself log(n) times and gets overwritten with each iteration.
# So, basically its just one single box of memory that is there. 
'''Lets say a program
s = "abcdefc"
l = []
for i in s:
    l.append(i)
# Now this has O(n) Space complexity, as there are multiple boxes of memory being created.

'''






    
    
    