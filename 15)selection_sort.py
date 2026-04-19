# Algorithm to sort array in ascending order.


nums = [5,7,8,4,1,6,9,2]

# How it works:
'''
We take 5, and traverse from 7 to 2, and see and find the smallest element.
Then we simply replace it with 5. 
# Note: Loop must run till the end, otherwise it may stop at 4 only (cuz its smaller than 5).

Try doing this code on my own, just from the logic, then it will be easy to understand the entire thing, and why min_index is needed etc.
'''


for i in range(0,len(nums)):
    min_index = i
    for j in range(i+1,len(nums)):
        if nums[j] < nums[min_index]:
            min_index = j
    
    nums[i],nums[min_index] = nums[min_index],nums[i]


# Time complexity: O(n^2)
# Space complexity: O(1), fixed number of variables, i, j, min_index, nums... they all just update themselves rather than creating new ones.


# Also, can try doing selection sort, but to get the array in descending order.
