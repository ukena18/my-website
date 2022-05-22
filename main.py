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
