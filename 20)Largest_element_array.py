#Ques: Find the largest element in the array.

nums = [5,32,-97,99,3,67]


largest = nums[0]
# Or one can do: largest = float("-inf"), for -infinity.


for i in range(len(nums)):
    if nums[i] >= largest:
        largest = nums[i]
    
print(largest)


# Time complexity: O(n), linearly dependent with input size ie len(nums)
# Space complexity: O(1), constant space, only updation.

