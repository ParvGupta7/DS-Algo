
# Ex:- 153 = 1^3 + 5^3 + 3^3 = 153 

n = int(input("Enter number: "))
temp = n
temp2 = n

digit_count = 0

while(n > 0):
    digit_count+=1
    n=n//10

# print("number of digits:" ,digit_count)
total = 0
while(temp > 0):
    rem = (temp%10)**digit_count
    total += rem
    temp=temp//10


if total == temp2:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

# Time Complexity: log10(n) + log10(n) = 2*(log10(n)) = O(log10(n))
# Space Complexity: O(1)
