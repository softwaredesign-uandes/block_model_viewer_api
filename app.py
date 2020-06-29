import flask
from flask import jsonify
import random
from generate_blocks import generate_blocks
from load_block_model_from_file import load_block_model_from_file
import requests

app = flask.Flask(__name__)

FEATURE_FLAG_API_URL = 'https://dry-brushlands-69779.herokuapp.com/api/feature_flags/'

BLOCK_MODELS = {
  'kd': load_block_model_from_file('kd', ['index', 'x', 'y', 'z', 'tonn', 'blockvalue', 'destination', 'CU %', 'process_profit']),
  'marvin': load_block_model_from_file('marvin', ['index', 'x', 'y', 'z', 'tonn', 'au [ppm]', 'cu %', 'proc_profit']),
  'zuck_small': load_block_model_from_file('zuck_small', ['index', 'x', 'y', 'z', 'cost', 'value', 'rock_tonnes', 'ore_tonnes']),
  'zuck_medium': load_block_model_from_file('zuck_medium', ['index', 'x', 'y', 'z', 'cost', 'value', 'rock_tonnes', 'ore_tonnes']),
  'newman1': load_block_model_from_file('newman1', ['index', 'x', 'y', 'z', 'type', 'grade', 'tonns', 'min_caf', 'value_extracc', 'value_proc', 'apriori_process'])
}

BLOCK_MODEL_NAMES = [
  {
    "name": "kd"
  },
  {
    "name": "marvin"
  },
  {
    "name": "zuck_small"
  },
  {
    "name": "zuck_medium"
  },
  {
    "name": "newman1"
  }
]

@app.route('/api/block_models/', methods=['GET'])
def block_models():
  block_models = BLOCK_MODEL_NAMES
  if requests.get(FEATURE_FLAG_API_URL).json()['restful_response']:
    block_models = { "block_models": block_models }
  return jsonify(block_models)

@app.route('/api/block_models/<name>/blocks/', methods=['GET'])
def blocks(name):
  return jsonify(BLOCK_MODELS[name])

@app.route('/api/block_models/<name>/blocks/<index>', methods=['GET'])
def block(name, index):
  block = next(filter(lambda b: b["index"] == int(index), BLOCK_MODELS[name]["block_model"]["blocks"]), None)
  return jsonify({ "block": block } )

@app.route('/api/block_models/<name>/blocks/<index>/extract/', methods=['POST'])
def extract(name, index):
  block = next(filter(lambda b: b["index"] == int(index), BLOCK_MODELS[name]["block_model"]["blocks"]), None)
  return jsonify({ "blocks": [block] } )

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
  app.run(port= 8000)