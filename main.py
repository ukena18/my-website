
# # # # from cmath import e
# # # # import statistics
# # # # from tracemalloc import start 

# # # # ser = statistics.median_low([1,2,3,4])
# # # # print(ser)



# # # # elements = [4,5,3 ]


# # # # def partition(elements,start,end):
# # # #     pivot_index = start
# # # #     pivot= elements[pivot_index]

# # # #     # start  =pivot_index + 1
# # # #     # end = len(elements)-1

# # # #     while start < end :
# # # #         while elements[start] <= pivot:
# # # #             start +=1

# # # #         while elements[end] >= pivot:
# # # #             end -=1
# # # #         if start <end:
# # # #             elements[start], elements[end] = elements[end], elements[start]

# # # #     elements[pivot_index], elements[end] = elements[end] , elements[pivot_index]

# # # #     return end


# # # # def quick_sort(elements,start,end):
# # # #     if start < end :
# # # #         p1 = partition(elements,start,end)
# # # #         quick_sort(elements,start,p1-1)
# # # #         quick_sort(elements,p1+1,end)
# # # #         print(elements)


# # # # quick_sort(elements,0,len(elements)-1)
# # # import statistics

# # # statistics.






# # # # def insert_me(arr,start,end,target_idx):
# # # #     if start<end:
# # # #         if arr[target_idx]> arr[start] :
# # # #             insert_me(arr,start+1,end,target_idx)
# # # #         else:
# # # #             arr.insert(start,arr[target_idx])
# # # #             arr.pop(target_idx+1)
    



# # # # def insertion_sort(elements):
# # # #     i= 1
    
# # # #     while i<len(elements)-1:
# # # #         insert_me(elements,start=0,end=i,target_idx=i)

# # # #         i +=1

            
# # # # elements = [1,4,3,5]
# # # # insertion_sort(elements)
# # # # print(elements)

# # # # def merge_two_sorted_lists(arr1,arr2):
# # # #     sorted_list = []
# # # #     len_a = len(arr1)
# # # #     len_b = len(arr2)
# # # #     i = j = 0
# # # #     while i < len(arr1) and j < len(arr2):



# # # # def subarr(arr,k):
# # # #      windowsSum = 0
# # # #      maxSum = (0,[])

# # # #      windowsSum = sum(arr[:k])

# # # #      for end in range(k,len(arr)):
# # # #         windowsSum += arr[end]  - arr[end - k]


# # # #      print(maxSum)

# # # # arr = [1,3,4,5,2,5,6,5]
# # # # subarr(arr,3)

# # # # def add_up(arr,total,i):
# # # #     if total == 0:
# # # #         return 1
# # # #     elif total<0:
# # # #         return 0
# # # #     elif i< 0:
# # # #         return 0
# # # #     elif total< arr[i]:
# # # #         return add_up(arr,total,i-1
# # # # arr = [1,3,4,5,2,5,6,5]

# # # # # find all subset total is 12

# # # # def add_up(arr,target,total=0):
# # # #     res_arr= []
# # # #     arr_tot = sum(arr)
# # # #     if total == target:
# # # #         res_arr.append(arr_tot)
# # # #     if total<= target: 
# # # #         for num in arr:
# # # #             arr.remove(num)
# # # #             add_up(arr,target-num,sum(arr))


# # # # def commonChild(s1, s2):
# # # #     # Write your code here
# # # #     i, j = 0,0
# # # #     def lcs(i,j):
# # # #         if i> len(s1)-1 or j >len(s2)-1: return 0
# # # #         if s1[i] == s2[j]:
# # # #             return 1 + lcs(i+1,j+1)   
# # # #         else:
# # # #            return  max(lcs(i+1,j),lcs(i,j+1))
        
# # # #     result = lcs(i,j)
# # # #     return result 

# # # # me =commonChild("alasfgcvbi","alimmm")
# # # # print(me)

# # # def all_pair(arr,target,all_me=[]):
# # #     if target == 0:
# # #         return []
# # #     if target < 0:
# # #         return None
# # #     for i in range(len(arr)):
# # #         temp = target - arr[i]
# # #         temp_res = all_pair(arr,temp)
# # #         if temp_res != None:
# # #            all_me.append( temp_res + [arr[i]])
# # #     return all_me
        
    



