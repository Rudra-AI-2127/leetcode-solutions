class Solution(object):
    def numberOfSpecialChars(self, word):
        return sum(c in word and c.upper() in word for c in set(word) if c.islower())