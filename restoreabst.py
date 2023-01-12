#Given the inorder and preorder traversals of a binary tree t, but not t itself, restore t and return it.
#Example
#For inorder = [4, 2, 1, 5, 3, 6] and preorder = [1, 2, 4, 3, 5, 6], the output should be
#restoreBinaryTree(inorder, preorder) = {
#    "value": 1,
#    "left": {
#        "value": 2,
#        "left": {
#            "value": 4,
#            "left": null,
#            "right": null
#        },
#        "right": null
#    },
#    "right": {
#        "value": 3,
#        "left": {
#            "value": 5,
#            "left": null,
#            "right": null
#        },
#        "right": {
#            "value": 6,
#            "left": null,
#            "right": null
#        }
#    }
#}
#Input/Output
#[time limit] 4000ms (py)
#[input] array.integer inorder
#An inorder traversal of the tree. It is guaranteed that all numbers in the tree are pairwise distinct.
#Constraints:
#1 ≤ inorder.length ≤ 2 · 104,
#-105 ≤ inorder[i] ≤ 105.
#[input] array.integer preorder
#A preorder traversal of the tree.


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


def restoreBinaryTree(inorder, preorder):
    if not inorder or not preorder:
        return None
    
    #create a new Tree node with the value of the first elment in the preorder list
    root = Tree(preorder[0])
    #find the index of the root in the inorder list
    root_idx = inorder.index(root.value)
    
    #recursivly build the left and right subress using inorder and preorder list
    root.left = restoreBinaryTree(inorder[:root_idx], preorder[1: root_idx +1])
    root.right = restoreBinaryTree(inorder[root_idx + 1:], preorder[root_idx +1:])
    return root

#Test
inorder = [4, 2, 1, 5, 3, 6]
preorder = [1, 2, 4, 3, 5, 6]
print (restoreBinaryTree(inorder, preorder))
