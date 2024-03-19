#it helps to maintain a sorted list of numbers
# it is called search tree because it can be used to search for the presence of a number in 0(log(n)) time

#this is different from regular binary tree
#all nodes of left subtee are less than the root node
#all nodes of right subtree are more than root node
#both subtrees of each node are also BST i.e they have the above two properties



'''
Visualize this shit

we move forward by going left or right
if we have to find 4
we search the root first which might be more or less than 4, we move right , now again we compare to 4, similarly now you might move left, until and unless 4 is found


Insertion
this will be somewhat similar look at the value of the node that you want to compare and keep on moving, and add where you reach at last, left,right, left, right , insert'


Deletion operation
case1:
if the node to be deleted in a binary search tree is a leaf node, which means it is the bottommost node, simply remove it since all the other nodes will be arranged according to need

case2:
if it has a single child node, try to visualize
replace that node with its child node
remove the child node from its original position, for this you have to copy the value

case3:
if the node to be deleted has two children
get the inorder successor of that node, which i think means a node anywhere in the tree which holds the value just greater than that node
replace the node with the inorder successor
remove the inorder successor from its original position


lets look at the code now
'''


class Node:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left) 

    print(str(root.key) + '->', end = " ")
    inorder(root.right) 

# Binary Search Tree operations in Python


# Create a node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Inorder traversal
def inorder(root):
    if root is not None:
        # Traverse left
        inorder(root.left)

        # Traverse root
        print(str(root.key) + "->", end=' ')

        # Traverse right
        inorder(root.right)


# Insert a node
def insert(node, key):

    # Return a new node if the tree is empty
    if node is None:
        return Node(key)

    # Traverse to the right place and insert the node
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

def minValueNode(node):
    current = node

    while(current.left is not None):
        current = current.left# i think we are traversing in a tree

    return current

def deleteNode(root,key):
    if root is None:
        return root
    
    if key<root.key:
        root.left = deleteNode(root.left,key)

    elif key>root.key:
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
    #if temp node has two children
    #place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)

        root.key = temp.key

        #delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root

root = None
root = insert(root,8)
root = insert(root,3)
root = insert(root,1)
root = insert(root,6)
root = insert(root,7)
root = insert(root,10)
root = insert(root,14)
root = insert(root,4)

print("Inorder traversal: ", end=" ")
inorder(root)

print('\nDelete 10')
root = deleteNode(root,10)

print("Inorder traversal: ",end=" ")
inorder(root)

    
