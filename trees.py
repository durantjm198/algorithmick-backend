import json
class Trees:

  def traversal(self, tree, order):
    result = {}
    # tree is an array. Look up how trees can be represented as arrays and how
    # you can do a traversal on it!
    # order can be "preOrder", "postOrder", or "inOrder"
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