'''
Priority Queue Applications



Dijkstra's algorithm
for implementing stack
for load balancing and interrupt handling in an operating system
for data compression in Huffman code
'''
#Priority queue using heap data structure
#heap is a complete binary tree(can only have two children elements) that satisfies the heap property
#max heap(parent element has maximum value) and min heap(parent element has minimun value)

#doesnt matter if the left child is bigger or smaller than the right the heap just has to have its root node bigger or smaller than the children nodes
#Recursion is being used
#Algorithm
"""
Heapify(array, size, i)
  set i as largest (i is the index of the non-leaf node)
  leftChild = 2i + 1 #index of the leftChild
  rightChild = 2i + 2 #index of the rightChild try it using diagram
  
  if leftChild > array[largest]
    set leftChildIndex as largest
  if rightChild > array[largest]
    set rightChildIndex as largest

  swap array[i] and array[largest]

"""

#To create max-heap
"""
MaxHeap(array, size)
  loop from the first index of non-leaf node down to zero
    call heapify


For Min-Heap, both leftChild and rightChild must be larger than the parent for all nodes.    
"""

#Insert element into Heap
"""
If there is no node, 
  create a newNode.
else (a node is already present)
  insert the newNode at the end (last node from left to right.)
  
heapify the array

"""

#Delete Element from Heap
"""
If nodeToBeDeleted is the leafNode
  remove the node
Else swap nodeToBeDeleted with the lastLeafNode
  remove noteToBeDeleted
   
heapify the array
"""

#Peek(Find max/min)
"""
Peek operation returns the maximum element from Max Heap or minimum element from Min Heap without deleting the node.

For both Max heap and Min Heap

    return rootNode
"""

#Extract -Min/Max
"""
Extract-Max returns the node with maximum value after removing it from a Max Heap whereas Extract-Min returns the node with minimum after removing it from Min Heap.
"""

#Actual Implementation with code
#max-heap data structure in Python
def heapify(arr,n,i): #heap in the form of an array, size of array/heap,index of the parent/current node
    largest =i# setting index of the largest node i.e the parent node to i
    l = 2*i+1 # the leftChild will have index this l
    r = 2*i+2 # the rightChild will have index this r

    if l<n and arr[i] < arr[l]: #if left child exists(l<n) and its value is greater than the parent, 
        largest =l  #update largest to the index of the left child

    if r<n and arr[largest]<arr[r]: # if the right child exists do the same shit
        largest =r 

    if largest != i:#if largest is not equal to parent index
        arr[i],arr[largest]= arr[largest],arr[i] # swap the values of parent and the child with the largest value
        heapify(arr, n, largest) #recursively call heapify on the affected child node

def insert(array, newNum):
    size = len(array)
    if size ==0: #if array is empty
        array.append(newNum)# just append it to the array
    else:
        array.append(newNum) #otherwise, append the new number to the array and then loop through the array 
        for i in range((size//2)-1, -1, -1): #starting from the parent of the last element(size//2)and going up to the root
            heapify(array, size, i)#for each iteration ,call heapify on the current parent node  

def deleteNode(array, num):
    size = len(array)
    i =0
    for i in range (0, size):
        if num == array[i]:#find the index of the element to be deleted in the array
            break

    array[i], array[size-1]= array[size -1],array[i]#swap the element to be deleted with the last element in the array
    array.remove(num) #remove the last element from the array

    for i in range((len(array)//2)-1,-1,-1):#loop through the array starting from the parent of the last element (len(array)//2) and going up to the root
        heapify(array, len(array), i) # for each iteration call heapify on the current parent node

arr =[]


insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
