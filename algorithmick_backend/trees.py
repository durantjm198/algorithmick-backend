import json

def inOrderHelper(tree, root, steps):
  if tree[root * 2 + 1] != None:
    inOrderHelper(tree, root * 2 + 1, steps)
  steps.append({'node': root})
  if tree[root * 2 + 2] != None:
    inOrderHelper(tree, 2 * root + 2, steps)

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