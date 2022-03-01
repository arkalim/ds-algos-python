class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

# pre order traversal (DFS)
def traversePreOrder(node):
    if node is None:
        return
    print(node.value, end=' ')
    traversePreOrder(node.left)
    traversePreOrder(node.right)

# in order traversal (DFS)
def traverseInOrder(node):
    if node is None:
        return
    traverseInOrder(node.left)
    print(node.value, end=' ')
    traverseInOrder(node.right)

# post order traversal (DFS)
def traversePostOrder(node):
    if node is None:
        return
    traversePostOrder(node.left)
    traversePostOrder(node.right)
    print(node.value, end=' ')

# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return
    # if we reach the level, print the value
    if level == 1:
        print(root.value, end=" ")
    # until we reach the level, keep digging
    else:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)

# Height of the tree
def height(node):
    # base case
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        leftHeight = height(node.left)
        rightHeight = height(node.right)

        # Use the larger one (+1 for root node)
        return max(leftHeight, rightHeight) + 1

# level order traversal
def traverseLevelOrder(node):
    # find the number of levels in the tree
    # and print the values at each level
    for level in range(1, height(node)+1):
        printCurrentLevel(node, level)


# construct a tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('\nHeight of the tree: ', height(root))

print('\nPre-order traversal')
traversePreOrder(root)

print('\nIn-order traversal')
traverseInOrder(root)

print('\nPost-order traversal')
traversePostOrder(root)

print('\nLevel-order traversal')
traverseLevelOrder(root)