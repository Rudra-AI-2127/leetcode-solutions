
class Solution(object):
    def numberOfSpecialChars(self, word):
        lower = set()
        upper = set()

        for ch in word:
            if ch.islower():
                lower.add(ch)
            else:
                upper.add(ch.lower())

        return len(lower & upper)
