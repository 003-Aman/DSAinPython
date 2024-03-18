#a binary tree has node and it has two children
#it has a data item, a left node and a right node

'''
types of tree:
full binary tree: all nodes hace two children or none including the last
perfect binary tree: every node has two children expect the ones which are at last(height =0)
complete binary tree: the last leaf element might not have a right sibling, and the leaf elements must lean towards the left
Degenerate or pathological tree:every node has only one child, either the left or the right
skweed binaary tree: left - skewed and right skewed binary tree
every node has only one node and all are left or all are right
balanced binary tree: tree in which the difference between the height of the left and the right subtree for each node is either 0 or 1

'''
'''Binary Tree Applications
For easy and quick access to data
In router algorithms
To implement heap data structure
Syntax tree
'''
#lets jump into the code
class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None # till here should be pretty basic

    def traversePreOrder(self):
        print(self.val, end="")
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()


    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val,end="")
        if self.right:
            self.right.traverseInOrder()

    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val,end="")

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()