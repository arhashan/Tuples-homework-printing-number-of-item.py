game = input("Enter a game name: ")
rev_game = ""
for char in game:
    rev_game = char + rev_game
print("reverse string is " + rev_game)    
if game == rev_game:
    print("They are pallindrome")
else:
    print("They are  not pallindrome")    