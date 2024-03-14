#heap and hash are ofc different
'''
heap is a complete binary tree that satisfies the heap property:
Max heap :parent is always greater than child and the key(key and value) of the root node is the largest among all the nodes
Min heap : exactly the opposite

'''

#Heap operations
'''
Heapify:making an unarranged tree/array to a max heap or min heap
1. take an array
2. make a binary tree from the array in procedural index(make the diagram to understand it)
3.Start from the index of the non-leaf node whose index is given by n/2-1
non -leaf node bhaneko last node ko parent raixa haldai jada ko
'''

"""
Heap Data Structure Applications
Heap is used while implementing a priority queue.
Dijkstra's Algorithm
Heap Sort


"""
#This is a max heap
def heapify(array, size, index):#this fuction takes the array representing the heap, the size of the heap and the index of the current node
    largest = index #largest is set to index which represents the index of the largest element among the current node and its children
    left = 2*index +1 # this can be seen using the heap diagram that its true always
    right = 2*index+2

    if left < size and array[index]<array[left]:#it checks if the left exists by left<size and if its value is greater
        largest = left # if it is, it updates it

    if right < size and array[index]<array[right]:#same shit
        largest = right     


    if largest != index: #now this will swap the current element with the left or right before value matrai set vathyo
        array[index], array[largest]=arr[largest],array[index]
        heapify(array,size,largest)# this time its not index but the largest being put in as a parameter
        #again recursively it is called until it meets all the conditions meaning largest = index

def insert(array, newNum):#this needs an empty array at first and then we keep on inserting to make it longer or we can give a bigger array directly at first doesnt matter
    size = len(array)
    if size ==0:# if no elements have been inserted yet
        array.append(newNum)#khurukka append

    else:
        array.append(newNum)#but paila xa vane append
        for i in range((size//2)-1,-1,-1):#and then heapify specifically max-heapify
            #the loop iterates over the parent nodes of the last inserted element and calls 'heapify' on each parent node
            heapify(array, size,i) #\


def deleteNode(array,num):
    size =len(array)
    i =0
    for i in range(0,size):#searches for the element to be deleted in the heap
        if num == array[i]:
            break

    array[i], array[size-1] = array[size -1],array[i]#once found it removes the last element from the heap using the remove method
    array.remove(num)

    for i in range((len(array)//2)-1,-1,-1):
        heapify(array,len(array),i)#now we heapify again


arr=[]    
insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))   


