# search a number into the list , if you find just return true on the other hand return false .

arr = []
for i in range(5):
   n = int(input("enter your number: "))
   arr.append(n)

print(arr)

num = int(input("enter your number: "))


flag = False 

for n in arr:
    if num == n:
        flag = True
        break
    
    else:
       flag = False 


if flag == True:
    print("True")
else:
   print("False")


