class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n2 = len(text2)
        count = 0
        last = -1
        for i in range(0,n2):
            if text2[i] in text1:
                t1ind = text1.index(text2[i])
                if t1ind >= last:
                    count += 1
                    last = t1ind
            

        return count


text1 = "oxcpqrsvwf"
text2 = "shmtulqrypy"
solution = Solution()
print(solution.longestCommonSubsequence(text1, text2)) 