#given a binary search tree t, find the kth smallest element in it with O(1) space complexity
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def kthSmallestInBST(t, k):
     # Define a generator function that performs a DFS traversal of the tree
    def dfs(node):
        # If the node exists, yield the values from the left subtree, the node's value, and the values from the right subtree
        if node:
            # The yield keyword is used to define a generator function
            yield from dfs(node.left)
            yield node.value
            yield from dfs(node.right)
    
    # Call the generator function and store the result in a variable
    f = dfs(t)
    # Iterate through the generator function k times
    for _ in range(k):
        # Store the next value in the generator function in a variable
        ans = next(f)
    # Return the kth smallest value
    return ans
#Test
t = Tree(3)
t.left = Tree(1)
t.right = Tree(5)
t.right.left = Tree(4)
t.right.right = Tree(6)

print (kthSmallestInBST(t, 4))