# # # arr= [1,2]
# # # # find all pair makes it 12 

# # # print(all_pair(arr,6))


# # # def maxSubsetSum(arr):
# # #     if len(arr) == 0:
# # #         return 0
# # #     if len(arr) == 1:
# # #         return arr[0]

# # #     max_subset = 0
    
# # #     for i in range(0,len(arr)):
# # #         num = [arr[i],]
# # #         num.append(maxSubsetSum(arr[i+2:]))
# # #         max_subset = max(sum(num), max_subset)
# # #     return max_subset
    
# # # arr = [3, 5, -7]
# # # m = maxSubsetSum(arr)
# # # print(m)

# # # def fib(n):
# # #     if n <= 2:
# # #         return 1
# # #     return fib(n-1) + fib(n-2)
# # # # 1 1 2 3 5 8
# # # print(fib(5))


# # # def fib2(n):
# # #     if n ==1 or n ==2:
# # #         return 1
# # #     arr = [1, 1 ,]
# # #     for i in range(2,n):
# # #         print(arr[0])
# # #         # print(i-2)
# # #         # arr[i] = arr[i-1] + arr[i-2]
# # #     # return arr[-1]

# # # print(fib2(5))

# # # def gridtraveler(x,y):
# # #     if x== 1 and y== 1: return 1
# # #     if x== 0 or y == 0: return 0
# # #     return gridtraveler(x-1,y)  + gridtraveler(x,y-1) 
# # # print(gridtraveler(2,3))


# # # def gridTraveler(x,y):
# # #     arr = [[0]*(x+1) for i in range(y+1)]
# # #     arr[1][1] = 1
# # #     for i in range(arr):
# # # #         for j in range(arr):
# # # #             arr[]

# # # for i in range(10,1,-1):
# # #     print(i)


# # # def getMinimumCost(k, c):
# # #     if k ==len(c):
# # #         return sum(c)
# # #     c.sort(reverse=True)
# # #     mul = 1
# # #     total = 0
# # #     for i in range(0,len(c),k):
# # #         for j in c[i:i+k]:
# # #             total += mul*j
            
# # #         mul +=1
# # #     return total

# # # c= [2, 5, 6]
# # # k =2 
# # # print(getMinimumCost(k,c))

# # # # should return 15

# # def minimalHeaviestSetA(arr):
# #     if len(arr)==1:
# #         return arr[0]
# #     if len(arr) ==2:
# #         if arr[0] != arr[1]:
# #             return max(arr)
# #         else:
# #             return arr 
# #     # Write your code here
# #     arr.sort(reverse=True)
# #     i = 0 
# #     size = len(arr)-1
# #     sub_a = []
# #     while i <  size:
        
# #         sub_b = []
# #         sub_a.append(arr[i])
# #         while arr[i] ==arr[i+1]:
# #             sub_a.append(arr[i])
# #             i += 1
# #         sub_b.extend(arr[i+1:])
# #         if sum(sub_a) > sum(sub_b):
# #             return sub_a
        
# #         i +=1

# # n  = [3,7,5,6,2]

# # print(minimalHeaviestSetA(n))
        

# # me = {2:3,4:5,}
# # print(min(me))

# # class Solution:
# #     def coinChange(self, coins, amount):
# #         dp = [amount + 1] * (amount + 1)
# #         dp[0] = 0
        
# #         for a in range (1, amount + 1):
# #             for c in coins:
# #                 if (a - c) >= 0:
# #                     dp[a] = min(dp[a], 1 + dp[a-c])
# #         return dp[amount] if dp[amount] != amount + 1 else -1

# # me = Solution()

# # print(me.coinChange([1,2,5],11))



# # from cmath import e
# # from re import L
# # from tkinter import N
# # from turtle import right


# # class Node:
# #     def __init__(self,val):
# #         self.right = None
# #         self.left = None
# #         self.val = val



# # a =Node(1)
# # b= Node(2)
# # c= Node(3)
# # d= Node(4)
# # e= Node(5)
# # f= Node(6)

