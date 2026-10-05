class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Lengths must match
        if len(s) != len(goal):
            return False
        # Check if goal is in s+s
        return goal in (s + s)
sol = Solution()
print(sol.rotateString("abcde", "cdeab"))  # True
print(sol.rotateString("abcde", "abced"))  # False
