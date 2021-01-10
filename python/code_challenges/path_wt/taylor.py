

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def check_weight(root, n):
  target = n
  total_so_far = 0
  def traverse(root, total_so_far):

    if root:
      total_so_far += root.val
      # print(total_so_far)
      if not root.left and not root.right:
        # print(total_so_far)
        if target == total_so_far:
          print("right after if statement and before return",total_so_far)
          return total_so_far

        # First recur on left child
      traverse(root.left, total_so_far)
        # now recur on right child
      traverse(root.right, total_so_far)
      return False
  print(traverse(root, total_so_far))
  if target == traverse(root, total_so_far):
    return True
  return False



# Driver code
root = Node(10)
root.left = Node(0)
root.right = Node(5)
root.right.left = Node(0)
root.right.right = Node(5)

print(check_weight(root,20))
