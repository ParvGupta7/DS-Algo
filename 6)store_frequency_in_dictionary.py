# Basically, store the frequency of all elements in dictionary/frequency_map.

freq_map = {}

nums = [1,2,3,4,4,1,3,5,8,9,10,6,6,7,10,1,1,1]

#Brute Force Logic: If the element doesn't already exist in dictionary, we make dict[element]=1, else: dict[element]+=1
'''

for i in nums:
    if i not in freq_map:
        freq_map[i]=1
    else:
        freq_map[i]+=1

print(freq_map)
'''
# When we look at it initially, it seems that Time complexity is O(n^2) cuz of the membership operator.
# However, membership operator doesn't search linearly, instead it operates in O(1).
# Hence, total Time Complexity = O(n).
# Space complexity = O(n), dependent on number of elements in 'nums'.

# Method 2: Using .get() method of dictionary.
# It retrieves the value of a specific key. Syntax: dict.get(key)
# Why use .get() instead of (dict[key]) ? Cuz if we try to access a key that doesn't exist, program crashes.
# Whereas with .get(), it would return 'None' and not crash.
# We can also mention a default value, so if a key doesn't exist, it will be created with some default value specified.
# Syntax: dict.get(key,defaul_val)


hash_map = {}
for i in range(len(nums)):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1   # Try Dry Run

print(hash_map)


# Note: Hashmap refers to the general abstract data structure format. Dictionary is its name in Python.
# This is a much more standard approach.
# Here also, the time complexity for this O(n) due to the for loop. The .get() works in O(1).
# Space complexity remains O(n) as we store all unique keys from nums.





