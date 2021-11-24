fib = [0,1,1,2,3,5,8]
st_no = 0
second_no = 0
first_no = 1
fib_nos =[]
current_no = 1

for i in range(5):
  
  current_no = first_no + second_no
  first_no,second_no = second_no, current_no
  
  fib_nos.append(current_no)

print(fib_nos)