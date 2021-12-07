# FibArray = [0, 1]
 
# def fibonacci(n):
   
#     # Check is n is less
#     # than 0
#     if n <= 0:
#         print("Incorrect input")
         
#     # Check is n is less
#     # than len(FibArray)
#     elif n <= len(FibArray):
#         return FibArray[n - 1]
#     else:
#         temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
#         FibArray.append(temp_fib)
#         return temp_fib
 




fib_array = [0,1,1]

def fibonacci(n):
  if n<=0:
    return "Incorrect"
  
  if n <= len(fib_array):
    print(f"Called for n={n}")
    return fib_array[n-1]
  
  else:
    print(f"Calculating for n={n}")
    temp = fibonacci(n-1) + fibonacci(n-2)
    fib_array.append(temp)
    return temp


print(fibonacci(10))
print(fib_array)


def fibonacci(n):
 
  if n==0 :
    return 0
  if n== 1 or n==2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))

