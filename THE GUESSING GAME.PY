
import random
def game():
    print("you are playing this game")
    score=random.randint(1,600)
    with open("sample.txt")as f:
        hi_score=f.read()

        if (int(hi_score=="" or hi_score==0)):
         print("hi_score=0")
        else:
           print ("hi_score is")
           print (int(hi_score))

    print(f"your score is {score}")           
    if (int(score) > int(hi_score)):
       print(f"you have set new hi_score{score}")
       with open("sample.txt","w")as f:
          f.write(str(score))
    else:
       print("try again")
game()


