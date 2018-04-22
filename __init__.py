from flask import Flask, request, jsonify
import json
from trees import Trees
application = Flask(__name__)