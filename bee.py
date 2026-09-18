letters = ["a","e","h","t","m","i"]

w_dictionary = {
    'ate':1,
    'eat':1,
    'meat':1,
    'team':1,
    'time':1,
    'mate':1,
    'heat':1,
    'hate':1,
    'them':1,
    'tea':1
}


print("==============================")
print("         Bee world            ")
print("==============================")

print("\n your 6 letters are: ")
for letter in letters:
    print(letter.upper(),end="")

print("\n")

r_words=list(w_dictionary.keys())
points=0
game_over=False

print("Finding words using these letters.")
print("you have 3 attempts for each word.")
print("Each correct word gives points.")
print(".................")

while len(r_words)>0:
    print("\nWords remaining: ", len(r_words))
    print("current points: ",points)
    attempts=3
    correct=False


    while attempts > 0:

        
        guess= input("Enter your word: ").lower()
        if guess in r_words:
            earned=w_dictionary[guess]
        
            points += earned

            print("correct! ")
            print("your earned: ",earned)
            r_words.remove(guess)
            correct=True
            break
        else:
            attempts -=1
            if attempts >0:
                print("\nwrong guess! ")
                print("attempts remaining: ",attempts)

            else:
                print("\nwrong guess! ")
                print("No attempts remaining.")
                game_over=True
                break

    if game_over:
        break

if correct == False :
    print("\n_____GAME OVER____")
    print("Total points earned: ",points)
    print("words still remaining: ",len(r_words))


if len(r_words) == 0:
    print("\n\n")
    print("======GAME OVER======")
    print("======CONGRATULATION=====")
    print("you found all words! ")
    print("Total points earned: ",points)