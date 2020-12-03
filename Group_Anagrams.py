# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.

def group_anagrams(strs):
    listOfWords = []
    listOfAnagrams = []
    for i in range(len(strs)):
        word = sorted(strs[i])
        word = ''.join(word)

        if word in listOfWords:
            indexOfWords = listOfWords.index(word)
            listOfAnagrams[indexOfWords].append(strs[i])
        else:
            listOfWords.append(word)
            listOfAnagrams.append([strs[i]])

    return listOfAnagrams

print(group_anagrams(strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))
