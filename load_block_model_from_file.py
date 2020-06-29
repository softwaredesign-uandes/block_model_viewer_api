from itertools import starmap

def load_block_model_from_file(block_model_name, columns):
  def to_float(value):
    try:
      return float(value)
    except ValueError:
      return value

  def line_to_dict(line):
    return dict(zip(columns, map(to_float, line.split(' '))))

  blocks = []
  with open('files/' + block_model_name + '.blocks') as text_file:
    blocks = list(map(line_to_dict, text_file.read().split('\n')))

  return { "block_model": { "blocks" : blocks } }
