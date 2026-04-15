# Ques: Reverse an array using Recursion

num = [5,7,3,2,6,1,5,9]
# Let's say we reverse from index 2 to index 5:
# -> [5,7,1,6,2,3,5,9]

# Reverse karna hai, not sort !



def reverse(arr,left,right):
    if left >= right:
        return arr
    
    #temp = arr[left]
    #arr[left] = arr[right]
    #arr[right]=temp

    arr[left],arr[right] = arr[right],arr[left] # No need for temp

    return reverse(arr,left+1,right-1) # Here we are returning... why ?
    
    # Note that, for every stack frame, there must be some output, so we return. not just after reaching base-case, but every stack-frame in recursion call.




print(reverse([5,7,3,2,6,1,5,9],0,7))


# Dry run:
# reverse(0,7)-> reverse(1,6) -> reverse(2,5)->reverse(3,4)->reverse(4,3)(BASE-CASE)-> return arr

# Time complexity: O(n), dependent on size of the array.
# Space complexity: O(n): stores its own copy of left and right variables for each stack frame/recursive call.
# Note: arr need not be stored for each stack frame, as lists/dictionaries are not copied in every recursive call (for performance reason)
# They are mutable, and only their reference address is stored directly. (No need to access different arr in different stack frame, rather go to the same address for each recursive call.)
