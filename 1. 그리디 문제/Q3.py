#Q3 문자열 뒤집기

S=input()

before=S[0]
count=0

if before=='1':
  for i in range(1,len(S)):
    if before!=S[i]:
      before=S[i]      
      if S[i]=='0':
        count +=1
else:
  for i in range(1,len(S)):
    if before!=S[i]:
      before=S[i]
      if S[i]=='1':
        count +=1
        
print(count)