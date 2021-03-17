print("Welcome to this Game!")

print('''Rules :
1 You have 3 Attemepts 
2 Guess the Correct number to win
3 You can take a hint''')

secret = 9
guess_count = 0
guess_avaliable = 3 

while guess_count < guess_avaliable:
    guess = int(input("Guess: "))
    guess_count  += 1
    if guess == secret:
        print("You win")
        break
else:
    print("You Lose")

    

