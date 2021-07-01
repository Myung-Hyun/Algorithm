#Q11 뱀

n = int(input())
k = int(input())

graph=[[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
  x, y = map(int,input().split())
  graph[x][y]=1

l = int(input())
move=[]
for _ in range(l):
  move_time, rotate_direc= input().split()
  move.append((int(move_time), rotate_direc))

#동 남 서 북
dx=[0,1,0,-1]
dy=[1,0,-1,0]
direction =0

def turn(direction, rotate_direc):
  if rotate_direc=='L':
    direction = (direction -1) % 4
  if rotate_direc=='D':
    direction = (direction +1) % 4
  return direction

#뱀의 머리 위치
x=1
y=1
#뱀이 있는 곳은 2로 표시, 뱀의 위치 정보 리스트에 저장(2와 0으로 바꿀 좌표 저장)
graph[x][y]=2
snake=[(x,y)]

time_count=0
break_all=False

for i in range(len(move)):
  for j in range(move[i][0]):
    nx=x + dx[direction]
    ny=y + dy[direction]
    #print(snake)
    print(nx,ny)
    # 다음 움직일 칸에 자기자신 또는 벽이 있는 경우
    if nx<=0 or nx>=n+1 or ny<=0 or ny>=n+1:
      time_count +=1
      break_all=True
      break 
    elif graph[nx][ny] == 2:
      time_count +=1
      break_all=True
      break 
    else:

      # 다음 움직일 칸에 사과가 있는 경우
      if graph[nx][ny] == 1:    
        graph[nx][ny]=2
        snake.append((nx,ny))
      elif graph[nx][ny] == 0:
        px,py = snake.pop(0)
        graph[px][py]=0
        graph[nx][ny]=2
        snake.append((nx,ny))
      else:
        pass
      
      x,y =nx, ny
      time_count +=1
  if break_all==False:
    direction=turn(direction, move[i][1])
  else:
    break

print(time_count)



  






