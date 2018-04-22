from flask import Flask, request, jsonify
import json
from trees import Trees
app = Flask(__name__)

app.run(debug=True)