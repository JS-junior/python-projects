from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route("/")
def index():
  return "Hello world"
  
@app.route("/signup", methods=["GET", "POST"])
def signup():
  pass
  
@app.route("/login")
def login():
  pass
  
@app.route("/logout")
  
if __name__ == "__main__":
  app.run(debug=True)