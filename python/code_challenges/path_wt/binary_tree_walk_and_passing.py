# walk and in three orders: pre, in, post
# pass lower nodes information?
# how pass higher nodes information?

# walk and print in preorder; no info passing
def print_tree(bin_tree):

  current = bin_tree.root

  def walk_and_print(node):

      print(node.value)

      if node.left_node:
          walk_and_print(node.left_node)

      if node.right_node:
          walk_and_print(node.right_node)

  walk_and_print(current)



# pass lower nodes information?
def print_tree_pass_lower(bin_tree):

  current = bin_tree.root

  def walk_and_print(node, pass_down_info):

      print(node.value)
      pass_down_info = 2 + node.value

      if node.left_node:
          walk_and_print(node.left_node, pass_down_info)

      if node.right_node:
          walk_and_print(node.right_node, pass_down_info)

  walk_and_print(current, pass_down_info_start)



# how pass higher nodes information?
def print_tree_pass_higher(bin_tree):

  current = bin_tree.root

  def walk_and_print(node):
    returned_info_left, returned_info_right = 0

    this_node_info = print(node.value)

    if node.left_node:
      returned_info_left = walk_and_print(node.left_node)

    if node.right_node:
      returned_info_right = walk_and_print(node.right_node)

    combined_info = this_node_info + returned_info_left + returned_info_right
    return combined_info

  walk_and_print(current)
