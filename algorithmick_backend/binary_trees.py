import json

def left(n):
  return 2 * n + 1

def right(n): 
  return 2 * n + 2

def is_binary_search_tree(tree):
  response = {"steps": []}
  def is_bst_util(rt, mini, maxi):
    step = {'node' : rt}
    
    if len(tree) < rt or tree[rt] == None:
      step['result'] = "true"
      response["steps"].append(step)
      return True

    if tree[left(rt)] > tree[rt] or tree[right(rt)] < tree[rt]:
      step["result"] = 'false'
      response["steps"].append(step)
      return False
    
    response["steps"].append(step)
    return is_bst_util(left(rt), mini, tree[rt]) and \
      is_bst_util(right(rt), tree[rt], maxi)

  response["array"] = tree
  response["result"] = is_bst_util(0, float('-inf'), float('inf'))
  return response

def binary_tree_traversal(tree, order='preOrder'):
  def preOrderHelper(tree, rt, steps):
    if tree[rt] != None:
      steps.append({'node': rt})
    if len(tree) > left(rt):
      preOrderHelper(tree, left(rt), steps)
    if len(tree) > right(rt):
      preOrderHelper(tree, right(rt), steps)

  def inOrderHelper(tree, rt, steps):
    if len(tree) > left(rt):
      inOrderHelper(tree, left(rt), steps)
    if tree[rt] != None:
      steps.append({'node': rt})
    if len(tree) > right(rt):
      inOrderHelper(tree, right(rt), steps)

  def postOrderHelper(tree, rt, steps):
    if len(tree) > left(rt):
      postOrderHelper(tree, left(rt), steps)
    if len(tree) > right(rt):
      postOrderHelper(tree, right(rt), steps)
    if tree[rt] != None:
      steps.append({'node': rt})
  
  response = {}
  response['steps'] = []

  if order == 'preOrder':
    preOrderHelper(tree, 0, response['steps'])
  elif order == 'inOrder':
    inOrderHelper(tree, 0, response['steps'])
  elif order == 'postOrder':
    postOrderHelper(tree, 0, response['steps'])

  response["array"] = tree  
  response["result"] = True
  return response