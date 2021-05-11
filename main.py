import random

with open('list.txt','r') as f:
    words = f.readlines()

word=random.choice(words)[:-1]


allowed_errors=7
guesses=[]
done=False

while not done:
    for letters in word:
        if letters.lower() in guesses:
            print(letters,end=" ")
        else:
            print("_",end=" ")
    print(" ")

    guess=input(f"Allowed errors left {allowed_errors},Next guess:")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break
for letter in words:
     if letter.lower() not in guess:
        done=False
if done:
    print(f"you have founded the word.it is {word}")
else:
    print(f"Game Over the word was {word}")

