# Bubble sort to get array sorted in ascending order...
# It basically works by swapping adjacent elements.

nums = [5,8,1,6,9,2,4]
'''
Now, lets say we take pointer i at 0th index, and the loop goes till i reaches end of nums
compare nums[i] and nums[i+1]
5,8 sorted, 8,1 (swap), 1,6 (ok), 6,9 (ok), 9,2 (swap), 9,4 (swap)
and in the final array nums, the largest element ie 9, will be at the end of nums.
Now, we will do the same thing, just till second last element (excluding 9 in the loop).


'''

for i in range(0,len(nums)):
    for j in range(0,len(nums)-1-i): # -1 was important otherwise index out of range.... it would take last element as nums[j] and compare with nums[j+1] which doesn't exist.
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            #print(nums)

print(nums)

#Time complexity = O(n^2)
# Space complexity = O(1)

# On the first pass, it performs len(nums)-1 iterations, second pass len(nums)-2 and so on.

# Try writing it again for practice, just with the idea in mind.


