# Sorting an array in ascending order using Merge sort algorithm.

# It works on Divide & Conquer technique, or we can say Divide and Merge.

# It has 2 components:
# Component 1: It keeps on dividing an array into halves, until individual/atomic elements are left.
# Component 2: Then it merges those elements back in sorted order.

nums = [3,1,2,4,1,5,2,6,4]
#.      0 1 2 3 4 5 6 7 8 (index)


'''
For even number of elements, we can half-half it for dividing part.
However, this has 9 elements so we can divide it like 5:4 , or even 4:5....in this program we do 4:5
How ? len(nums)=9 .... len(nums)/2 = 4.5 .... floor(len(nums)) = 4 

[3,1,2,4] | [1,5,2,6,4]

[3,1] | [2,4]

[3]|[1]

Then Merge back, then go to right halves. 

'''

# Before diving in to divide, lets first understand how to merge 2 sorted arrays.


'''
arr1 = [1,2,3,4] ; arr2 = [1,2,4,8,9,10,11,12]
#.      i                  j           

# We took i and j pointers and create a new arr

arr3 = []

i=0;j=0
while(i<len(arr1) and j < len(arr2)):
    if arr1[i] < arr2[j]:
        arr3.append(arr1[i])
        i+=1
    elif arr2[j] < arr1[i]:
        arr3.append(arr2[j])
        j+=1
    else: # Both equal
        arr3.append(arr1[i])
        arr3.append(arr2[j])
        i+=1
        j+=1

# The above loop will stop if either of the array is traversed ('and' condition), so the other one might not be fully traversed
# Cleanup code: to append all remaining elements

while(i < len(arr1)):
    arr3.append(arr1[i])
    i+=1

while(j < len(arr2)):
    arr3.append(arr2[j])
    j+=1



print(arr3)

'''






