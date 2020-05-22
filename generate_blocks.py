def generate_blocks(xSize, ySize, zSize):
  def is_block_in_core(i, j, k, xSize, ySize, zSize):
    return (i > (1.0/3.0) * xSize and i < (2.0/3.0) * xSize and j > (1.0/3.0) * ySize and 
      j < (2.0/3.0) * ySize and k < (1.0/3.0) * zSize)

  blocks = []
  for i in range(xSize):
    for j in range(ySize):
      for k in range(zSize):
        cuGrade = 0.0
        auGrade = 0.0
        if is_block_in_core(i, j, k, xSize, ySize, zSize):
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