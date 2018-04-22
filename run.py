from flask import Flask, request, jsonify
import json
from trees import Trees
from .app import application

@application.route("/")
def hello():
  return "<h1>KENDRICK DESERVED THE GRAMMY</hi>"

@application.route("/trees/traversal", methods=['POST'])
def traversal():
  data = request.get_json()
  order = data.get('traversal')
  tree = data.get('tree')
  return json.loads(Trees.traversal(tree, order))