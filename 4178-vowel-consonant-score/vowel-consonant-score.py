class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = set('aeiou')
        v = 0
        c = 0

        for ch in s:
            if ch.isalpha():          # consider only letters
                if ch in vowels:
                    v += 1
                else:
                    c += 1

        return v // c if c > 0 else 0
