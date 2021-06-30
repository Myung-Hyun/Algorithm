#Q1 모험가 길드

horror = list(map(int,input().split()))
horror.sort()

member=0
group=0

for i in horror:
  member += 1
  if member >= i:
    group +=1
    member =0

print(group)