'''
A tree is a non linear hierarchical data structure
in linear data structures like array,LL,stack and queues the time complexity increases with size

A tree consists of node and edges. edges is the link between the nodes and you know what a node is
a tree consists of depth and height, as height increases depth decreases and as depth increases height decreases
inversely proportional to each other

Degree is the total number of branches of that node

Forest is the collection of disjoint trees which we ccan create by cutting the root of a tree

Types:
Binary tree, binary search tree, avl tree, b-tree
'''
#Applications
'''
Tree Applications
Binary Search Trees(BSTs) are used to quickly check whether an element is present in a set or not.
Heap is a kind of tree that is used for heap sort.
A modified version of a tree called Tries is used in modern routers to store routing information.
Most popular databases use B-Trees and T-Trees, which are variants of the tree structure we learned above to store their data
Compilers use a syntax tree to validate the syntax of every program you write.
'''

#Tree traversal
'''
Linear data structures like arrays, stacks, queues, and linked list have only one way to read the data. 
But a hierarchical data structure like a tree can be traversed in different ways.

a tree has: a node carrying data and two subtrees(left and right)
'''
#types of traversal
'''
1.inorder traversal: left subtree->node->right subtree
2.preorder traversal: root->left->right
3.postorder traversal: left ->right->node

'''

#Tree traversal 

class Node:
    def __init__(self,item):
        self.val = item
        self.left = None
        self.right = None

def inorder(root): #l,n,r
    if root:#which checks if there is a root and returns true
        inorder(root.left)#traverse left
        print(str(root.val) + "->", end="")
        inorder(root.right)        
def postorder(root):#l,r,n
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val)+ "->", end ="")   

def preorder(root):#n,l,r
    if root:
        print(str(root.val)+ "->", end ="") 
        postorder(root.left)
        postorder(root.right) 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)        
