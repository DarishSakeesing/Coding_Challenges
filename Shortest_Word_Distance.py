# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

def shortestDistance(words, word1, word2) -> int:
    pointer1 = -1
    pointer2 = -1
    distance = float('inf')

    for i in range(len(words)):
        if words[i] == word1 or words[i] == word2:
            if words[i] == word1:
                pointer1 = i
            else:
                pointer2 = i
            
            if pointer1 != -1 and pointer2 != -1:
                new_distance = abs(pointer2 - pointer1)
                if new_distance < distance:
                    distance = new_distance

    return distance


a = ['a', 'b', 'c', 'd', 'b']

result = shortestDistance(a, 'd', 'b')
print(result)
   
