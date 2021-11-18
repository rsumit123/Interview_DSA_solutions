import copy
in_array = [(1,5),(8,12),(2,6),(7,10)]
# in_array = [(1, 3), (2, 5), (3,4), (8, 10), (9, 11), (15, 21)]
# 


# all_intervals = []




# all_intervals = {}
# for intervals in range(len(in_array)):
#   all_intervals[intervals] = []
#   for intervals1 in range(intervals,len(in_array)):
#     if in_array[intervals][0]<=in_array[intervals1][0]<=in_array[intervals][1] or in_array[intervals][0]<=in_array[intervals1][1]<=in_array[intervals][1]:
#       all_intervals[intervals].append(intervals1)


# print(all_intervals)
# for keys,values in all_intervals.items():
#   for inters in values:
#     all_intervals[keys].extend(all_intervals[inters])
    
#     all_intervals[keys] = list(set(all_intervals[keys]))

# new_intervals = copy.deepcopy(all_intervals)

# for keys,values in new_intervals.items():
#   local_int = []
#   for i in values:
#     if keys!=i and i in new_intervals:
#       try:
#         del all_intervals[i]
#       except:
#         pass

# big_list = []
# for values in all_intervals.values():
#   big_list.append(list(map(lambda x : in_array[x],values)))
# print()
# print(big_list)


stack_top=[]
in_array = [(1, 3), (2, 5), (8, 10), (9, 11), (15, 21)]

in_array = sorted(in_array, key= lambda x:x[0])
print(in_array)
stack_top.append([in_array[0]])
for i in in_array[1:]:
  top = stack_top[-1].copy()
  for j in top:
    print("checking with",stack_top[-1])
    print("checking for i",i)
    
    

    if j[0] <= i[0] <= j[1] or j[0] <= i[1] <= j[1] :
        print("interval found")
        stack_top[-1].append(i)
        break
    else:
      stack_top.append([i])
      break
        
      
    
  print("stacktop",stack_top)
  


  
  






