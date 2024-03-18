#every parent node/internal node has either two or no children
#also known as a proper binary tree
#leaves are the nodes that no not have any children
#internal nodes are the ones which have atleast one chidren except the root node
'''
Full binary tree theorems
let, 
i = the no. of internal nodes
n = the total no. of nodes
l = no. of leaves
λ = number of levels
'''
class Node:
    def __init__(self,item):
        self.item = item
        self.leftChild = None
        self.rightChild = None

def isFullTree(root):
    if root is None:
        return True

    if root.leftChild is None and root.rightChild is None:
        return True

    if root.leftChild is not None and root.rightChild is not None:
        return (isFullTree(root.leftChild) and isFullTree(root.rightChild))  
    #basically jun value hamle provide garxam left ra right ko check gareko gare garxa until it does have one, recursion

    return False #left xa right xaina vane false or vice versa

root = Node(1)
root.rightChild = Node(3)
root.leftChild = Node(2) 
root.leftChild.leftChild = Node(4)
root.leftChild.rightChild = Node(5)
root.leftChild.rightChild.leftChild = Node(6)
root.leftChild.rightChild.rightChild = Node(7)

if isFullTree(root):#which means if it returns true
    print("The tree is a binary full tree")
else:
    print("The tree is not a binary tree")    