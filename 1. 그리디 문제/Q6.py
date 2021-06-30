#Q6 무지의 먹방 라이브

import heapq


def solution(food_times, k):
  answer = 0
  q=[]
  length=len(food_times)

  if sum(food_times)<=k:
    return -1

  #(음식시간, 음식번호)
  for i in range(len(food_times)):
    heapq.heappush(q,(food_times[i],i+1))
  
  # 
  # while q:
  #   food=heapq.heappop(q)
  #   k=k-length*food[0]
  #   length -=1
  #   if k<=0:
  #     answer=(food[1]+1)%len(food_times)
  #     break;

  return answer

print(solution([8,6,4],15))