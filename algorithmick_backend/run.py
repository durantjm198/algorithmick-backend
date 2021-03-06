from flask import Flask, request, jsonify, render_template
import json
from .binary_trees import binary_tree_traversal
from .binary_trees import is_binary_search_tree

application = Flask(__name__)

# Helper function -- attempts to turn a string into an int, and fails silently
# if input is invalid.
def string_to_int(s):
  try:
    return int(s)
  except ValueError:
    return None

@application.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@application.route('/')
def docs_home():
  return render_template('docs_home.html')

@application.route("/binary_trees/traversal", methods=['POST'])
def traversal_endpt():
  data = request.get_json()
  order = data['traversal']
  tree = list(map(string_to_int, data['tree']))
  return json.dumps(binary_tree_traversal(tree, order))

@application.route("/binary_trees/is_binary_search_tree", methods=['POST'])
def is_bst_endpt():
  data = request.get_json()
  tree = list(map(string_to_int, data['tree']))
  return json.dumps(is_binary_search_tree(tree))

"""@application.route('/binary_trees/binary_search', methods=['POST'])
def binary_search_endpt():
  data = request.get_json()
  tree = list(map(string_to_int, data['tree']))
  target = string_to_int(data['target'])
  return json.dumps(is_binary_search_tree(tree))"""