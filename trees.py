import json
class Trees:
  #left kid = 2i + 1
  #right kide = 2i + 2
  def inOrder(self, tree, s, finish) 
     steps = []
     if start > end:
        return

     inOrder(tree, s*2 + 1, finish);
 
     
    steps.apend({"node", tree[s]})
 
     
     inOrder(arr, s*2 + 2, finish);
     
     return steps      

 def traversal(self, tree, order):
    result = {}
    # tree is an array. Look up how trees can be represented as arrays and how
    # you can do a traversal on it!
    # order can be "preOrder", "postOrder", or "inOrder"
    #binary tree- is it a binary search tree
    if order == 'preOrder'
        result['result'] = true 
        steps = []
        for i in tree
            steps.append({"node",i})
        result['steps'] = steps
    
    if order == 'inOrder'
        result['results'] = true
        result['steps'] =  inOrder(trees,0, len(tree) - 1)

        
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

print(Trees.traversal([1, 2, 3, 4, 5], 'preOrder'))