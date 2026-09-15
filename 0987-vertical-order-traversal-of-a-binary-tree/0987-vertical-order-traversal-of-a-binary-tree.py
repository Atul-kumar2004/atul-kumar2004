# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes = []
        queue = deque([(root, 0, 0)])

        while queue:
            node, row, col = queue.popleft()
            nodes.append((col, row, node.val))
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        nodes.sort()
        column_map = defaultdict(list)
        for col, row, val in nodes:
            column_map[col].append(val)

        return [column_map[c] for c in sorted(column_map)]
        