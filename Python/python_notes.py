'''

BIG O NOTATION LOOK UP BFS AND DFS

'''

##############################  O(1)  ############################

# Array
nums = [1,2,3]
nums.append(4)  #push to end
nums.pop()      #pop from end
nums[0]         #lookup
nums[1]
nums[2]

# Hashmap/set
hashMap = {}
hashMap["key"] = 10     #insert
print("key" in hashMap) #lookup
print(hashMap["key"])   #lookup
hashMap.pop("key")      #remove

mySet = set() 
mySet.add(5)            #insert
print(5 in mySet)       #lookup
mySet.remove(2)         #remove


#Queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()

queue.appendleft(1)

queue.pop()





############################  O(n) ###############################
nums = [1,2,3]
sum(nums)           #sum of array
for n in nums:      #looping
    print(n)

nums.insert(1,100)  #insert middle
nums.remove(100)    #remove middle
print(100 in nums)  #search

import heapq
heapq.heapify(nums) #build heap

#sometimes even nested loops can be O(n), e.g. monotonic stack or sliding window







############################  O(n^2) ###############################

#Traverse a square grid
nums = [[1,2,3], [4,5,6], [7,8,9]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(nums[i][j])

#Get every pair of elements in array
nums = [1,2,3]
for i in range(len(nums)):
    for j in range(i+1, len(nums[i])):
        print(nums[i],nums[j])

# Insertion sort (insert in middle n times -> n^2)



############################  O(n*m) ###############################

#Get every pair of elements from two arrays
nums1, nums2 = [1,2,3], [4,5]
for i in range(len(nums1)):
    for j in range(len(nums2)):
        print(nums1[i],nums2[j])

#Traverse rectangle grid
nums = [[1,2,3], [4,5,6]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        print(nums[i][j])


############################  O(logn) ###############################

#Binary search
nums = [1,2,3,4,5]
target = 6
l, r = 0, len(nums) - 1
while l <= r:
    m = (l + r) // 2
    if target < nums[m]:
        r = m - 1
    elif target > nums[m]:
        l = m + 1
    else:
        print(m)
        break


#Binary search on BST
def search(root,target):
    if not root:
        return False
    if target < root.val:
        return search(root.left, target)
    elif target > root.val:
        return search(root.right, target)
    else:
        return True

# Heap Push and Pop
import heapq
minHeap = []
heapq.heappush(minHeap, 5)
heapq.heappop(minHeap)



############################  O(nlogn) ###############################

#HeapSort
import heapq
nums = [1,2,3,4,5]
heapq.heapify(nums) #O(n)
while nums:
    heapq.heappop(nums) #O(logn)
#Overall run time is O(nlogn)



#MergeSort
#(and most built-in sorting functions)


############################  O(logn) ###############################
#Recursion, tee height n, two branches
def recursion(i, nums):
    if i == len(nums):
        return 0
    branch1 = recursion(i + 1, nums)
    branch2 = recursion(i + 2, nums)



'''

DATA STRUCTURES

'''

############################  BFS ###############################
from collections import deque

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E', 'F'],
  'C' : ['G'],
  'D' : [],
  'E' : [],
  'F' : ['H'],
  'G' : ['I'],
  'H' : [],
  'I' : []
}

def bfs(graph,node):
    visited = []
    queue = deque()

    visited.append(node)
    queue.append(node)

    while queue:
        #popleft is O(1)
        s = queue.popleft()
        print(s)

        for n in graph[s]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

def main():
    bfs(graph, 'A')

main()


############################  DFS ###############################
graph = {
    'A': ['B', 'G'],
    'B': ['C', 'D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['I'],
    'I': [],
}

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = []

    visited.append(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def main():
    dfs_recursive(graph, 'A')

main()




'''

PYTHON NOTES

'''

# Custom sort (in this case by length of string)
arr = ["bob", "alice", "jane", "doe"]
arr.sort(key=lambda x:len(x))

# List comprehension
arr = [i for i in range(5)] #returns [0,1,2,3,4,5]

#ASCII Values
print(ord("b")) #97

#Combine a list of strings (with an empty string delimiter)
strings = ["ab", "cd", "ef"]
print("".join(strings)) #returns abcdef


# Looping through maps
myMap = {"alice" : 90, "bob": 70}

for key in myMap:
    print(key, myMap[key]) # returns alice 90
                           #         bob 70

for val in myMap.values():
    print(val)             # returns 90
                           #         70

for key,val in myMap.items():
    print (key,val)        # returns alice 90
                           #         bob 70


# Tuples (like arrays but immutable, can be used as key for hashmap/set)
tup = (1,2,3)
print(tup[0])

myMap = {(1,2): 3}

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

#Lists cant be key


#No max heaps by default, work around is use min heap and multiply by -1 when push and pop
import heapq

maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap,-2)

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))


# Enumerate
for i, n in enumerate(arr):
    arr[i] *= 2

# Class
class MyClass:
    #Constructor
    def __init__(self,nums):
        #Create Member variables
        self.nums = nums
        self.size = len(nums)

    #self keyword required as param
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()
    

'''
LEETCODE EXAMPLES
'''

############################  BFS ###############################
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        if not grid:
            return 0

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands
    
############################  DFS ###############################
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c,visit,prevHeight):
            if ((r,c) in visit or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r + 1,c,visit,heights[r][c])
            dfs(r - 1,c,visit,heights[r][c])
            dfs(r,c + 1,visit,heights[r][c])
            dfs(r,c - 1,visit,heights[r][c])

        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
                
        return res
