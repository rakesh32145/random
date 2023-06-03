# ROCK PAPER SCISSORS GAME(USING RAMDOM MODULE) PYTHON PROJECT
import random
l=["rahul","rakesh","kanha"]
'''
rahul vs kanha-> kanha wins
rahul vs rakesh-> rahul wins
kanha vs rakesh-> rakesh wins
'''
while True:
    count=0
    ucount=0
    uc=int(input('''    
Game start...
1 yes
2 no | Exit
       '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
1 Rahul
2 Rakesh
3 Kanha
'''))
            if userinput==1:
                uchoice="rahul"
            elif userinput==2:
                uchoice="rakesh"
            elif userinput==3:
                uchoice="kanha"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("computer value",Cchoice)
                print("User value",uchoice)
                print("game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="rahul" and Cchoice=="rakesh") or (uchoice=="kanha" and Cchoice=="rahul") or (uchoice=="rakesh" and Cchoice=="kanha"):
                print("computer value",uchoice)
                print("user value",Cchoice)
                print("you win")
                ucount=ucount+1
            else:
                print("computer value",Cchoice)
                print("user value",uchoice)
                print("Computer win")
                ccount=ccount+1

        if ucount==ccount:
            print("final game draw...")
            print("user score",ucount)
            print("computer score",ccount)

        elif ucount>count:
            print("final you win the game...")
            print("user score",ucount)
            print("computer score",ccount)

        else:
            print("final computer win the game...")
            print("user score",ucount)
            print("computer score",ccount)   
        

            
    else:
        break
