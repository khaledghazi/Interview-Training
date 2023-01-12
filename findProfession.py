#Consider a special family of Engineers and Doctors. This family has the following rules:
#1. Everybody has two children.
#2. The first child of an Engineer is an Engineer and the second child is a Doctor.
#3. The first child of a Doctor is a Doctor and the second child is an Engineer.
#4. All generations of Doctors and Engineers start with an Engineer.
#Given the level and position of a person in the ancestor tree above, find the profession of the person.
#Note: in this tree first child is considered as left child, second - as right.

def findProfession(level, pos):
    if level == 1:
        return "Engineer"
    if findProfession(level - 1, (pos + 1) // 2) == "Engineer":
        if pos % 2 == 1:
            return "Engineer"
        else:
            return "Doctor"
    else:
        if pos % 2 == 1:
            return "Doctor"
        else:
            return "Engineer"

#Test
print (findProfession(1, 1))
print (findProfession(2, 1))
print (findProfession(2, 2))
print (findProfession(3, 3)) 
print (findProfession(10, 470))
