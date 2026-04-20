# Ques: To sort the array in ascending order using Insertion Sort

nums = [3,5,6,4,8,9,10,7,1,7]

'''
Imagine a pointer at beginning, looks at 3, (single element ~ sorted, moves on to 5)
5 > 3 ? sorted, moves on, 6 > 5, sorted moves on, 4 not greater than 6!!
So,  we need to insert 4 in [3,5,6] ....
We basically do (key = 4) and remove 4, and make its value as its previous index value.

[3,5,6,_,8,9,10,7,1]
[3,5,6,6,8,9,10,7,1]
[3,5,5,6,8,9,10,7,1]
[3,4,5,6,8,9,10,7,1]

Then we move on, do same for 7 and 1...


How to implement in code ?

->Take a pointer i = 0, when it reaches 4, do key = 4.
->Also, must have another pointer running which is j which is always a step behind i (j = i-1)
->[3,5,6,4,8,9,10,7,1]
   i   


->[3,5,6,4,8,9,10,7,1]
       j i                (since nums[i-1]>nums[i]), key = 4, j = i-1, nums[j+1] = nums[j], and j = j-1


->[3,5,6,6,8,9,10,7,1]
     j   i         (nums[j] > key), nums[j+1] = nums[j], j=j-1


     
->[3,5,5,6,8,9,10,7,1]
   j     i        (Here, nums[j] is not greater than key!!), so nums[j+1] = key


->[3,4,5,6,8,9,10,7,1]
   j     i    (Let's say key = 1, so we would have never find an element smaller than key, then we that if index of j == -1, then nums[j+1]=key)


->[3,4,5,6,8,9,10,7,1]
           i

->[3,4,5,6,8,9,10,7,1]
             i

->[3,4,5,6,8,9,10,7,1]
                i

->[3,4,5,6,8,9,10,7,1]
                j i     (Again, nums[i-1]>nums[i],key=7,j=i-1)

Do the same with j=j-1, until some (nums[j] < key), then do nums[j+1]=key
'''





for i in range(len(nums)):
    if (i > 0) and (nums[i-1] > nums[i]):
        key = nums[i]
        j = i-1
        while((j >= 0) and (nums[j]>key)):
            nums[j+1] = nums[j]
            j=j-1

        #if (nums[j]<key) or (j==-1): # now this part is buggy.... since there are multiple conditions like duplicates etc that we will need to specify with if statement.
            #nums[j+1]=key
        # Instead, just write nums[j+1]=key, so that if j==-1, the while loop is terminated, or if nums[j]<key, then also while loop is ternimated.

        nums[j+1]=key
        

            

print(nums)


# It does work with duplicates as well, try dry runnning the code.
# It is Okay :)

# Time complexity: For loop, and another while loop inside, O(n^2).
# Space complexity: O(1), since variable values only gets updated, no new variables are created w.r.t input size len(nums).

