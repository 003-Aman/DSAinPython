#a perfect binary tree is a binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level
#all the internal nodes have a degree of two
#Recursively, a perfect binary tree can be defined as:

#If a single node has no children, it is a perfect binary tree of height h = 0,
#If a node has h > 0, it is a perfect binary tree if both of its subtrees are of height h - 1 and are non-overlapping.


#checking if a binary tree is perfect binary tree

class newNode:
    def __init__(self,k):
        self.key = k
        self.right = self.left = None


def calculateDepth(node):
        d=0
        while(node is not None):
            d += 1#after increasing the depth
            node = node.left # go to the left node
        return d #if there is no node just return the initial depth which is 0
    
def is_perfect(root,d,level =0):
        #check if the tree is empty
        if (root is None):
            return True
        
        if (root.left is None and root.right is None):
            return (d==level+1)#this returns a boolean
        
        if(root.left is None or root.right is None):
            return False
        
        return (is_perfect(root.left,d,level+1) and is_perfect(root.right, d, level +1))

root = None
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)

if(is_perfect(root,calculateDepth(root))):
    print("The tree is a perfect binary tree")

else:
    print("the tree is not a perfect binary tree")    