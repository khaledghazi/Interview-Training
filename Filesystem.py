#Suppose we represent our file system as a string. For example, the string "user\n\tpictures\n\tdocuments\n\t\tnotes.txt" represents:
#user
#   pictures
#   documents
#       notes.txt  
#The directory user contains an empty sub-directory pictures and a sub-directory documents containing a file notes.txt.
#The string "user\n\tpictures\n\t\tphoto.png\n\t\tcamera\n\tdocuments\n\t\tlectures\n\t\t\tnotes.txt" represents:
#user
#   pictures
#       photo.png
#       camera
#   documents
#       lectures
#           notes.txt

# The directory user contains two sub-directories pictures and documents. pictures contains a file photo.png and an empty second-level sub-directory camera. documents contains a second-level sub-directory lectures containing a file notes.txt.
# We want to find the longest (as determined by the number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "user/documents/lectures/notes.txt", and its length is 33 (not including the double quotes).
# Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
# Note: Due to system limitations, test cases use form feeds ('\f', ASCII code 12) instead of newline characters.
# Example
# For fileSystem = "user\f\tpictures\f\tdocuments\f\t\tnotes.txt", the output should be
# longestPath(fileSystem) = 24.
# There are no other files in the file system, so "user/documents/notes.txt" is the longest path.
# For fileSystem = "user\f\tpictures\f\t\tphoto.png\f\t\tcamera\f\tdocuments\f\t\tlectures\f\t\t\tnotes.txt", the output should be
# longestPath(fileSystem) = 33.
# "user/documents/lectures/notes.txt" is the longest path.
# Input/Output
# [execution time limit] 4 seconds (py3)
# [input] string fileSystem
# A representation of the file system, where the names of files and directories consist of English letters, digits and spaces. It is guaranteed that:
# the name of a file contains at least a period and an extension;
# the name of a directory or a file doesn't contain multiple consecutive spaces (however, it may contain leading or trailing spaces);
# each directory name ends with a '/'.
# It is also guaranteed that the total number of directories in the first part of fileSystem doesn't exceed 10.
# [output] integer
# The length of the longest absolute path to a file in the abstracted file system described by fileSystem. If there is no file in the system, return 0.

def longestPath(filesystem):
    lines = filesystem.split("\f")
    stack = []
    max_len = 0
    for line in lines:
        level = line.count("\t")
        while len(stack) > level:
            stack.pop()
        stack.append(line.strip())
        if "." in line:
            max_len = max(max_len, len("/".join(stack)))
    return max_len
    

print(longestPath("user\f\tpictures\f\tdocuments\f\t\tnotes.txt"))
