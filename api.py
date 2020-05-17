import flask
from flask import jsonify
import random

app = flask.Flask(__name__)

def generateBlocks():
  def isBlockInCore(i, j, k, xSize, ySize, zSize):
    return (i > (1.0/3.0) * xSize and i < (2.0/3.0) * xSize and j > (1.0/3.0) * ySize and 
      j < (2.0/3.0) * ySize and k < (1.0/3.0) * zSize)

  blocks = []
  xSize = 20
  ySize = 20
  zSize = 10
  for i in range(xSize):
    for j in range(ySize):
      for k in range(zSize):
        cuGrade = 0.0
        auGrade = 0.0
        if isBlockInCore(i, j, k, xSize, ySize, zSize):
          cuGrade += random.random() / 2.0
          auGrade += random.random() / 2.0
        blocks.append({
          "x_index": i,
          "y_index": j,
          "z_index": k,
          "au" : auGrade,
          "cu" : cuGrade,
        })
  return blocks

@app.route('/api/blocks/', methods=['GET'])
def blocks():
  return jsonify(generateBlocks())

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'
    return response

app.run()