# Count the number of digits in a number. Also, tell its complexity.


n = int(input("Enter number: "))

count = 0

while(n>0):
    count+=1
    n=n//10

print("Number of digits:",count)


# Space complexity is O(1), Time complexity is O(log10(n)+1)

# This is because, lets say n = 100, it has 3 digits. 
# Now, if we just calculate log10(n), then floor it, we get 3.
# So every number, be it 1500190 or anything, will run as many times as it has digits in it, which = log10(num)+1 
# Alternate approach: just calculate log10(number), then floor it.
