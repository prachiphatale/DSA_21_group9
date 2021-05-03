# -*- coding: utf-8 -*-

### This Python Program is meant to determine the manual value of 
### the Minimum Range Query of a Segment Tree

### Compiled by. Abiola Anderson & Prachi Prashant Phatale

import sys;
from math import ceil,log2;
import numpy as np
import time
  
MAXVal = sys.maxsize;


## Import text file treat as number list
def readInfoText():
    file = open("8388608int.txt","r")
    #file = open("1048576int.txt","r")
    #file = open("524288int.txt","r")
    #file = open("262144int.txt","r")
    #file = open("131072int.txt","r")
    #file = open("65536int.txt","r")
    #file = open("32768int.txt","r")
    #file = open("16384int.txt","r")
    #file = open("8192int.txt","r")
    #file = open("4192int.txt","r")
    #file = open("4096int.txt","r")
    #file = open("1024int.txt","r")
    #file = open("512int.txt","r")
    #file = open("128int.txt","r")
    #file = open("32int.txt","r")
    #file = open("8int.txt","r")
    numbers = []
    for number in file:
        numbers.append(int(number))
    return numbers
 
# A utility function to get minimum of two numbers 
def minVal(x, y) :
    return x if (x < y) else y; 
  
# A utility function meant to determine the position of
# the middle index from corner indexes. 
def midPt(m, a) :
    return m + (a - m) // 2; 
  
""" 
A recursive function is used to find the minimum value in a given range 
of array indices. 

Function Parameters;
  
    seg st: indcates the given segment tree.
    
    ind: Index of current node in the segment tree. Initially 0 is passed as 
            the root is always at index 0 given the size of the datase.
            
    start & end: This shows the Start and end points within a given index 
            of the segment which is seen in current node, i.e., seg[ind].
            
    qst & qbr: Starting and ending indexes of query range 
"""
def RMQUtil( seg, start, end, qst, qbr, ind) :
  
    # If segment of this node is within the range limit, the min of the segment 
    # will be returned
    if (qst <= start and qbr >= end) :
        return seg[ind]; 
  
    # If segment of this node is outside the given range 
    if (end < qst or start > qbr) :
        return MAXVal; 
  
    # If segment component overlaps with the range return the minimum value
    mid = midPt(start, end); 
    return minVal(RMQUtil(seg, start, mid, qst, qbr, 2 * ind + 1), 
                  RMQUtil(seg, mid + 1, end, qst, qbr, 2 * ind + 2)); 
  
# Return minimum of elements in range from index qst (query start) to qbr (query 
# end). It mainly uses RMQUtil() 
def RMQ( seg, o, qst, qbr) : 
  
    # Make sure input values can be defined
    if (qst < 0 or qbr > o - 1 or qst > qbr) : 
        print("Invalid Input, Undefined"); 
        return -1;     
    return RMQUtil(seg, 0, o - 1, qst, qbr, 0); 
  
# A recursive function that constructs Segment Tree for array[start..se]. si is 
# index of current node in segment tree seg 
def buildUtil(arr, start, end, seg, si) :
  
    # If there is one element in array, store it in current node of segment tree and return 
    if (start == end): 
        seg[si] = arr[start]; 
        return arr[start]; 
  
    # If there are more than one elements, then recur for left and right subtrees and
    # store the minimum of two values in this node 
    mid = midPt(start, end); 
    seg[si] = minVal(buildUtil(arr, start, mid, seg, si * 2 + 1),
                    buildUtil(arr, mid + 1, end, seg, si * 2 + 2)); 
    return seg[si]; 
  
"""
Function to construct segment tree from an array. 
This function allocates memory for segment tree and fills the allocated memory 
"""
def buildST(arr, o) :
    # Allocate memory for segment tree by;
  
    # finding the Height and maximum of the segment tree fill the menmory then 
    # return the constructed tree.
    x = (int)(ceil(log2(o)));  
    max_size = 2 * (int)(2**x) - 1; 
    seg = [0] * (max_size); 
    buildUtil(arr, 0, o - 1, seg, 0);  
    return seg; 
  
# Driver Code
start = time.time()

if __name__ == "__main__" : 
    numbers = readInfoText()
    ### Driver code to test above 
    # Build segment tree from given array,  
    # Starting index of query range & Ending index of query range, 
    # Print minimum value in arr[qst..qbr]
    
    arr = numbers
    o = len(arr);
   
    sl = buildST(arr, o); 
    
    qst = int(input("Enter your min: "))
    qbr = int(input("Enter your max: "))
    
    rangeV = RMQ(sl, o, qst, qbr)
    rangeL = np.arange(qst, qbr).tolist()           
    rangeQ = arr[qst : qbr]
    
    print("Range of a given value;", rangeQ)
    rangeQ.sort() 
    
    print("Ordered list of a given range;", rangeQ)
    print("Minimum of value in range [", qst, ",", qbr, "]", "is =", rangeV);

end = time.time()
Runtime = end - start
print("Time Lapsed;", Runtime,"ms")
   