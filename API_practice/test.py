from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
app.secret_key = "PRACTICE FOR API"

@app.route('/', methods = ['GET'])
def home() :
    return """ <h1> Practice for API...! </h1> """

if __name__ == "__main__" :
    app.run(debug = True)