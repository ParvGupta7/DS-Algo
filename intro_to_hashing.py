# Hashing is the general concept of key-value pairs. Dictionary is how we implement it in Python.
# It is used for O(1) retrieval, updation, deletion.

# Question: Two lists 'm' and 'n', check the frequency of all elements of 'm' in 'n'.

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,11,1,9,5,67,2]

# Example output: {10:1 , 11:0 ... 2:2}

# Brute force: Loop thru m, and check if each element of it exists in n.
'''
dict = {}

for i in range(len(m)):
    dict[m[i]]=0


for i in range(len(m)):
    for j in range(len(n)):
        if m[i]==n[j]:
            dict[m[i]] = dict.get(m[i])+1

print(dict)

'''

# The time complexity for this is O(n) + O(n^2). Space complexity is O(k)
# If the constraint is that 'n' and 'm' can have 10^8 elements, then O(n^2) will produce 10^16 iterations, resulting in TLE.
# Another constraint(given) is 1 <= n[i] <= 10, that means n will have values ranging from 1 to 10 only !

# Optimal Approach: We create a hash_list with length 11, 0 to 10, with all values as 0 in it.

'''hash_list = [0]*11'''

# Now, loop thru n, and lets say n[i] = 5, hash_list[i] += 1 
# Then simply we can check if any element in m exists in n, and if yes then how many occurences is stored in hash_list.
'''
for i in range(len(n)):
    hash_list[n[i]] += 1

# print(hash_list)

for i in range(len(m)):
    if (m[i] > 10 or m[i] < 1):
        print(0)
    else:
        print(hash_list[m[i]])
'''
# Time complexity: O(m + n) or O(m) + O(n)
# Note: In the context of Big O notation, O(m + n) is equivalent to O(m) + O(n).
# This means total iterations can be 10^8 + 10^8 = 2 x 10^8 ~ 10^8 (ignoring constant)

# Space complexity: we created hash_list but it will always have constant length of 11. So O(1)



# Another approach: To store frequence of all elements of n in a dictionary.

'''
d = {}

for i in range(len(n)):
    d[n[i]] = d.get(n[i],0)+1

for i in m:
    print(i,":",d.get(i,0))

# Time complexity: O(n)+O(m), Space complexity: O(k), where k is number of unique elements in n.
'''

# Character hashing:
# We need to tell the frequency of elements in list q in string s.
# Constraint: 'a' <= s[i] <= 'z'

s = "azyxyyzaaaa"
q = ["d","a","y","x"]

#Brute force: for i in q, for j in s (O(q*s)), that is O(n^2) -> TLE
# In Hashing, the approach is usually to create a hash_list with all values 0, to store the frequencies of each element.
hash_lst = [0]*26
# This list can be made with 100 length too, but  97 (a) to 122 (z) Ascii covers 26 alphabets in lowercase.
'''

for char in s:
    ascii_val = ord(char) 
    char_index = ascii_val - 97 # So, 0 index -> a, 1->b, 25->z
    hash_lst[char_index]+=1

#print(hash_lst)
'''
'''
# The above loop is for explanation, but its not optimized for space complexity. Optimized version:
for char in s:
    hash_lst[ord(char)-97] += 1

#print(hash_lst)

for ch in q:
    print(hash_lst[ord(ch)-97])
'''

#Time Complexity : O(s) + O(q) ~ Linear.
# Space complexity constant O(1).


# Now I'll try doing this with a dictionary to get output {a:1, b:3, c:2.....z:0} like this.

hash_dict = {}
for char in s:
    hash_dict[char] = hash_dict.get(char,0)+1

for ch in q:
    print(ch,":",hash_dict.get(ch,0))


# This one's my favourite approach, its time complexity = O(n) (Dependent on len(s)), its space complexity is O(1) too, cuz atmost hash_dict will have 26 key-value pairs.
# q will probably have unique characters only so atmost 26, but its not mentioned in the question.




























