#also known as a height-balanced binary tree
#a binary tree in which the height of the left and right subtree of any node differ by not more than 1
# the difference between the value in the left and right subtree is not more than one
#the left subtree is balanced
#the right subtree is balanced


#df = height of left child - height of right child

'''Balanced Binary Tree Applications
AVL tree
Balanced Binary Search Tree'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

class Height:
    def __init__(self):
        self.height =0

def isHeightBalanced(root,height):
    left_height = Height()
    right_height = Height()


    if root is None:
        return True
    
    l=isHeightBalanced(root.left,left_height)
    r=isHeightBalanced(root.right, right_height)

    height.height = max(left_height.height,right_height.height)+1

    if abs(left_height.height - right_height.height)<=1:
        return l and r
    
    return False


height = Height()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

if isHeightBalanced(root,height):
    print("the tree is balanced")
else:
    print("the tree is not balanced")    