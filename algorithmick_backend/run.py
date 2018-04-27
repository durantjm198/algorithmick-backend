from flask import Flask, request, jsonify
import json
from .trees import Trees

application = Flask(__name__)

@application.route('/')
def hello():
  return "<h1>KENDRICK DESERVED THE GRAMMY</hi>"

@application.route("/trees/traversal", methods=['POST'])
def traversal():
  data = request.form
  print(request.form)
  order = data.get('traversal')
  tree = data.get('tree')
  return json.loads(Trees.traversal(tree, order))