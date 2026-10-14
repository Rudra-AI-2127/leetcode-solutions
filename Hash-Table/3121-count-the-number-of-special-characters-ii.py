class Solution(object):
    def numberOfSpecialChars(self, word):
        ans = 0
        for c in set(word.lower()):
            if c in word and c.upper() in word:
                if word.rfind(c) < word.find(c.upper()):
                    ans += 1
        return ans