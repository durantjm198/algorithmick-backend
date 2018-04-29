import json


def preOrderHelper(tree, root, steps):
  if tree[root] != None:
    steps.append({'node': root})
  if len(tree) > root * 2 + 1:
    preOrderHelper(tree, root * 2 + 1, steps)
  if len(tree) > root * 2 + 2:
    preOrderHelper(tree, 2 * root + 2, steps)

def inOrderHelper(tree, root, steps):
  if len(tree) > root * 2 + 1:
    inOrderHelper(tree, root * 2 + 1, steps)
  if tree[root] != None:
    steps.append({'node': root})
  if len(tree) > root * 2 + 2:
    inOrderHelper(tree, 2 * root + 2, steps)

def postOrderHelper(tree, root, steps):
  if len(tree) > root * 2 + 1:
    postOrderHelper(tree, root * 2 + 1, steps)
  if len(tree) > root * 2 + 2:
    postOrderHelper(tree, 2 * root + 2, steps)
  if tree[root] != None:
    steps.append({'node': root})
  
def binary_tree_traversal(tree, order='preOrder'):
  result = {}
  result['steps'] = []

  if order == 'preOrder':
    preOrderHelper(tree, 0, result['steps'])
  elif order == 'inOrder':
    inOrderHelper(tree, 0, result['steps'])
  elif order == 'postOrder':
    postOrderHelper(tree, 0, result['steps'])

  result["array"] = tree  
  result["result"] = True
  return result