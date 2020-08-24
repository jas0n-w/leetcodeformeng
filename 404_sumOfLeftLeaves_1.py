# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        def dfs(node, is_left):
            if not node: return 0
            if not node.left and not node.left and is_left:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)
    
        return dfs(root, False)


if __name__ == "__main__":
    pass
    # assert Solution().sumOfLeftLeaves([1,2,3,4,5]) == 4