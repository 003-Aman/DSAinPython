#all levels are completed except the lowest one which is filled from the left
#as it is filled from the left it will lean towards the left
# the last leaf element might not have a right sibling
#look at the comparisons between them

'''
how a complete binary tree is created
in an array:
select the first element as the node
the next two will be the child left and right
the next two will be the children of the left and the two after that will be the children of the right
keep repeating until the last element

'''
'''
Relationship between array indexes and tree element
A complete binary tree has an interesting property that we can use to find the children and parents of any node.

If the index of any element in the array is i, the element in the index 2i+1 will become the left child and element in 2i+2 index will become the right child.
Also, the parent of any element at index i is given by the lower bound of (i-1)/2.
'''
#used in heaps and heap sort too
class Node:
    def __init__(self,item):
        self.item = None
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    return (1+count_nodes(root.left)+ count_nodes(root.right))

def is_complete(root,index,numberNodes):
    if root is None:
        return True

    if index >= numberNodes:
        return False
    return (is_complete(root.left, 2*index +1, numberNodes) and is_complete(root.right, 2*index +2,numberNodes))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

node_count = count_nodes(root)
index =0

if is_complete(root,index,node_count):
    print("the tree is a complete binary tree")
else:
    print("the tree is not a complete binary tree")    
