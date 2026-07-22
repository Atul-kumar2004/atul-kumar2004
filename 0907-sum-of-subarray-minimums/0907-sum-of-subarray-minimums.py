class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            left[i] = count
        stack = []
        for i in range(n - 1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            right[i] = count
            
        # Calculate total sum of contributions
        total_sum = 0
        for i in range(n):
            total_sum = (total_sum + arr[i] * left[i] * right[i]) % MOD
            
        return total_sum