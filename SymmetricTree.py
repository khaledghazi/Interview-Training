#Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
    def __repr__(self, level = 0):
        if self is None:
            return ""
        
        qeue = [self]
        tree_str = ""
        while qeue:
            level_vlaues = []
            childern = []
            for node in qeue:
                level_vlaues.append(str(node.value))
                if node.left:
                    childern.append(node.left)
                if node.right:
                    childern.append(node.right)
            tree_str += "\t".join(level_vlaues) + "\n"
            qeue = childern
        return tree_str


def isTreeSymmetric(t):
    if t == None:
        return True
    else:
        return isMirror(t.left, t.right)

def isMirror(t1, t2):
    if t1 == None and t2 == None:
        return True
    if t1 == None or t2 == None:
        return False
    if t1.value != t2.value:
        return False
    return (t1.value == t2.value) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)


#Test
t = Tree(1)
t.left = Tree(2)
t.right = Tree(2)
t.left.left = Tree(3)
t.left.right = Tree(4)
t.right.left = Tree(4)
t.right.right = Tree(3)

print (isTreeSymmetric(t))
print(t)