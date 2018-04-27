import json

class Trees:
#  def inOrder(self, tree, n, list2) 
#    if n == len(tree)/2 + 1:
#      list2.append(tree[n])
#    if n == len(tree/2) + 2:
#      list2.append(tree[n])  
#     else: 
        
#  def postOrder(self, tree, root, steps):
#    if tree[2 * root + 1] != None:
#      postOrder(tree, 2 * root + 1)
#    if tree[2 * root + 2] != 1
#      postOrder(tree, 2 * root + 2)
#    steps.append({"node" : root})
#    return steps
    
 def traversal(self, tree, order='preOrder'):
    result = {}
    if order == 'preOrder':
      result['result'] = True
      steps = []
      for i in tree:
        steps.append({"node",i})
      result['steps'] = steps
    
 #   if order == 'inOrder'
  #      result['results'] = true
   #     list1 = []
    #    n = len(tree)
      #  list2 = []
     #   list1 = inOrder(tree, n, list2)
       # result['steps'] =  

#    if order == 'postOrder'
 #     result['results'] = True
  #    result['steps'] = postOrder(tree, 0, [])

        
    # check which it is, and do the appropriate traversal
    # this method should return the following dictionary:
    #{
    #  "result": true,
    #  "steps": [
    #    {"node": 0}, // these node numbers are the indices in the input array!
    #    {"node": 1},
    #    {"node": 3}
    #  ]
    #}
    # where each number is the node's index in the input array as you view
    # it in the traversal
    return json.loads(result)