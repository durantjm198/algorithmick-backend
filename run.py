print("made thee app", file=sys.stderr)

@app.route("/")
def hello():
  return "<h1>KENDRICK DESERVED THE GRAMMY</hi>"

@app.route("/trees/traversal", methods=['POST'])
def traversal():
  data = request.get_json()
  order = data.get('traversal')
  tree = data.get('tree')
  return json.loads(Trees.traversal(tree, order))
print("functions weren't sus", file=sys.stderr)