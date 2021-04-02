class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_pallindrome(word):
            return word == word[::-1]
        
        output = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                    
                if is_pallindrome(word1 + word2):
                    output.append([i, j])
        return output

# Time Limit Exceeded