# # a.left = b
# # a.right = c
# # b.left = d
# # b.right = e
# # c.right= f

# # # def dfs(root):
# # #     stack = [root,]
# # #     while len(stack) > 0:
# # #         last = stack.pop()
# # #         print("-->",last.val,end= "")
# # #         if last.right : stack.append(last.right) 
# # #         if last.left :stack.append(last.left)
        

# # # dfs(a)


# # # def deep(root):
# # #     if root == None: return []
# # #      left = deep(root.left)
# # #     right= deep(root.right)
# # #     return [root.val]+left+right
# # # print(deep(a))


# # # def empty(string):
# # # #     if string == "":
# # # #         return ""

# # # #     return string[-1] + empty(string[:-1])

# # # # a = empty("fuv you ali i hate my life")
# # # # print(a)


# # # def palindrome(string):
# # #     if string == "" or len(string)==1:
# # #         return True
# # #     if string[0] == string[-1]:
# # #         return palindrome(string[1:-1])
# # #     return False
# # # att = palindrome("kadyak")
# # # print(at


# # # def turn_to_binary(num,rem=[]):
# # #     if num == 1: 
# # #         rem.insert(0,num)
# # #         return 


# # #     new_no = num//2
# # #     rem.insert(0,num%2)
# # #     turn_to_binary(new_no,rem)
# # #     return rem
    



# # # print(turn_to_binary(13))

# # # def total(n):
# # #     if n == 1: return 1
# # #     return n + total(n-1)

# # # print(total(5))


# # # def binary_search(arr,target):
    
# # #     mid = len(arr) //2
# # #     if arr[mid] == target:
# # #         return True
# # #     if mid  <= 0 : return False
# # #     if arr[mid] > target:
# # #         return binary_search(arr[:mid],target)
    
# # #     return binary_search(arr[mid:],target)
    
# # # arr = [1,2,3,4,5,6,7,8,9,10,11]
# # # print(binary_search(arr,2))


# # # def binary_search(arr,target,left,right):
# # #     mid = (right+left) //2
# # #     if left > right:    return  False
# # #     if arr[mid] == target: return mid
# # #     if  arr[mid] < target: 
# # #         return binary_search(arr,target,mid+1,right)
# # #     return binary_search(arr,target,left,mid-1)
    
# # # arr= [1,2,3,4,5,6,7,8,9,10,]
# # # print(binary_search(arr,1,0,len(arr)))

# # def merge_sort(arr):
# #     if len(arr) == 1: return arr
# #     mid = len(arr)//2
# #     left = arr[:mid]
# #     right = arr[mid:]

# #     left_sort = merge_sort(left)
# #     right_sort = merge_sort(right)
# #     arr = two_arr(left_sort,right_sort)
# #     return arr

# # def two_arr(arr1,arr2):
# #     i = j= 0
# #     temp_arr = []
# #     while i < len(arr1) and j< len(arr2):
# #         if arr1[i]<arr2[j]:
# #             temp_arr.append(arr1[i])
# #             i+=1
# #         elif arr2[j] <= arr1[i]:
# #             temp_arr.append(arr2[j]) 
# #             j+=1
# #     while i< len(arr1):
# #         temp_arr.append(arr1[i])
# #         i+=1
# #     while j < len(arr2):
# #         temp_arr.append(arr2[j])
# #         j+=1

# #     return temp_arr

# # # a = [1,4,7]
# # # b= [3,6,8]

# # arr= [3,5,4,7,8,2,4,8]
# # print(merge_sort(arr))







# # from email import header


# # # def reverse_linked_list(linked_list):
# # #     if linked_list ==None or linked_list.next == None :
# # #         return linked_list

# # #     p = reverse_linked_list(linked_list.next)
# # #     linked_list.next.next = linked_list
# # #     linked_list.next = None

# # #     return p 


# # # def superDigit(n, k):
# # #     # Write your code here
# # #     new = str(n)*k
    
# # #     def dp(n):
# # #         if int(n)<10:
# # #             return n
# # #         me =0
# # #         for np in n:
# # #             me += int(np)
# # #         return dp(str(me))
# # #     return dp(new)

# # # print(superDigit(21,4))


