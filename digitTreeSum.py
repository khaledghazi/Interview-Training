class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
    def __repr__(self, level = 0):
        lines = []
        if self.right:
            found = False
            for line in repr(self.right).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(str(self.value))
        if self.left:
            found = False
            for line in repr(self.left).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)


#We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.
#Given a binary tree t, find the sum of all the numbers encoded in it.
#Example
#For
#t = {
#    "value": 1,
#    "left": {
#        "value": 0,
#        "left": {
#            "value": 3,
#            "left": null,
#            "right": null
#        },
#        "right": {
#            "value": 1,
#            "left": null,
#            "right": null
#        }
#    },
#    "right": {
#        "value": 4,
#        "left": null,
#        "right": null
#    }
#}
#the output should be
#digitTreeSum(t) = 218.
def digitTreeSum(t):
    if t == None:
        return 0
    queue = [t]
    result = []
    while queue:
        node = queue.pop(0)
        if node.left:
            node.left.value = node.value * 10 + node.left.value
            queue.append(node.left)
        if node.right:
            node.right.value = node.value * 10 + node.right.value
            queue.append(node.right)
        if node.left == None and node.right == None:
            result.append(node.value)
    return sum(result)

t = Tree(1)
t.left = Tree(0)
t.right = Tree(4)
t.left.left = Tree(3)
t.left.right = Tree(1)
print(digitTreeSum(t))
