from flask import Flask, request, jsonify
import json
from .trees import binary_tree_traversal

application = Flask(__name__)

@application.route('/')
def hello():
  return "<h1>KENDRICK DESERVED THE GRAMMY</hi>"

@application.route("/trees/traversal", methods=['POST'])
def traversal():
  data = request.form
  order = data.get('traversal')
  tree = data.get('tree')
  print('tree: ' + tree)
  print('order: ' + order)
  return json.dumps(binary_tree_traversal(tree, order))