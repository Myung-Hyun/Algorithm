
#Q10 자물쇠와 열쇠

def solution(key, lock):
  n=len(lock)
  new_lock=[[0]*3*n for _ in range(3*n)]

  for i in range(n,2*n):
    for j in range(n,2*n):
      new_lock[i][j]=lock[i-n][j-n]
  #temp=new_lock
  #print(temp)

  for _ in range(4):
    key=rotate(key)
    for x in range(2*n):
      for y in range(2*n):
        #new_lock=temp
        #print(new_lock)
        for i in range(n):
          for j in range(n):
            new_lock[i+x][j+y]=new_lock[i+x][j+y]+key[i][j]
        if check(new_lock):
          #print(new_lock)
          return True
        else:
          for i in range(0,3*n):
            for j in range(0,3*n):
              new_lock[i][j]=0
          for i in range(n,2*n):
            for j in range(n,2*n):
              new_lock[i][j]=lock[i-n][j-n]
          continue
        
  return False


def rotate(key):
  m=len(key)
  result = [[0]*m for _ in range(m)]

  for i in range(m):
    for j in range(m):
      result[j][m-i-1] = key[i][j]

  return result


def check(new_lock):
  n =len(new_lock)//3

  for i in range(n,2*n):
    for j in range(n,2*n):
      if new_lock[i][j]==0 or new_lock[i][j]==2:
        return False
      else:
        continue
  
  return True

print(solution([[1,1,0],[0,1,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))









