def solution(s):
  newS = []
  for i in range (0, len(s)):
    if i % 2 == 0:
          if(len(s) == i +1):
            newS.append(s[i]+'_')
          else:
            newS.append(s[i]+ s[i+1])
  return newS
  
print(solution("abcd"))