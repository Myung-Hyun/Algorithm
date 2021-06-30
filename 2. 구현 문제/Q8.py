#Q8 문자열 재정렬


S=list(input())

S.sort()
#print(S)
num=0
alpha=''

for i in S:
  if i.isalpha() != True:
    num += int(i)
  else:
    #print(alpha)
    alpha =alpha + i

print(alpha+str(num))