# # grid = [[5,3,0,0,7,0,0,0,0],
# #         [6,0,0,1,9,5,0,0,0],
# #         [0,9,8,0,0,0,0,6,0],
# #         [8,0,0,0,6,0,0,0,3],
# #         [4,0,0,8,0,3,0,0,1],
# #         [7,0,0,0,2,0,0,0,6],
# #         [0,6,0,0,0,0,2,8,0],
# #         [0,0,0,0,1,9,0,0,5],
# #         [0,0,0,0,0,0,0,0,0]]

# # def possible(row, column, number):
# #     global grid
# #     #Is the number appearing in the given row?
# #     for i in range(0,9):
# #         if grid[row][i] == number:
# #             return False

# #     #Is the number appearing in the given column?
# #     for i in range(0,9):
# #         if grid[i][column] == number:
# #             return False
    
# #     #Is the number appearing in the given square?
# #     x0 = (column // 3) * 3
# #     y0 = (row // 3) * 3
# #     for i in range(0,3):
# #         for j in range(0,3):
# #             if grid[y0+i][x0+j] == number:
# #                 return False

# #     return True

# # # def solve():
# # #     global grid
# # #     for row in range(0,9):
# # #         for column in range(0,9):
# # #             if grid[row][column] == 0:
# # #                 for number in range(1,10):
# # #                     if possible(row, column, number):
# # #                         grid[row][column] = number
# # #                         solve()
# # #                         grid[row][column] = 0

# # #                 return
      
# # #     print(grid)
# # #     input('More possible solutions')

# # # solve()





# grid = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]

# # it is from 0 to 9 
# #  0 1 2 3 4 5 6 7 8
# def is_valid(x,y,target):
#     global grid
#     # horizontal
#     for row in grid:
#         if target == row[y]:
#             return False
#     # vertical
#     for col in grid[x]:
#         if target == col:
#             return False
#     # 3x3 grid
#     x0 = (y//3) *3
#     y0 = (x//3)*3
#     for i in range(0,3):
#         for j in range(0,3):
#             if target == grid[i+y0][j+x0]:
#                 return False
#     return True
# for i in range(1,10):
#     print(is_valid(0,8,i))

# def solve():
#     global grid
#     for i in range(9):
#         for j in range(9):
#             if grid[i][j] == 0:
#                 for num in range(1,10):
#                     if is_valid(i,j,num):
#                         grid[i][j] = num
#                         solve()
# #                         grid[i][j] = 0
# #                 return               
# # #     print(grid)

# # # solve() 
# # # print(grid)      
# # # 0,3 0,4 0,5
# # # 1,3 1,4 1,5
# # # 2,3 2,4 2,5
# # def dp(arr,target):
# #     if target < 0: return False
# #     if target == 0: return True
# #     okay = []
# #     for num in arr:
        
# #         left=  target -num
# #         ans = dp(arr,left)
# #         if ans:
# #             okay.append(num)

# #     print(okay)

# # arr = [2,4,5,3,6,7]
# # print(dp(arr,12))

# def depthFirst(graph,source):
#     stack = [source]

#     while  len(stack) > 0:
#         current = stack.pop()
#         print(current)
#         for neighbor in graph[current]:
#             stack.insert(0,neighbor)

# # graph ={
# #     "a":["c","b"],
# #     "b":["d"],
# #     "c":["e"],
# #     "d":["f"],
# #     "e":[],
# #     "f":[]
# # }

# depthFirst(graph,"a")



# def hasPath(graph,source,target):
#     if source == target: return True
#     for neigbor in graph[source]:
#         if hasPath(graph,neigbor,target):
#             return True
#     return False
#     # queue = [source]
#     # while len(queue) > 0:
#     #     current = queue.pop()
#     #     if current == target:
#     #         return True
#     #     for neigbors in graph[current]:
# #     #         queue.insert(0,neigbors)
# #     # return False

# # graph ={
# #     "f":["g","i"],
# #     "g":["h"],
# #     "h":[""],
# #     "i":["g","k"],
# #     "j":["i"],
# #     "k":[]
# # }
# # print(hasPath(graph,"g","h"))



