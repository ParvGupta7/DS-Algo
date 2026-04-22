# Check if an array is sorted or not, return True or False

nums= [3,5,6,8,9,10,20,1]

def check_sorted(array):

    for i in range(len(array)-1):
        if(array[i]>array[i+1]):
            return False
    
    return True


print(check_sorted(nums))


# Time complexity: Worst case O(n), if array is sorted.
# Space complexity: O(1)

        