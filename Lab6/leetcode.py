class Solution:
    base = 47
    md = 1000000007

    @staticmethod
    def create_hashes(text):
        n = len(text)
        base = Solution.base
        md = Solution.md
        hashes = [0] * (n + 1)
        pows = [0] * (n + 1)
        pows[0] = 1
        for i in range(1, n + 1):
            hashes[i] = (hashes[i - 1] * base + ord(text[i - 1])) % md
            pows[i] = (pows[i - 1] * base) % md
        return hashes, pows
    

    @staticmethod
    def get_hash(lb, rb, hashes, pows):
        md = Solution.md
        return (hashes[rb] + md - hashes[lb] * pows[rb - lb] % md) % md

    def distinctEchoSubstrings(self, text: str) -> int:
        subs = set()
        hashes, pows = self.create_hashes(text)

        for wlen in range(1, len(text) // 2 + 1):
            count = 0
            for lb in range(len(text) - wlen):
                rb = lb + wlen
                if text[lb] == text[rb]:
                    count += 1
                else:
                    count = 0
                
                if count == wlen:
                    subs.add(self.get_hash(lb - wlen + 1, lb + 1, hashes, pows))
                    count -= 1
        return len(subs)
        