# def buildPath(edges):
#     graph_dict = {}
#     for pair in edges:
#         if pair[0] in graph_dict:
#             graph_dict[pair[0]].append(pair[1])
#         else:
#             graph_dict[pair[0]] = [pair[1]]
#         if pair[1] in graph_dict:
#             graph_dict[pair[1]].append(pair[0])
#         else:
#             graph_dict[pair[1]] = [pair[0]]
#     return graph_dict

# def undirectedPath(graph,start,end,visited=[]):
#     if start == end:
#         return True
#     if start in visited: return False
#     stack = [start]
#     for neighbor in graph[start]:
#         visited.append(neighbor)
#         if undirectedPath(graph,neighbor,end,visited):
#             return True
# #     else:
# #         return False
        



# # edges = [
# #     ["i","j"],
# #     ["k","i"],
# #     ["m","k"],
# #     ["k","l"],
# #     ["o","n"]
# # ]
# # graph = buildPath(edges)
# # print(undirectedPath(graph,"k","n"))

# # def least_amount(coins,target):
# #     if target == 0: return []
# #     if target < 0: return None

# #     min_size = None
# #     for coin in coins:
# #         new_target = target-coin
# #         result = least_amount(coins,new_target) 
# #         if result !=None:
# # #             result.append(coin)
# # #         if min_size == None  :
# # #             min_size = result

# # #         else: 
# # #             if len(min_size)>len(result):
# # #                 min_size = result

        
# # #     return min_size
    

# # # coins = [5,1,2]
# # # print(least_amount(coins,11))


# # a = 1
# # while a < 3:
# #     print(f"while {a} ")
# # #     for i in range(2):
# # #         if i ==1: break
# # #         print(f"hello  {i} for")

# # #     a+=1


# # nums =[1,2,3,4,5,6,7,8,9]
# # a= 4
# # for i in range(a):
# #     print("hello")
# #     a+=1
# # print(a)


# def maximumUniqueSubarray( nums):
#     extra_dict = {}
#     start =  0
#     end = 1
#     max_score = 0
#     if len(nums)==1: return nums[0]
#     win_arr = [nums[0],]
#     while end< len(nums):
#         if nums[end] in win_arr:
#             if nums[end] in extra_dict:
#                 start = extra_dict[nums[end]]
#                 end+=1
#             else:
#                 extra_dict[nums[end]] = end
#         end +=1
#         win_arr = nums[start:end]
#         max_score = max(max_score,sum(set(win_arr)))
#     return max_score                



# arr =[4078,1065,3781,6541,304,9192,5474,3049,6281,385,1531,3194,7445,9453,6210,5165,6203,9272,6798,1719,6618,1580,3353,2387,5477,2289,8431,2653,6842,481,5777,4494,5935,7983,8983,9216,6897,3467,4598,6343,6429,7830,9543,1312,5491,5748,8252,4271,2345,1358,3924,741,1844,5695,322,3204,3815,1432,9226,3372,6007,3916,9402,5363,7240,9291,9821,3543,7215,3691,3149,5295,7813,3049,710,6500,4893,7063,4647,6865,7190,2844,7508,6811,7719,2916,3496,9861,5385,5655]
# print(maximumUniqueSubarray(arr))


# class Tries:
#     def __init__(self,word,):
#         self.word = word

#     def create(self):
#         for i in self.word:

# profit = [0,1,2,5,6]
# weight = [0,2,3,4,5]
# max_weight =8
# def  knapsack(n,c):
#     if n==0 or c==0 : return 0
#     if c < weight[n]:
#         return knapsack(n-1,c)
#     else:
#         temp1 = knapsack(n-1,c)
#         temp2 = profit[n] + knapsack(n-1,c-weight[n])
#         return max(temp1,temp2)

# me =knapsack(4,8)
# print(me)


# def optimize(arr):
#     arr.sort()
#     i = j =  len(arr)-1
    

#     while i>0 and j > 0:
#         if sum(arr[j:]) > sum(arr[:j]) and j != 0:
#             return arr[j:]
#         elif sum(arr[j:i]) < sum(arr[:j]):
#             j -=1
    




# # arr= [3,7,5,6,2]
# # arr = [4,5,6,5,5,7,8,2,1]
# # print(optimize(arr))


