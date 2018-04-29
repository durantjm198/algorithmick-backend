import json

def inOrderHelper(tree, root, steps):
  if len(tree) >= 2 * root + 1:
    if tree[2 * root + 1] != None:
      inOrderHelper(tree, root * 2, steps)
  steps.append({'node': root})
  if len(tree) >= 2 * root + 2:
    if tree[2 * root + 2] != None:
      inOrderHelper(tree, 2 * root + 1, steps)

def binary_tree_traversal(tree, order='preOrder'):
  result = {}
  result['steps'] = []

  if order == 'preOrder':
    for i in tree:
      result["steps"].append({"node": i})
  elif order == 'inOrder':
    inOrderHelper(tree, 0, result['steps'])
  #  elif order == 'postOrder':

  result["array"] = tree  
  result["result"] = True
  return result