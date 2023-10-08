# Python is dynamicly typed
n, m = 10, "abc"
# print(n)
n, m, z = 10.12, "asbc", True
print(n,m)

n += 1

# NULL is None in python
# and - &&, or - ||, also parentheses need for multi line conditions

n = None
print("n =", n)
x = 1
if x > 2:
    print("X is bigger than 2")
elif (x < 2
      and x > 0 ) :
    print("X is in b/w 0 and 2")
else:
    print(" X is smaller than 1")

z = 0
while(z < 3): # parenthese we can use but not neccessary
    print(z)
    z+=1

# # Looping from i = 0 to i = 4

for i in range(5):
    print(i)

for i in range(2,6):# including 2 but excluding 6
    print("I:",i)

for x in range(5,1,-1):#including 5 but not including 1, decrementing by 1 (-1)
    print("X:",x)

print(5/2) # auto decimel point answer gonna be 2.5
print(5//2) # now it'll do int divide - 2x
print(-3//2) #  - 2 - it go down however most lang it goes toward 0 automatically
print(-int(3/2)) #  - 1 - to go thru it and to get from decimal to int it will work like other
print(10%3)
# # -ve value doesn't work as expected
# print(- 10 % 3 ) # gave us 2 should've been -1

# # work around for module
import math

print(math.fmod(-10,3))
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(3,2))
# print( math.pow(2,1000) < float("inf"))

# Arrays are called list in python and used as ofter as hashmaps
arr = [1,2,3] 
arr.append(4)
arr.append(5)
print(arr)
arr.pop()
print(arr)

arr.insert(1,1.2) # big o of n  
print(arr)
arr.insert(3,4) # put third element in the arr list the number 4
print(arr)
arr[0] = 0
arr[1] = 0
print(arr)
#  creating array of size 5 with all 1's

# n = 5
arr1 = [1]*5
arr2 = [i for i in range(5)]
print(arr1)
print(arr2)
print(len(arr))
# arr[4] = 4
# # reading last value of arr by indexing
print(arr2[-1])

# # imprtant useful feature, last index is non inclusive
print(arr2[1:4])
# print(arr[4:5])
# print(arr)
# # number of array elements need to same as number of variable
a, b, c =[1,2,3]
print(a,b,c)
# print(a)
# with index
for i in range(len(arr2)):
    print(arr2[i])
# without index 
for i in arr2:
    print(i)

# we can get index and value with enumerate
for i, n in enumerate(arr2):
    print(i,n) # i is index and n is numner

# looping thru multiple array simultaneously with unpacking

nums1 = [1,2,3]
nums2 = [2,3,4]
for n1,n2 in zip(nums1, nums2):
    print(n1,n2)
# # reversing is as easy as calling reverse()
nums1.reverse()
print(nums1)

# #  sorting just as easy in ascenfing order by default
nums1.sort()
print(nums1)

# #  for desceding order
nums1.sort(reverse=True)

print(nums1) 
# need to take care for uppercase and lowercase since uppercase are smaller number 
arrr = ["Karan", "Alice","Bob","Kbran","Kbsan"]
arrr.sort()
print(arrr)
# lambda parameters:experssion
age_check = lambda age: True if age >= 18 else False

print(age_check(18))

print(arrr.sort(key=lambda x:len(x)))

print(arrr)

# List comprehension
# arr4 = [i for i in range(5)]
# print(arr4)
# arr5 = [i+1 for i in range(5)]
# print(arr5)
# arr6 = [i*i for i in range(5)]
# print(arr6)

# 2-d list
 
arr2d = [[0]*4 for i in range(4)]

print(arr2d)
# # this one changes all value of inside array even if even change one of them
arr2d2 = [[0]*4]*4
print(arr2d2)
arr2d2[0][1] = 2
arr2d[0][1] = 2
print(arr2d)
print(arr2d2)

s = "abc" # strings are immutable
print(s[0:2])

# adding new character to the string create new string making it O(n)
s+= "DEF"
print(s)

print(int("123")+int("124"))
print(str(12)+str(124))
# to get the askii value of character 
print(ord("a"))
print(ord("b"))

#  empty string delimitor to join strings in list
strings = ["Ka","ran", "Bhas","kar"] 
print("".join(strings)) # KaranBhaskar returns

# queue is basically .pop(0) so we remove from 0 index but it is slow and big(O)

from collections import deque 
# # it is done with constant time
data = deque()
data.append("Karan")
data.append("Bhaskar")
print(data)
data.popleft()
print(data)
data.appendleft("MR.Karan")
print(data)

# Creating custom stack using classes
# underscore_data good convestion to say we aern't supposed to view it
class Stack:
    def __init__(self):
        self._data = []
    
    def push(self,data):
        self._data.append(data)
    def pop(self):
        return self._data.pop()
    
stack = Stack()
stack.push(10)
 
#  HashSet  -  all are constant time
mySet = set()

mySet.add(1)
mySet.add(2)

print(mySet)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)
# in intro to comp science class
# def fact(num):
    # if(num==1):
#         return 1
#     return fact(num-1)*num

# print(fact(10))

# Hash table is using key instead of index - basically object in js ig
data = {}
data[3] = "Karan Bhaskar"

print(data)
# from collections import OrderedDict

# data  = OrderedDict()
# data.name  = "Karan"
# print(data.name)

print(set([1,2,3]))
mySet = {i+1 for i in range(5)}
print(mySet)

myMap = {}
myMap["alice"] = 88
myMap["bob"] = 88

print(myMap)
print(len(myMap))

print("alice" in myMap)
myMap.pop("alice")
print("alice" in myMap)

myMap1 = {i: i*2 for i in range(3)}
print(myMap1)

myMap3 = {"karan": "W","apex": "L"}
for key in myMap3:
    print(key, myMap3[key])

for val in myMap3.values():
    print(val)

for key, val in myMap3.items():
    print(key, val)
# can't modify them 
# tup = (1,3,4)

# print(tup)
# print(tup[0])
# print(tup[-1])

import heapq

# # they are arrays under the hood
miniHeap = []

heapq.heappush(miniHeap, 10)
heapq.heappush(miniHeap, 1)
heapq.heappush(miniHeap, 8)
# # min is always ate index 0 
print(miniHeap) 

while len(miniHeap):
    print(heapq.heappop(miniHeap))

# # work around to get max heap is mulitply bu -1
maxHeap = []
heapq.heappush(maxHeap,-3)
heapq.heappush(maxHeap,-2)
heapq.heappush(maxHeap,-1)

print(-1*maxHeap[0])
while len(maxHeap):
    print(-1*heapq.heappop(maxHeap))

arr10 = [2,1,4,2,4,5,63,34,2]

heapq.heapify(arr10)

while arr10:
    print(heapq.heappop(arr10))

#  nested functions
def someFunction(a,b,arr):
#     #  we can change the arr
    def someNestedFunction():
        for i in range(len(arr)):
            arr[i] = b
#         # but for variable we need to need to use local keyword for outside
            nonlocal a
            a = b
    someNestedFunction()
    print(a,b,arr)

nums = [1,2,3]
a = 1
b = 2

someFunction(a,b,nums)
    
class SomeClass:
    def __init__(self,num):
        self.num = num
        self.size  =  len(num)
    
    def getLength(self):
        print(self.size)
    
