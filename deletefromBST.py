#write a method to delete a node or more from a BST
#Removing a value x from a BST t is done in the following way: If there is no x in t, nothing happens; Otherwise, let t' be a subtree of t such that t'.value = x.
#If t' has a left subtree, remove the rightmost node from it and put it at the root of t';
#Otherwise, remove the root of t' and its right subtree becomes the new t's root.
#Given a binary search tree t and an array of numbers queries, remove the items from queries from t, if present, and return the resulting BST.
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

# given a BST and an array of numbers, remove the items from the array from the BST
def deleteFromBST(t, queries):

        def remove (n , k ) : 
            if n : 
                if   n.value > k : n.left  = remove(n.left ,k)
                elif n.value < k : n.right = remove(n.right,k)
                else : ## == 
                    if   not n.left  : return n.right
                    # elif not n.right : return n.left 

                    ### not a recursive remove to avoid straightening
                    ##  which elif would have avoided...
                    if n.left.right is None : 
                        n.value = n.left.value
                        n.left  = n.left.left
                    else : 
                        tmp = n.left
                        while tmp.right.right : 
                            tmp = tmp.right
                        n.value = tmp.right.value
                        tmp.right = tmp.right.left
                return n

        for q in queries : 
            t = remove(t,q) 
        return t
t = Tree(5)
t.left = Tree(3)
t.right = Tree(6)
t.left.left = Tree(2)
t.left.right = Tree(4)
t.left.left.left = Tree(1)
queries = [3, 5]
print(t)
print (deleteFromBST(t, queries))

