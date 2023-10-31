class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))

        return res

n = 0b00000010100101000001111010011100
solution = Solution()
print(solution.reverseBits(n))