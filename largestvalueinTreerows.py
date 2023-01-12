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



def largestValuesInTreeRows(t):
    if t == None:
        return []
    queue = [t]
    result = []
    while queue:
        max = -100000
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.value > max:
                max = node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(max)
    return result

t = Tree(1)
t.left = Tree(2)
t.right = Tree(5)
t.left.left = Tree(3)
t.left.right = Tree(4)
t.right.left = Tree(6)
t.right.right = Tree(7)
print(largestValuesInTreeRows(t))
