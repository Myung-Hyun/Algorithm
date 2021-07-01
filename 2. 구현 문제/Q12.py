
#Q12 기둥과 보 설치
print("Q12")

def solution(n,build_frame):
  result=[]
  for build in build_frame:
    x, y, stuff, operation = build
    # 구조물 설치
    if operation ==1:
      result.append([x,y,stuff])
      if possible(result) == False:
        result.remove([x,y,stuff])
    # 삭제
    else:
      result.remove([x,y,stuff])
      if possible(result) == False:
        result.append([x,y,stuff])
    
  return result

def possible(result):
  for x,y,stuff in result:
    # 기둥인 경우
    if stuff ==0:
      if y==0 or [x-1,y,1] in result or [x,y,1] in result or [x,y-1,0] in result:
        continue
      return False
    # 보인 경우
    else:
      if [x,y-1,0] in result or [x+1,y-1,0] in result or ([x-1,y,1] in result and [x+1,y,1] in result):
        #print(1)
        continue
      return False
  #print(3)
  return True

n=5
build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

result= solution(5,build_frame)
result.sort()
print(result)


