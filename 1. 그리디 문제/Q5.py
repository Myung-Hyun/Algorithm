#Q5 볼링공 고르기

n, m=map(int, input().split())
balls=list(map(int,input().split()))

balls.sort()
ball_num=[0]*(m+1)

for ball in balls:
  for i in range(1,m+1):
    if ball == i:
      ball_num[i] +=1
# print(ball_num)

result=0
for i in range(1,m+1):
  for j in range(i,m):
    result += ball_num[i] * ball_num[j+1]

print(result)