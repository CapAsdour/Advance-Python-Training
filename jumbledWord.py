# this is a game of guessing the word 
import random
def choose():
    ar=["rainbow","winter","coming"]
    pick=random.choice(ar)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
    
def play():
    p1=input("player 1 plz enter your name")
    p2=input("player 1 plz enter your name")
    pp1=0
    pp2=0
    count=0
    while(True):
        picked_word=choose()
        jumbled_word=jumble(picked_word)
        if count%2==0:
            print(p1,"your turn")
            print(jumbled_word)
            guessed=input("enter the correct word   ")
            if guessed == picked_word:
                pp1+=1
            else:
                print("your guess was wrong . Correct word is ",picked_word)
            c=int(input("press 1 to continue or 0 to leave"))
            if c== 0:
                print("thanks for playing")
                break
            else:
                print(p1,p2,"scores",pp1,pp2)
        else:
            print(p2,"your turn")
            print(jumbled_word)
            guessed=input("enter the correct word      ")
            if guessed == picked_word:
                pp2+=1
            else:
                print("your guess was wrong . Correct word is ",picked_word)
            c=int(input("press 1 to continue or 0 to leave"))
            if c== 0:
                print("thanks for playing")
                break            
            else:
                print(p1,p2,"scores",pp1,pp2)
                
        count+=1
play()        