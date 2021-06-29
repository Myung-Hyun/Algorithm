from collections import deque

n = int(input())
space=[]
fish=[]


for i in range(n):
  space.append(list(map(int,input().split())))

#처음 아기상어 위치, 물고기 위치+물고기 크기
for i in range(n):
  for j in range(n):
    if space[i][j]==9:
      x,y=i,j
    elif space[i][j] !=0:
      fish.append((i,j,space[i][j]))

# print(x,y)
# print(fish)