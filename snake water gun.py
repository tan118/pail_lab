'''s=1
g=0
w=-1
'''
import random
computer=random.choice([-1,0,1])
compdict={1:"snake",-1:"water",0:"gun"}
youstr=str(input("enter your choice(s,w,g)"))
youdict={"s":1,"w":-1,"g":0}
you=youdict[youstr]

print(f"you chose:{compdict[you]}\n computer chose {compdict[computer]}")

if(computer==youstr):
    print("draw")
else:
 if(computer==1 and you==0):
    print("you win")
 elif(computer==1 and you==-1):
    print("you lose")
 elif(computer==0 and you==1):
    print("you lose")
 elif(computer==0 and you==-1):
    print("you win")
 elif(computer==-1 and you==0):
    print("you lose")
 elif(computer==-1 and you==1):
    print("you win")
 else :
    print("something went worng")


