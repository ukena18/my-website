#!/bin/python3

import math
import os
import random
import re
import sys

#
# There is a large pile of socks that must be paired by color. Given an array of integers   #representing the color of each sock, determine how many pairs of socks with matching colors there #   are.
# Complete the 'sockMerchant' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

# def sockMerchant(n, ar):
#     check_pair = []
#     number_of_pairs = 0
#     # loop through the array
#     for single_sock in ar:
#         if single_sock in check_pair:
#             check_pair.remove(single_sock)
#             number_of_pairs +=1
#         else:
#             check_pair.append(single_sock)
#     return number_of_pairs

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = sockMerchant(n, ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()


##### 
##### 
# 1 - i can do for loop through the arr 
# 2 - append each element to the new_array and 
# an incrementing for number of pair of socks
# 3 - check if the element is already in the array
# 4 - if the element i go through is already in the array
#   pop out this element from array and increment thenumber of pairs
#  i can do all of them inside an for loop so it will have o(n)  time complexity
#  and o(n) space complexity 
# s_len =len("sas")
# quitent= 10//s_len
# new_str= quitent*"sas"
# new_s_len= len(new_str)
# leftover =10-new_s_len
# new_str += new_str[:leftover]
# print(new_str)


# def minimumBribes(q):
#     number_of_bribe = 0
#     sorted_q = sorted(q)
#     pivot = last_index=len(q)-1
#     while True:
#         if pivot==0 and last_index==0:
#             return number_of_bribe
#         if sorted_q[pivot] == q[last_index]:
#             pivot -=1
#             last_index -=1
#         else:
#             if sorted_q[pivot] == q[last_index-1]:
#                 q[last_index],q[last_index-1] = q[last_index-1],q[last_index]
#                 number_of_bribe +=1
#             elif sorted_q[pivot] == q[last_index-2]:
#                 q[last_index-2],q[last_index-1] = q[last_index-1],q[last_index-2]
#                 number_of_bribe +=1
#             else: 
#                 return "Too chaotic"
        
    # return number_of_bribe
def min_swap(arr):  
    swap= 0
    index=0
    while True:
        if index==len(arr)-1:
            break
        if arr[index]-1 == index:
            index += 1
        else:
            arr[index-1],arr[index] = arr[index],arr[index-1]
            swap +=1
        
        
    return swap

if __name__ == '__main__':
    
    test =[[5, 1, 2, 3, 7, 8, 6, 4],
    [1,2,5,4,3],
    [1, 2, 5, 3, 4, 7, 8, 6]]
    for i in test:
        ans = min_swap(i)
        print(ans)