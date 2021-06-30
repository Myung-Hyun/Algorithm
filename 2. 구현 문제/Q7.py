#Q7 럭키 스트레이트


S=input()

left=0
right=0

for i in range(0,len(S)//2):
  left += int(S[i])

for i in range(len(S)//2,len(S)):
  right+= int(S[i])

# print(left)
# print(right)

if left==right:
  print('LUCYK')
else:
  print('READY')