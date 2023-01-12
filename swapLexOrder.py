import collections
#Given a string str and array of pairs that indicates which indices in the string can be swapped, return the lexicographically largest string that results from doing the allowed swaps. You can swap indices any number of times.
#Example
#For str = "abdc" and pairs = [[1, 4], [3, 4]], the output should be swapLexOrder(str, pairs) = "dbca".
#By swapping the given indices, you get the strings: "cbda", "cbad", "dbac", "dbca". The lexicographically largest string in this list is "dbca".
#For str = "acxrabdz" and pairs = [[1, 3], [6, 8], [3, 8], [2, 7]], the output should be swapLexOrder(str, pairs) = "zdxrabca".
#By swapping the given indices, you get the strings: "zcxrabda", "zdxrabca", "acxrabdz". The lexicographically largest string in this list is "zdxrabca".
def swaplexorder(strn, pairs):
       # if not strn or not pairs : return strn
    # check for connected node groupings which can be sorted individually
    grp = {} # set of all possible locations an index could end up
    for a,b in pairs : 
        g = grp.get(a,{a}) | grp.get(b,{b}) 
        for n in g : # reset all nodes in group
            grp[n] = g
    for n in grp : 
        grp[n] = tuple(sorted(grp[n]))
    reord = {}
    for c in set(grp.values())  : 
        word = sorted((strn[i-1] for i in c), reverse = True)
        for i,l in zip(c,word) : 
            reord[i-1] = l # string is 0 indexed
    return ''.join(reord.get(i,x) for i,x in enumerate(strn))

print(swaplexorder("acxrabdz", [[1, 3], [6, 8], [3, 8], [2, 7]]))
