# RUN LENGTH ENCODING AND DECODING
string1 = "aaaabbbccccaaaaaaeee"
string2 = "a4b3c4a6e3"


count = 1
string1 += "#"
result_str = ""
for i in range(1,len(string1)):
  if string1[i] == string1[i-1]:
    count+=1
  else:
    result_str+=string1[i-1]+str(count)
    count=1



  
print(result_str)

encoded_str = ""
for i in range(1,len(result_str),2):
  # print(result_str[i])
  encoded_str = encoded_str + result_str[i-1]*int(result_str[i])
print(encoded_str)

l1 = [2,10,8,5,6]
k = 13
