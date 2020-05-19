import flask
from flask import jsonify
import random

app = flask.Flask(__name__)

def generateBlocks():
  def isBlockInCore(i, j, k, xSize, ySize, zSize):
    return (i > (1.0/3.0) * xSize and i < (2.0/3.0) * xSize and j > (1.0/3.0) * ySize and 
      j < (2.0/3.0) * ySize and k < (1.0/3.0) * zSize)

  blocks = []
  xSize = 10
  ySize = 10
  zSize = 5
  for i in range(xSize):
    for j in range(ySize):
      for k in range(zSize):
        cuGrade = 0.0
        auGrade = 0.0
        if isBlockInCore(i, j, k, xSize, ySize, zSize):
          cuGrade += random.random() / 2.0
          auGrade += random.random() / 2.0
        blocks.append({
          "x": i,
          "y": j,
          "z": k,
          "au" : auGrade,
          "cu" : cuGrade,
        })
  return blocks

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
      "name": "sm2"
    }
  ]
  return jsonify(block_models)

@app.route('/api/block_models/<name>/blocks/', methods=['GET'])
def blocks(name):
  return jsonify(generateBlocks())

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'
    return response

app.run()