#Given two binary trees t1 and t2, determine whether the second tree is a subtree of the first tree.
#A subtree for vertex v in a binary tree t is a tree consisting of v and all its descendants in t.
#Determine whether or not there is a vertex v (possibly none) in tree t1 such that a subtree for vertex v (possibly empty) in t1 equals t2.
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

def isSubtree(t1, t2):
    #Check if t2 is a subtree of t1
    if t2== None:
        return True
    #Check if t1 is a subtree of t2
    if t1 == None:
        return False
        #Check if t1 and t2 are the same
    if t1.value == t2.value:
        #Check if t1 and t2 are the same
        if isSameTree(t1, t2):
            return True
    #Check if t2 is a subtree of t1.left or t1.right
    return isSubtree(t1.left, t2) or isSubtree(t1.right, t2)
#Check if t1 and t2 are the same
def isSameTree(t1, t2):
    #Check if t1 and t2 are the same
    if t1 == None and t2 == None:
        return True
    #Check if t1 and t2 are the same
    if t1 ==None or t2 == None:
        return False
    #Check if t1 and t2 are the same
    if t1.value != t2.value:
        return False
    
    return isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)

#Test
t1 = Tree(1)
t1.left = Tree(2)
t1.right = Tree(3)
t1.left.left = Tree(4)
t1.left.right = Tree(5)
t1.right.left = Tree(6)
t1.right.right = Tree(7)

t2 = Tree(2)
t2.left = Tree(4)
t2.right = Tree(5)

print (isSubtree(t1, t2))
