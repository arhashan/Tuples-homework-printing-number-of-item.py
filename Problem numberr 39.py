thing = input("Enter a name of a thing: ")
rev_thing = ""  #we use this code to create an empty box where we will build the reversed word step by step.
for m in thing:
    rev_thing = m + rev_thing
if rev_thing == thing:
    print("It is Palindrome!")
else:
    print("Sorry! It is not palindome!")    