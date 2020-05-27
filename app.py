import flask
from flask import jsonify
import random
from generate_blocks import generate_blocks
import requests

app = flask.Flask(__name__)

FEATURE_FLAG_API_URL = 'https://dry-brushlands-69779.herokuapp.com/api/feature_flags/'

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
  if requests.get(FEATURE_FLAG_API_URL).json()['restful_response']:
    block_models = { "block_models": block_models }
  return jsonify(block_models)

@app.route('/api/block_models/<name>/blocks/', methods=['GET'])
def blocks(name):
  blocks = generate_blocks(20,20,10)
  if requests.get(FEATURE_FLAG_API_URL).json()['restful_response']:
    blocks = { "block_model": { "blocks": blocks } }
  return jsonify(blocks)

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
  app.run(port= 8000)