# Import the libraries
import pyautogui
import time
import pytesseract
from PIL import ImageGrab
from PIL import Image
import random
import pyscreeze
import PIL

__PIL_TUPLE_VERSION = tuple(int(x) for x in PIL.__version__.split("."))
pyscreeze.PIL__version__ = __PIL_TUPLE_VERSION


sw, sh = pyautogui.size()
middleOfSCreen= (sw/2, sh/2)

def myTurn():
    
    time.sleep(3)
    print("it's your turn!")
    turnTime = 50

    # #play the highest cost card

    # if(pyautogui.locateCenterOnScreen("5manaLeft.png",  confidence=0.6)!=None):
    #     fiveManaLeft=pyautogui.locateCenterOnScreen("5manaLeft.png",  confidence=0.5)
    #     fml=(fiveManaLeft.x/2, fiveManaLeft.y/2)
    #     pyautogui.moveTo(fml,None,1)
    #     pyautogui.dragTo(middleOfSCreen, button='left', duration=1)
    #     pyautogui.moveTo(19, 395, 1.5)

    # if(pyautogui.locateCenterOnScreen("5manaMiddle.png",  confidence=0.6)!=None):
    #     fiveManaMiddle=pyautogui.locateCenterOnScreen("5manaMiddle.png",  confidence=0.5)
    #     fmm=(fiveManaMiddle.x/2, fiveManaMiddle.y/2)
    #     pyautogui.moveTo(fmm,None,1)
    #     pyautogui.dragTo(middleOfSCreen, button='left', duration=1)
    #     pyautogui.moveTo(19, 395, 1.5)

    # if(pyautogui.locateCenterOnScreen("5manaRight.png",  confidence=0.6)!=None):
    #     fiveManaRight=pyautogui.locateCenterOnScreen("5manaRight.png",  confidence=0.5)
    #     fmr=(fiveManaRight.x/2, fiveManaRight.y/2)
    #     pyautogui.moveTo(fmr,None,1)
    #     pyautogui.dragTo(middleOfSCreen, button='left', duration=1)
    #     pyautogui.moveTo(19, 395, 1.5)

    # if(pyautogui.locateCenterOnScreen("3manaLeft.png",  confidence=0.6)!=None):
    #     threeManaLeft=pyautogui.locateCenterOnScreen("3manaLeft.png",  confidence=0.5)
    #     tml=(threeManaLeft.x/2, threeManaLeft.y/2)
    #     pyautogui.moveTo(tml,None,1)
    #     pyautogui.dragTo(middleOfSCreen, button='left', duration=1)
    #     pyautogui.moveTo(19, 395, 1.5)

    # if(pyautogui.locateCenterOnScreen("3manaMiddle.png",  confidence=0.6)!=None):
    #     threeManaMiddle=pyautogui.locateCenterOnScreen("3manaMiddle.png",  confidence=0.5)
    #     tmm=(threeManaMiddle.x/2, threeManaMiddle.y/2)
    #     pyautogui.moveTo(tmm,None,1)
    #     pyautogui.dragTo(middleOfSCreen, button='left', duration=1)
    #     pyautogui.moveTo(19, 395, 1.5)


    # if(pyautogui.locateCenterOnScreen("3manaRight.png",  confidence=0.6)!=None):
    #     threeManaRight=pyautogui.locateCenterOnScreen("3manaRight.png",  confidence=0.5)
    #     tmr=(threeManaRight.x/2, threeManaRight.y/2)
    #     pyautogui.moveTo(tmr,None,1)
    #     pyautogui.dragTo(middleOfSCreen, button='left', duration=1)
    #     pyautogui.moveTo(19, 395, 1.5)


    #click hero power, might be an issue if hero power is not green
    print("going to use my hero power!")
    if(pyautogui.locateCenterOnScreen("heroPower.png", confidence=0.7)!=None):
        HeroPower = pyautogui.locateCenterOnScreen("heroPower.png", confidence=0.7)
        hp1 = (HeroPower.x/2, HeroPower.y/2)
        pyautogui.moveTo(hp1, None, random.uniform(0.1,0.8))
        pyautogui.click()
    elif(pyautogui.locateCenterOnScreen("heroPower.png", confidence=0.6)!=None):
        HeroPower = pyautogui.locateCenterOnScreen("heroPower.png", confidence=0.7)
        hp1 = (HeroPower.x/2, HeroPower.y/2)
        pyautogui.moveTo(hp1, None, random.uniform(0.1,0.8))
        pyautogui.click()
    else:
        print("WARNING: Hero Power not found")

    time.sleep(0.5)
    pyautogui.moveTo(19, 395, 1.5)

    print("time to sleep")
    time.sleep(2)



    #click end turn
    print("time to end my turn")
    showing = False
    numberOfFails=1
    while(showing!=True):
        if(pyautogui.locateCenterOnScreen("gameOver.png", confidence=0.9)!=None):
            showing=True
            gameOver()
        if(pyautogui.locateCenterOnScreen("endTurn.png", confidence=0.4)!=None):
            endTurn=pyautogui.locateCenterOnScreen("endTurn.png", confidence=0.4)
            et1 = (endTurn.x/2, endTurn.y/2)
            pyautogui.moveTo(et1, None, random.uniform(0.1,0.8))
            pyautogui.click()
            pyautogui.moveTo(56,299, random.uniform(0.1, 2))
            showing=True
            opponentsTurn()

        if(pyautogui.locateCenterOnScreen("yourTurn.png", confidence=0.5)!=None):
            endTurn2=pyautogui.locateCenterOnScreen("yourTurn.png", confidence=0.5)
            et2 = (endTurn2.x/2, endTurn2.y/2)
            pyautogui.moveTo(et2, None, random.uniform(0.1,0.8))
            pyautogui.click()
            pyautogui.moveTo(56,299, random.uniform(0.1, 2))
            showing=True
            opponentsTurn()

       
        print(f"I've looped through {numberOfFails} times, I can't see the end turn button.")
        numberOfFails+=1
        

    print(("something isn't working, going to opponents turn"))
    
    opponentsTurn()
     
