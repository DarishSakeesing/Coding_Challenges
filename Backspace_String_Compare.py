#Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#Example 1:
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".


def backspaceCompare(S: str, T: str) -> bool:
    newS = ''
    newT = ''
    for x in S:
        if x != '#':
            newS += x
        else:
            newS = newS[:-1]

    for y in T:
        if y != '#':
            newT += y
        else:
            newT = newT[:-1]

    if newS == newT:
        return True
    else:
        return False

# Should print False because "ab#c", "ab#b" are not equal
print(backspaceCompare("ab#c", "ab#b"))

#Should print True because "zx#y", "zc#y" are equal
print(backspaceCompare("zx#y", "zc#y"))