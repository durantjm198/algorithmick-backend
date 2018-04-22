import json
class Trees:
  
  def inOrder(self, tree, n, list2) 
     if n == len(tree)/2 + 1:
         list2.add(tree[n])
     if n == len(tree/2) + 2:
         list2.add(tree[n])  
     else: 
        
         

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
        list1 = []
        n = len(tree)
        list2 = []
        list1 = inOrder(tree, n, list2)
        result['steps'] =  

        
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