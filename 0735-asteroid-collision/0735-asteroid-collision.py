class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # Process collisions
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:   # top asteroid smaller, destroyed
                    stack.pop()
                    continue
                elif stack[-1] == -a:  # both destroyed
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack