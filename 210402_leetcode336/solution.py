from collections import defaultdict


class Trie:
    def __init__(self):
        self.links = defaultdict(self.__class__)
        self.index = None
        self.pali_indices = set()

    def insert(self, word, i):
        trie = self
        for j, ch in enumerate(word):
            trie = trie.links[ch]
            if word[j+1:] and is_palindrome(word[j+1:]):
                trie.pali_indices.add(i)
        trie.index = i


def is_palindrome(word):
    i, j = 0, len(word) - 1
    while i <= j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True


class Solution:
    def palindromePairs(self, words):
        root = Trie()
        res = []
        for i, word in enumerate(words):
            if not word:
                continue
            root.insert(word[::-1], i)
        for i, word in enumerate(words):
            if not word:
                continue
            trie = root
            for j, ch in enumerate(word):
                if ch not in trie.links:
                    break
                trie = trie.links[ch]
                if is_palindrome(word[j+1:]) and trie.index is not None and trie.index != i:
                    res.append([i, trie.index])
            else:
                for pali_index in trie.pali_indices:
                    if i != pali_index:
                        res.append([i, pali_index])
        if '' in words:
            j = words.index('')
            for i, word in enumerate(words):
                if i != j and is_palindrome(word):
                    res.append([i, j])
                    res.append([j, i])
        return res