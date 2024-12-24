#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      DELL
#
# Created:     21-02-2024
# Copyright:   (c) DELL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# ROCK.PAPPER,SCISSOR GAME

import random
l=["rock","paper","scissor"]
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game Start....
1 Yes
2 No | Exit

    '''))
    if uc==1:
        for a in range(1,6):
            userinput=int(input('''
1 Rock
2 Paper
3 Scissor

            '''))
            cchoice=random.choice(l)
            if userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="paper"
            elif userinput==3:
                uchoice="scissor"

            if cchoice==uchoice:
                print("Computer value ",cchoice)
                print("User value ",uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice=="rock" and cchoice=="scissor" or uchoice=="paper" and cchoice=="rock" or uchoice=="scissor" and cchoice=="paper"):
                print("Computer value ",cchoice)
                print("User value ",uchoice)
                print("You Win")
                ucount=ucount+1
            else :
                print("Computer value ",cchoice)
                print("User value ",uchoice)
                print("Computer win")
                ccount=ccount+1
        if(ucount>ccount):
            print("Final You Win The Game...")
            print("User Score",ucount)
            print("Computer Score",ccount)
        elif ucount<ccount:
            print("Final Computer Win The Game...")
            print("User Score",ucount)
            print("Computer Score",ccount)

        else:
            print("Game Draw...")
            print("User Score",ucount)
            print("Computer Score",ccount)

    else:
        break