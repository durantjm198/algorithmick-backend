from flask import Flask, request, jsonify
import json
from trees import Trees
app = Flask(__name__)

@app.route("/trees/traversal", methods=['POST'])
def traversal():
  data = request.get_json()
  order = data.get('traversal')
  tree = data.get('tree')
  return json.loads(Trees.traversal(tree, order))