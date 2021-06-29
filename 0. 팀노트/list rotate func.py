def rotate(key):
  m=len(key)
  result = [[0]*m for _ in range(m)]

  for i in range(m):
    for j in range(m):
      result[j][m-i-1] = key[i][j]

  return result