"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.

For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]
"""

import collections
#using array O(n^2)
def delete_nth_num(array, n):
    ans = []
    for num in array:
        if ans.count(num) < n:
            ans.append(num)
    return ans


print(delete_nth_num([1,3,3,4,4,2,1,5,1,5], 2))

#using hash table O(n)
def delete_nth(array, n):
    result = []
    counts = collections.defaultdict(int)
    for i in array:
        if counts[i]<n:
            result.append(i)
            counts[i]+=1
    return result

print(delete_nth([1,2,3,1,2,2,1,4,3],2))