#Traverse a binary Tree and check if there is a path from root to leaf with given sum
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
    def __repr__(self, level = 0):
        if self is None:
            return ""

        tree_str = ""
        tree_str += " " * level + str(self.value) + "\n"
        if self.left:
            tree_str += self.left.__repr__(level + 1)
        if self.right:
            tree_str += self.right.__repr__(level + 1)
        return tree_str

def hasPathWithGivenSum(t, s):
    if t == None:
        return s == 0
    else:
        ans = 0
        subSum = s - t.value
        if subSum == 0 and t.left == None and t.right == None:
            return True
        if t.left != None:
            ans = ans or hasPathWithGivenSum(t.left, subSum)
        if t.right != None:
            ans = ans or hasPathWithGivenSum(t.right, subSum)
        return ans

#Test
t = Tree(4)
t.left = Tree(1)
t.right = Tree(3)
t.left.left = Tree(1)
t.left.right = Tree(2)
t.right.right = Tree(1)
t.right.left = Tree(0)

print (hasPathWithGivenSum(t, 7))