#You have two arrays of strings, words and parts. Return an array that contains the strings from words, modified so that any occurrences of the substrings from parts are surrounded by square brackets [], following these guidelines:
#If several parts substrings occur in one string in words, choose the longest one. If there is still more than one such part, then choose the one that appears first in the string.
#For words = ["Apple", "Melon", "Orange", "Watermelon"] and parts = ["a", "mel", "lon", "el", "An"], the output should be
#solution(words, parts) = ["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"].
#While "Watermelon" contains three substrings from the parts array, "a", "mel", and "lon", "mel" is the longest substring that appears first in the string.

class Trie(object):
    def __init__(self):
        self.nxt = {}
        self.end = False

    def add(self, word):
        if not word:
            self.end = True
        else:
            self.nxt.setdefault(word[0], Trie()).add(word[1:])
        
    def __repr__(self, level = 0):
        lines = []
        if self.end:
            lines.append("end")
        for k, v in self.nxt.items():
            lines.append("%s -> %s" % (k, repr(v)))
        return "    " * level + "\n".join(lines)

def solution(words, parts):
    trie = Trie()
    for x in parts:
        trie.add(x)
    for i, w in enumerate(words):
        pos = len(w)
        L = -1
        for j in range(len(w)):
            t = trie
            k = j
            while k < len(w) and w[k] in t.nxt:
                t = t.nxt[w[k]]
                k += 1
                if t.end and k - j > L:
                    L = k - j
                    pos = j
        if L > 0:
            words[i] = "%s[%s]%s" % (w[:pos], w[pos:pos+L], w[pos+L:])
    return words



print(solution(["Apple", "Melon", "Orange", "Watermelon"], ["a", "mel", "lon", "el", "An"]))