# def kth_permutaion(n,k):
#         permutation = []
#         unused = list(range(1,n+1))
#         fact = [1]*(n+1)
#         for i in range(1,n+1):
#             fact[i] = i*fact[i-1]
            
#         k -=1
#         while n>0:
#             part_length = fact[n]//n
#             i  = k// part_length
#             permutation.append(unused[i])
#             unused.pop(i)
#             n-=1
#             k %= part_length
#         return "".join(map(str,permutation))



# # kth_permutaion(3,3)
    
# # 0/1 knapsack 
# def dp(arr,n):
#     if n==0: return True
#     if n< 0: return False
#     for num in arr:
#         dp1 =dp(arr, n-num)
#         if dp1== True : return True
#     return False



# arr = [2,3,4]
# print(dp(arr,5))


# def dp(arr,n):
#     fact =[0]*(n+1)
    

# from typing import Tuple


# class TrieNode(object):
#     """
#     Our trie node implementation. Very basic. but does the job
#     """
    
#     def __init__(self, char: str):
#         self.char = char
#         self.children = []
#         # Is it the last character of the word.`
#         self.word_finished = False
#         # How many times this character appeared in the addition process
#         self.counter = 1
    

# def add(root, word: str):
#     """
#     Adding a word in the trie structure
#     """
#     node = root
#     for char in word:
#         found_in_child = False
#         # Search for the character in the children of the present `node`
#         for child in node.children:
#             if child.char == char:
#                 # We found it, increase the counter by 1 to keep track that another
#                 # word has it as well
#                 child.counter += 1
#                 # And point the node to the child that contains this char
#                 node = child
# #                 found_in_child = True
# 
# #                 break
# #         # We did not find it so add a new chlid
# #         if not found_in_child:
# #             new_node = TrieNode(char)
# #             node.children.append(new_node)
# #             # And then point node to the new child
# #             node = new_node
# #     # Everything finished. Mark it as the end of a word.
# #     node.word_finished = True


# # def find_prefix(root, prefix: str) -> Tuple[bool, int]:
# #     """
# #     Check and return 
# #       1. If the prefix exsists in any of the words we added so far
# #       2. If yes then how may words actually have the prefix
# #     """
# #     node = root
# #     # If the root node has no children, then return False.
# #     # Because it means we are trying to search in an empty trie
# #     if not root.children:
# #         return False, 0
# #     for char in prefix:
# #         char_not_found = True
# #         # Search through all the children of the present `node`
# #         for child in node.children:
# #             if child.char == char:
# #                 # We found the char existing in the child.
# #                 char_not_found = False
# #                 # Assign node as the child containing the char and break
# #                 node = child
# #                 break
# #         # Return False anyway when we did not find a char.
# #         if char_not_found:
# #             return False, 0
# #     # Well, we are here means we have found the prefix. Return true to indicate that
# #     # And also the counter of the last node. This indicates how many words have this
# #     # prefix
# #     return True, node.counter

# # if __name__ == "__main__":
# #     root = TrieNode('*')
# #     add(root, "hackathon")
# #     add(root, 'hack')

# #     print(find_prefix(root, 'hac'))
# #     print(find_prefix(root, 'hack'))
# #     print(find_prefix(root, 'hackathon'))
# #     print(find_prefix(root, 'ha'))
# #     print(find_prefix(root, 'hammer'))



# # def me(x):
# #     assert x>10 , "Invalid"

# #     print(x)

# # me(21)
 

# def rob(nums):
#     rob1 = rob2 = 0
#     for n in nums:
#         temp = max(n+rob1,rob2)
#         rob1= rob2
#         rob2 = temp 

#     return rob2

# print(rob([1,2,3,4,1,1]))



def maxAlt(nums):
    dp ={}

    def dfs(i,even):
        if i==len(nums):
            return 0
        if (i,even) in dp:
            return dp[(i,even)]
        total = nums[i] if even else (-1*nums[i])
        dp[(i,even)] = max(total+ dfs(i+1,not even), dfs(i+1,even))
        return dp[(i,even)]
    
    a =  dfs(0,True)
    print(dp)
    return a
arr = [4,2,5,3]
maxAlt(arr)