import sys

print("i'm in the file", file=sys.stderr)
from flask import Flask, request, jsonify
import json
print("imported some shit", file=sys.stderr)
from trees import Trees
app = Flask(__name__)

app.run(debug=True)