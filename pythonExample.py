s = 0
list = [2 ,3 ,4 ,6 ,8]
for num in list:
    s = s + num
    print(s)


#find the maximum element without using built in function 

list = [2 ,3 ,4 ,10000,5]
maxi = list[0]
for n in list:
    if n > maxi:
     maxi = n 

print("Maximum: ",maxi)
 


#find the minimum element without using built in function 
list = [2 ,3 ,4 ,-6 ,-8]
min = list[0] # min = 2 
for n in list:
   if n < min:
      min = n 

print("Manimum: ",min)

#reverse the list without using the built in funciton 
list = [2 ,3 ,4 ,6 ,8]
rev_list = []
length = len(list) 

for i in range(length-1 , -1 , -1):
   rev_list.append(list[i])

print(rev_list)





#count the number of even and odd numbers .
list = [2 ,3 ,4 ,6 ,8 , 55]
even = 0 
odd = 0 
for n in list:
  if(n % 2 == 0):
     even = even + 1 
  else:
     odd = odd + 1
     
print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd)



