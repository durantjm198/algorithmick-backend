from flask import Flask, request, jsonify
import json
from .trees import binary_tree_traversal

application = Flask(__name__)

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
def hello():
  return "<h1>KENDRICK DESERVED THE GRAMMY</hi>"

@application.route("/trees/traversal", methods=['POST'])
def traversal():
  data = request.form
  order = data.get('traversal')
  tree = list(map(string_to_int, data.get('tree').split(',')))
  return json.dumps(binary_tree_traversal(tree, order))
