numbers = (3 , 45 , 56 , 7, "bangladesh" , "River" , 29.89 , "bangladesh" , 90) 

print(numbers) 
print(len(numbers))
print(type(numbers))

numbers = list(numbers)

print(numbers)
numbers[1] = 54 
print(numbers)
numbers = tuple(numbers)
print(numbers)


