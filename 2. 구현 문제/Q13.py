
#Q13 치킨 배달

from itertools import combinations

n, m = map(int, input().split())
graph=[]
chicken=[]
home=[]

for _ in range(n):
  graph.append(list(map(int,input().split())))

for i in range(len(graph)):
  for j in range(len(graph[0])):
    if graph[i][j]==1:
      home.append((i,j))
    elif graph[i][j]==2:
      chicken.append((i,j))

print("chicken: ", chicken)
print("home:", home)

def city_chicken_dist(canditate):
  city_dist=0
  
  for home_x, home_y in home:
    chicken_dist=int(1e9)
    for chicken_x, chicken_y in candidate:
      # print("home_x, home_y", home_x, home_y )
      # print("chicken_x, chicken_y", chicken_x, chicken_y )
      chicken_dist=min(chicken_dist,abs(chicken_x-home_x) + abs(chicken_y-home_y))
      #print(chicken_dist)
    city_dist +=chicken_dist
  
  return city_dist

candidates = list(combinations(chicken,m))
print("candidates: ", candidates)
result=int(1e9)

for candidate in candidates:
  
  result=min(result,city_chicken_dist(candidate))

print(result)










