#Q2 곱하기 혹은 더하기

S=input()

result=int(S[0])

for i in range(1,len(S)):
  number = int(S[i])
  if number <=1 or result <=1:
    result +=number
  else:
    result *=number

print(result)