def opponentsTurn():
    if(pyautogui.locateCenterOnScreen("gameOver.png", confidence=0.9)!=None):
            gameOver()
    print("it's your opponents turn!")

    #move mouse every once in a while, keep it off minions or cards in my hand
    your_turn=False
    while(your_turn!=True):
        if(pyautogui.locateCenterOnScreen("yourTurn.png", confidence=0.5)!=None):
            your_turn=True
            myTurn()
        if(pyautogui.locateCenterOnScreen("endTurn.png", confidence=0.5)==None):
            your_turn=True
            myTurn()
        if(pyautogui.locateCenterOnScreen("gameOver.png", confidence=0.9)!=None):
            your_turn=True
            gameOver()

def gameOver():
    print("GAME OVER  GAME OVER  GAME OVER")
    pyautogui.moveTo(900, 240, 0.5)
    time.sleep(4)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(1090, 745, random.uniform(0.2,0.5))
    pyautogui.click()
    pyautogui.click()
    time.sleep(3)
    pyautogui.click()
    mulligan()
    
def oddWarriorHearthstone(screenWidth, screenHeight):

    # click hearthstone
    res = pyautogui.locateCenterOnScreen("HsBtn.png", confidence=0.6)
    Hearthstone=(res.x/2, res.y/2)
    pyautogui.moveTo(Hearthstone, None, random.uniform(0.1,0.8))
    pyautogui.click()
    time.sleep(2)

    
    #clicks on deck
    deck = pyautogui.locateCenterOnScreen("deck.png", confidence=0.5)
    d1 = (deck.x/2, deck.y/2)
    pyautogui.moveTo(d1, None, random.uniform(0.4,0.9))
    pyautogui.click()
    time.sleep(random.uniform(0.1, 0.4))


    #starts queue
    start=pyautogui.locateCenterOnScreen("PlayBtn.png", confidence=0.5)
    s1 = (start.x/2, start.y/2)
    pyautogui.moveTo(s1, None, random.uniform(0.2,0.5))
    pyautogui.click()

    mulligan()

def mulligan():
    count=0
    flag=False
    print("You are now in the queue")
    cards=0
    while(flag!=True):
        print(f"Looping through, this is try {count}.")
        count+=1
        if(pyautogui.locateCenterOnScreen("inGame.png", confidence=0.7)!=None):
            print("you are now in the mulligan, time to pick a hand")
            # while(cards<4):
            #     if(pyautogui.locateCenterOnScreen("Mulligan5.png",  confidence=0.5)!=None):
            #         MulliganFive=pyautogui.locateCenterOnScreen("Mulligan5.png",  confidence=0.5)
            #         m5=(MulliganFive.x/2, MulliganFive.y/2)
            #         pyautogui.moveTo(m5,None,1)
            #         pyautogui.click()
            #         pyautogui.moveTo(1125, 700, 1.5)
            #     cards+=1
            time.sleep(40)
            beginGame=pyautogui.locateCenterOnScreen("inGame.png", confidence=0.5)
            bg1 = (beginGame.x/2, beginGame.y/2)
            pyautogui.moveTo(bg1, None, random.uniform(0.2,0.5))
            pyautogui.click()
            print("Clicked the confirm button!")
            flag=True
    time.sleep(6)
    whose_turn_is_it()
    
def whose_turn_is_it():
    print("Who's turn is it? lets find out")
    failCounter=0
    flag2=False
    while (flag2!=True):
        if(pyautogui.locateCenterOnScreen("yourTurn.png", confidence=0.4)!=None):
            print("it's your turn! pulling up the method...")
            flag2=True,
            myTurn()
        if(pyautogui.locateCenterOnScreen("EnemyTurn.png", confidence=0.4)!=None):
            print("it's your opponenets turn, pulling up the method...")
            flag2=True
            opponentsTurn()
        print(f"finished loop {failCounter}, didn't find anything")
        failCounter+=1
        
# Define the main function
def main():
    # Wait for 3 seconds before starting
    time.sleep(3)

    # Get the size of the screen
    screenWidth, screenHeight = pyautogui.size()

    oddWarriorHearthstone(screenWidth, screenHeight)
    input()

    #capture_image(screenWidth, screenHeight,"Barrens_1st_Boss_victory",200,300)
    
# Run the main function
if __name__ == "__main__":
    main()
