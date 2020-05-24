import flask
from flask import jsonify
import random
from generate_blocks import generate_blocks

app = flask.Flask(__name__)

@app.route('/api/block_models/', methods=['GET'])
def block_models():
  block_models = [
    {
      "name": "marvin"
    },
    {
      "name": "mclaughlin"
    },
    {
      "name": "sm3"
    }
  ]
  return jsonify(block_models)

@app.route('/api/block_models/<name>/blocks/', methods=['GET'])
def blocks(name):
  return jsonify(generate_blocks(20,20,10))

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
  app.run()