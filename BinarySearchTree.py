class Node(object):
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution(object):
  def _isValidBSTHElper(self, n, low, high):
    if not n:
      return True

    val = n.val

    if ((
      val > low and 
      val < high and 
      self._isValidBSTHElper(n.left, low, n.val) and 
      self._isValidBSTHElper(n.right, n.val, high))):
      return True
    return False

  def isValidBST(self, n):
    return self._isValidBSTHElper(n, float('-inf'), float('inf'))

# True BST
#     5
#    / \
#   4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution().isValidBST(node))

# False BST
#     5
#    / \
#   4   7
#      /
#     2
node.right.left = Node(2)
print(Solution().isValidBST(node))