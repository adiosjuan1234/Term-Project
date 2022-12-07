from cmu_112_graphics import *
import math
import random
import decimal
import ast

######################################
# appStarted
######################################

def appStarted(app):

    # Open up the window with the start menu
    app.mode = 'startMenu'

    # Canvas center coords for convenience
    app.cx = app.width/2
    app.cy = app.height/2

    # Image code credit: # https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#loadImageUsingUrl

    # Start Menu Images
    app.startMenuImage = app.loadImage('Start Menu Image.jpeg')
        # https://imgs.search.brave.com/VAmtw9ECmanDxPKW_k0OLQg6rIccFpHUOjbVN8FXVig/rs:fit:1024:768:1/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJhY2Nlc3Mu/Y29tL2Z1bGwvMjEz/OTgwMS5qcGc
    app.scaledStartMenu = app.scaleImage(app.startMenuImage, 2.6)
    app.marioKart112 = app.loadImage('Mario Kart 112.png')
        # https://fontmeme.com/super-mario-font/

    # Map Select Images
    app.mushroomCupImage= app.loadImage('Mushroom Cup.jpeg')
        # https://imgs.search.brave.com/tYLnsQg_6bhK4LRFkrHYkczS_dLVaV0jshY2UpPsvz0/rs:fit:474:225:1/g:ce/aHR0cHM6Ly90c2Ux/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5B/dm9yM2tWX1FfMUlM/UWlfUUVfbFBBSGFI/YSZwaWQ9QXBp
    app.mushroomCup = app.scaleImage(app.mushroomCupImage, 4/3)
    app.starCupImage = app.loadImage('Star Cup.jpeg')
        # https://imgs.search.brave.com/u3ul2NQsn2r93-gNiuZcQ24jkot2nj9U9Ag2PGZsPhU/rs:fit:474:225:1/g:ce/aHR0cHM6Ly90c2Uz/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC50/endNT0NiQ3NPZkdQ/ZE9rN3d1cjZ3SGFI/YSZwaWQ9QXBp
    app.starCup = app.scaleImage(app.starCupImage, 4/3)
    app.specialCupImage = app.loadImage('Special Cup.jpeg')
        # https://imgs.search.brave.com/f_waJsPeCPhblhbaClvaHp3SnOnvGKQI6RkxrWOPrNk/rs:fit:474:225:1/g:ce/aHR0cHM6Ly90c2U0/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC56/NzJEb1BSTG9icEsz/T3VGRERaWFF3SGFI/YSZwaWQ9QXBp
    app.specialCup = app.scaleImage(app.specialCupImage, 4/3)

    # Character Select Images
    app.mushroomCellImage = app.loadImage('Mushroom Grid Cell.jpeg')
        # https://imgs.search.brave.com/ynN4-fVQvqntZsSchTlvnXpMEeUe8G2QjK-krfO_7Vs/rs:fit:467:225:1/g:ce/aHR0cHM6Ly90c2Ux/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5U/dWRlVEF4VGZaRW5m/R3UzTXFfdWVRSGFI/aCZwaWQ9QXBp
    app.singleMushroom = app.scaleImage(app.mushroomCellImage, 1/5)
    app.starCellImage = app.loadImage('Star Grid Cell.jpeg')
        # https://imgs.search.brave.com/aeNSduQYStBbewGDsHtrVhLTJ5cGnjSO9SAp1ndSjEw/rs:fit:498:225:1/g:ce/aHR0cHM6Ly90c2U0/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5O/NUVCbmFWcEZ5eWVn/YmpxWVhRZ3BRSGFI/RCZwaWQ9QXBp
    app.singleStar = app.scaleImage(app.starCellImage, 1/5)
    app.crownCellImage = app.loadImage('Crown Grid Cell.jpeg')
        # https://imgs.search.brave.com/o8Zs5dTMwXvFALnmtTFy1QA-yoMukdrcyUxAjKr9tlo/rs:fit:494:225:1/g:ce/aHR0cHM6Ly90c2Uz/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5S/em5iN1Vqem1lVFM0/VHkxd0l0Vy13SGFI/RyZwaWQ9QXBp
    app.singleCrown = app.scaleImage(app.crownCellImage, 1/5)
    app.characterSelect = app.loadImage('Character Select.jpeg')
        # https://imgs.search.brave.com/C0F1iCYy5ofXPgYPhfrM_r568ofNa-twnf7OhH6wUvE/rs:fit:844:225:1/g:ce/aHR0cHM6Ly90c2Uz/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC44/M25RdlhfdWZpUnJO/VGlObXdKVzNBSGFF/SyZwaWQ9QXBp
    app.characters = app.scaleImage(app.characterSelect, 3/2)
    app.selectedCharacter = ''

    # Maps
    app.map1 = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
            [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
            [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1],
            [0,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1],
            [0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1],
            [0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1],
            [0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1],
            [0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
            [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
            [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
    app.map2 = [
            [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0],
            [0,0,1,1,1,0,1,0,0,0,0,1,1,1,0,0],
            [0,0,1,1,1,0,1,1,1,1,0,1,1,1,0,0],
            [0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],
            [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0],
            [1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1],
            [1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1],
            [1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1],
            [1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1],
            [0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0],
            [0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],
            [0,0,1,1,1,0,1,1,1,1,0,1,1,1,0,0],
            [0,0,1,1,1,0,0,0,0,1,0,1,1,1,0,0],
            [0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
        ]
    app.map3 = [
            [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,1,1,0,0,0,0,0,1,0,0,0,1,1,1,1],
            [0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,1],
            [0,1,1,1,1,1,1,0,1,0,1,1,0,0,1,1],
            [0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1],
            [1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
            [0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1],
            [0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
            [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0],
            [1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0],
            [1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0],
            [1,1,0,0,1,1,1,1,1,0,1,1,1,1,1,1],
            [1,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0],
            [1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,0],
            [1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0]
        ]
    app.selectedMap = [[]]
    app.mapForScore = ''

    # Racer + Track properties
    app.playerRadius = 1.5
    app.speed = app.playerRadius * 2
    app.playerHitbox = 8
    app.cellWidth = app.height/len(app.map1)
    app.px = app.cellWidth//2
    app.py = app.cellWidth//2
    app.angle = 0
    app.timerDelay = 40
    app.frames = 0
    app.totalTime = 0
    app.totalTimePassed = 0
    app.timePassed = 0
    app.lap = 1
    app.temp = False
    app.checkpoint = False

    # Item box properties
    app.itemboxSprite = app.loadImage('Item Box.png')
    side, _ = app.itemboxSprite.size
    app.itemboxUnscaled = app.scaleImage(app.itemboxSprite, 64/side)
    app.itemMap = []
    app.itembox1 = [(app.cellWidth*11, app.cellWidth), 
                    (app.cellWidth*10, app.cellWidth*9),
                    (app.cellWidth, app.cellWidth*12)]
    app.itembox2 = [(app.cellWidth*5.5, app.cellWidth*2.5), 
                    (app.cellWidth*11, app.cellWidth*15),
                    (app.cellWidth, app.cellWidth*14)]
    app.itembox3 = [(app.cellWidth*9.5, app.cellWidth*1.5), 
                    (app.cellWidth*13, app.cellWidth*12.5),
                    (app.cellWidth*3.5, app.cellWidth*11)]
    
    # Items
    app.currentItem = ''
    app.items = ['mushroom', 'banana', 'golden mushroom', 'fake-itembox']
    app.mushroomSprite = app.loadImage('Mushroom.png')
        # https://imgs.search.brave.com/AN8aCv_VECwW9Ztnmb9-Nm9tcqjPY2XlVp4bgmj1_6c/rs:fit:880:915:1/g:ce/aHR0cHM6Ly9pMi53/cC5jb20vd3d3LnBp/bmNsaXBhcnQuY29t/L3BpY2Rpci9taWRk/bGUvNTI0LTUyNDE4/Nzhfc3VwZXItbWFy/aW8tbXVzaHJvb20t/Y2xpcGFydC1tYXJp/by1rYXJ0LXdpaS1t/dXNocm9vbS5wbmc
    mSize, _ = app.mushroomSprite.size
    app.mushroom = app.scaleImage(app.mushroomSprite, 60/mSize)
    app.bananaSprite = app.loadImage('Banana.png')
        # https://imgs.search.brave.com/qLK4y46nVq7vOzNfB_ZqFBlPaEtnQiUhRCjdNfCBHCI/rs:fit:434:225:1/g:ce/aHR0cHM6Ly90c2U0/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC4w/VjJCMW0tSDZMVm1t/TTVHWWVrekh3SGFH/RyZwaWQ9QXBp
    bSize, _ = app.bananaSprite.size
    app.banana = app.scaleImage(app.bananaSprite, 60/bSize)
    app.goldenMushroomSprite = app.loadImage('Golden Mushroom.png')
        # https://imgs.search.brave.com/PTXJK_FFiSgHuqIY82xSC_3iBSv75ZaGqhWsqVnT3rI/rs:fit:124:225:1/g:ce/aHR0cHM6Ly90c2U0/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5x/LWRDWkVsclNMeDI3/RzVGVGdySmtnQUFB/QSZwaWQ9QXBp
    gSize, _ = app.goldenMushroomSprite.size
    app.goldenMushroom = app.scaleImage(app.goldenMushroomSprite, 60/gSize)
    app.fakeItemBoxSprite = app.loadImage('Fake Item Box.png')
        # https://imgs.search.brave.com/66w4nRr7I2MCCVjaWGonXcf-BXrOHQAqK3qu2LtqmYc/rs:fit:64:64:1/g:ce/aHR0cHM6Ly93d3cu/bWFyaW93aWtpLmNv/bS9pbWFnZXMvMS8x/Yy9NS1dfRmFrZV9J/dGVtX0JveF9TcHJp/dGUucG5n
    fSize, _ = app.fakeItemBoxSprite.size
    app.fakeItemBox = app.scaleImage(app.fakeItemBoxSprite, 60/fSize)
    app.itemsTemp = False
    app.bananaCoords = []
    app.fakeitemboxCoords = []
    app.speedboost = False
    app.collision = False

    # Character Karts
    app.karts = dict()
    app.marioImage = app.loadImage('Mario.png')
        # https://www.google.com/imgres?imgurl=https%3A%2F%2Fmario.wiki.gallery%2Fimages%2Fthumb%2Fa%2Fa0%2FMK8_Mario_Drifting_Standard_Kart_Shadowless_Artwork.png%2F1200px-MK8_Mario_Drifting_Standard_Kart_Shadowless_Artwork.png&imgrefurl=https%3A%2F%2Fwww.mariowiki.com%2FKart&tbnid=FQ_ViX32YnjeCM&vet=12ahUKEwitqO29n9_7AhW5n3IEHQ5oDm4QMygBegUIARDmAQ..i&docid=2uaIM1bxjayIiM&w=1200&h=1027&q=mario%20kart%20mario&client=opera-gx&ved=2ahUKEwitqO29n9_7AhW5n3IEHQ5oDm4QMygBegUIARDmAQ
    app.mario = app.scaleImage(app.marioImage, 1/10)
    app.karts['mario'] = app.mario
    app.luigiImage = app.loadImage('Luigi.png')
        # https://imgs.search.brave.com/hEwto3ZDNL_YcTnNQpOXz96a-rv5YbuaKIcju3gnszs/rs:fit:474:225:1/g:ce/aHR0cHM6Ly90c2Uz/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC53/LWo3d2c5bkhSdUUw/WldNNzJuaDR3SGFI/YSZwaWQ9QXBp
    app.luigi = app.scaleImage(app.luigiImage, 1/10)
    app.karts['luigi'] = app.luigi
    app.peachImage = app.loadImage('Peach.png')
        # https://imgs.search.brave.com/xPP0i7ieWCoPdS1ctLhfpwGk97T9yCu5RHbUa7-McY0/rs:fit:390:225:1/g:ce/aHR0cHM6Ly90c2Ux/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5l/U0RET21ET0dTakRU/SXZWTy0xTEFnSGFJ/XyZwaWQ9QXBp
    app.peach = app.scaleImage(app.peachImage, 1/10)
    app.karts['peach'] = app.peach
    app.toadImage = app.loadImage('Toad.png')
        # https://imgs.search.brave.com/TBHPvP0qhkqEoVSJTEpO5Q7orWV5B78htvsySvDdjAo/rs:fit:428:225:1/g:ce/aHR0cHM6Ly90c2Uy/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5l/Rmhvb1NROUh4ak1a/ZHZNZnVVN0xBSGFJ/TSZwaWQ9QXBp
    app.toad = app.scaleImage(app.toadImage, 1/10)
    app.karts['toad'] = app.toad
    app.yoshiImage = app.loadImage('Yoshi.png')
        # https://imgs.search.brave.com/Vqxs2jbvIw4zQ10dDz37_CKGcNd0gxpCL49w3ddJ_Nk/rs:fit:449:225:1/g:ce/aHR0cHM6Ly90c2U0/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5F/aGhieERFamFsS2lt/c0kzOXdTdzB3SGFI/MCZwaWQ9QXBp
    app.yoshi = app.scaleImage(app.yoshiImage, 1/10)
    app.karts['yoshi'] = app.yoshi
    app.dkImage = app.loadImage('Donkey Kong.png')
        # https://www.google.com/imgres?imgurl=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FI%2F71lO1%2BX8cSS.jpg&imgrefurl=https%3A%2F%2Fwww.amazon.com%2FHallmark-Keepsake-Christmas-Ornament-Nintendo%2Fdp%2FB0915R1DVF&tbnid=87liFywnBGK46M&vet=12ahUKEwiWmKPLn9_7AhWQvHIEHdJ9B44QMygBegUIARDvAQ..i&docid=NADVkGzdvSUxaM&w=2560&h=2560&q=mario%20kart%20donkey%20kong&client=opera-gx&ved=2ahUKEwiWmKPLn9_7AhWQvHIEHdJ9B44QMygBegUIARDvAQ
    app.dk = app.scaleImage(app.dkImage, 1/10)
    app.karts['donkeykong'] = app.dk
    app.warioImage = app.loadImage('Wario.png')
        # https://imgs.search.brave.com/MAUmI2T8BYNLlcNZGSJX9nultWDlNBGvVyuvoGtKRxA/rs:fit:397:225:1/g:ce/aHR0cHM6Ly90c2Uz/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC50/LUxVc0xhbGthMG5F/VE1RZEloVjJRSGFJ/MSZwaWQ9QXBp
    app.wario = app.scaleImage(app.warioImage, 1/10)
    app.karts['wario'] = app.wario
    app.bowserImage = app.loadImage('Bowser.png')
        # https://imgs.search.brave.com/peQRweN8h1h7ZVkSf8FGRZ29aowxw-LhFTpje0jyZLg/rs:fit:413:225:1/g:ce/aHR0cHM6Ly90c2Uz/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5j/ZU5DRG5VY2VpZldT/X0xhelVHc2hRSGFJ/ZyZwaWQ9QXBp
    app.bowser = app.scaleImage(app.bowserImage, 1/10)
    app.karts['bowser'] = app.bowser

    # Pause menu
    app.pauseImage = app.loadImage('Pause.jpg')
        # https://imgs.search.brave.com/dTHPCpFJ02O8p0vCcew3ZdPSMy-o8lxyox4b9j1rDdY/rs:fit:759:225:1/g:ce/aHR0cHM6Ly90c2Uy/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5O/WHl5OHlreGF1T203/YVdaQ0dpbm13SGFF/byZwaWQ9QXBp
    app.pause = app.scaleImage(app.pauseImage, 1/2)

    # Finish line
    app.finishline = [[1, 0],
                      [0, 1],
                      [1, 0],
                      [0, 1],
                      [1, 0],
                      [0, 1],
                      [1, 0],
                      [0, 1]]

    # Game over menu
    app.allTimeScores = ast.literal_eval(readFile('myData.txt'))
    app.congratsImage = app.loadImage('Game Over.png')
        # https://imgs.search.brave.com/AXE5RF5e2zfd52Bvx-QFWkG_oWmT17sHhRJBKvktLjY/rs:fit:1200:1080:1/g:ce/aHR0cHM6Ly9pbWFn/ZXMubGF1bmNoYm94/LWFwcC5jb20vNmZm/OWVjNGYtN2I1Yy00/NWMwLTlmZjMtZjgw/MWJjMzI1MGNhLnBu/Zw
    _ , congratsHeight = app.congratsImage.size
    app.congrats = app.scaleImage(app.congratsImage, app.height/congratsHeight)

# Menu credit: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes

######################################
# Start Menu
######################################

def startMenu_redrawAll(app, canvas):
    # Create background
    canvas.create_rectangle(0, 0, app.width, app.height, fill='navy')
    canvas.create_image(app.cx, app.cy, 
                        image=ImageTk.PhotoImage(app.scaledStartMenu))
    canvas.create_image(app.cx, 100,
                        image=ImageTk.PhotoImage(app.marioKart112))
    canvas.create_text(app.cx, 200, text="Press any key to continue",
                       font="impact 40 bold", fill='white')

def startMenu_keyPressed(app, event):
    if event.key != 'Escape':
        app.mode = 'mapSelect'
    else:
        quit()

######################################
# Map Select Menu
######################################

def mapSelect_redrawAll(app, canvas):
    # Draw the buttons for each map
    canvas.create_rectangle(0, 0, app.width, app.height, fill='dodgerblue')
    canvas.create_image(app.width*1/6, app.cy,
                        image=ImageTk.PhotoImage(app.mushroomCup))
    canvas.create_text(app.width*1/6, app.height*5/6, text='Mushroom Cup',
                       font='helvetica 27 bold', fill='navy blue')
    canvas.create_image(app.cx, app.cy,
                        image=ImageTk.PhotoImage(app.starCup))
    canvas.create_text(app.cx, app.height*5/6, text='Star Cup',
                       font='helvetica 27 bold', fill='navy blue')
    canvas.create_image(app.width*5/6, app.cy,
                        image=ImageTk.PhotoImage(app.specialCup))
    canvas.create_text(app.width*5/6, app.height*5/6, text='Special Cup',
                       font='helvetica 27 bold', fill='navy blue')
    canvas.create_text(app.cx, 100, text='Click on the icon to select the map!',
                       font='Impact 30', fill='yellow')
    canvas.create_text(10, 10, text='<< Esc to go back', fill='black',
                       font='impact 20', anchor='nw')
    canvas.create_text(app.width-10, 10, text='Press H for Help! >>', fill='black',
                       font='impact 20', anchor='ne')

def mapSelect_mousePressed(app, event):
    # Create buttons for each map
    cupWidth, _ = app.mushroomCup.size
    imageRadius = cupWidth/2
    if event.x >= app.width*1/6 - imageRadius and event.x <= app.width*1/6 + imageRadius:
        if event.y >= app.cy - imageRadius and event.y <= app.cy + imageRadius:
            app.mode = 'mushroomCup'
            app.mapForScore = 'map1'
    elif event.x >= app.cx - imageRadius and event.x <= app.cx + imageRadius:
        if event.y >= app.cy - imageRadius and event.y <= app.cy + imageRadius:
            app.mode = 'starCup'
            app.mapForScore = 'map2'
    elif event.x >= app.width*5/6 - imageRadius and event.x <= app.width*5/6 + imageRadius:
        if event.y >= app.cy - imageRadius and event.y <= app.cy + imageRadius:
            app.mode = 'specialCup'
            app.mapForScore = 'map3'

def mapSelect_keyPressed(app, event):
    # Escape to go back
    if event.key == 'Escape':
        app.mode = 'startMenu'
        app.mapForScore = ''
    elif event.key == 'h':
        app.mode = 'help'

######################################
# Help Menu
######################################

def help_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='orange')
    canvas.create_text(app.cx, app.cy,
                       text='''
1. Press S to move backwards
2. Press the Left/Right arrow keys to turn
3. Press Space to use an item
4. Press P to pause
5. Press on your nose for good luck!
                       ''', font = 'Roboto 50 bold', fill='maroon')
    canvas.create_text(10, 10, text='<< Esc to go back', fill='black',
                       font='impact 20 bold', anchor='nw')

def help_keyPressed(app, event):
    if event.key == 'Escape':
        app.mode = 'mapSelect'

######################################
# Mushroom Cup Menu
######################################

def mushroomCup_redrawAll(app, canvas):
    # Draw the character select options
    margin = 45//2
    for x in range(margin, app.width, 45):
        for y in range(margin, app.height, 45):
            canvas.create_image(x, y, 
                                image=ImageTk.PhotoImage(app.singleMushroom))
    canvas.create_image(app.cx, app.cy,
                        image=ImageTk.PhotoImage(app.characters))

def mushroomCup_keyPressed(app, event):
    # Escape to go back
    if event.key == 'Escape':
        app.mode = 'mapSelect'

def mushroomCup_mousePressed(app, event):
    # Create buttons for each character
    charWidth, charHeight = app.characters.size
    margin = 13
    x0 = (app.width - charWidth)*1/2 + margin
    y0 = (app.height - charHeight)*1/2 + margin
    charCellX = (charWidth - margin*5)/4
    charCellY = (charHeight - margin*3)/2

    if event.x >= x0 and event.x <= x0 + charCellX:
        if event.y >= y0 and event.y <= y0 + charCellY:
            app.selectedCharacter = 'mario'
            app.selectedMap = app.map1
            app.itemMap = app.itembox1
            app.mode = 'raceMode'
        elif event.y >= y0+charCellY+margin and event.y <= y0+2*charCellY+margin:
            app.selectedCharacter = 'yoshi'
            app.selectedMap = app.map1
            app.itemMap = app.itembox1
            app.mode = 'raceMode'
    elif event.x >= x0+charCellX+margin and event.x <= x0+2*charCellX+margin:
        if event.y >= y0 and event.y <= y0 + charCellY:
            app.selectedCharacter = 'luigi'
            app.selectedMap = app.map1
            app.itemMap = app.itembox1
            app.mode = 'raceMode'
        elif event.y >= y0+charCellY+margin and event.y <= y0+2*charCellY+margin:
            app.selectedCharacter = 'donkeykong'
            app.selectedMap = app.map1
            app.itemMap = app.itembox1
            app.mode = 'raceMode'
    elif event.x >= x0+2*charCellX+2*margin and event.x <= x0+3*charCellX+2*margin:
        if event.y >= y0 and event.y <= y0 + charCellY:
            app.selectedCharacter = 'peach'
            app.selectedMap = app.map1
            app.itemMap = app.itembox1
            app.mode = 'raceMode'
        elif event.y >= y0+charCellY+margin and event.y <= y0+2*charCellY+margin:
            app.selectedCharacter = 'wario'
            app.selectedMap = app.map1
            app.itemMap = app.itembox1
            app.mode = 'raceMode'
    elif event.x >= x0+3*charCellX+3*margin and event.x <= x0+4*charCellX+3*margin:
        if event.y >= y0 and event.y <= y0 + charCellY:
            app.selectedCharacter = 'toad'
            app.selectedMap = app.map1
            app.itemMap = app.itembox1
            app.mode = 'raceMode'
        elif event.y >= y0+charCellY+margin and event.y <= y0+2*charCellY+margin:
            app.selectedCharacter = 'bowser'
            app.selectedMap = app.map1
            app.itemMap = app.itembox1
            app.mode = 'raceMode'

def starCup_redrawAll(app, canvas):
    margin = 45//2
    for x in range(margin, app.width, 45):
        for y in range(margin, app.height, 45):
            canvas.create_image(x, y, 
                                image=ImageTk.PhotoImage(app.singleStar))
    canvas.create_image(app.cx, app.cy,
                        image=ImageTk.PhotoImage(app.characters))

def starCup_keyPressed(app, event):
    if event.key == 'Escape':
        app.mode = 'mapSelect'

def starCup_mousePressed(app, event):
    charWidth, charHeight = app.characters.size
    margin = 13
    x0 = (app.width - charWidth)*1/2 + margin
    y0 = (app.height - charHeight)*1/2 + margin
    charCellX = (charWidth - margin*5)/4
    charCellY = (charHeight - margin*3)/2
    
    if event.x >= x0 and event.x <= x0 + charCellX:
        if event.y >= y0 and event.y <= y0 + charCellY:
            app.selectedCharacter = 'mario'
            app.selectedMap = app.map2
            app.itemMap = app.itembox2
            app.mode = 'raceMode'
        elif event.y >= y0+charCellY+margin and event.y <= y0+2*charCellY+margin:
            app.selectedCharacter = 'yoshi'
            app.selectedMap = app.map2
            app.itemMap = app.itembox2
            app.mode = 'raceMode'
    elif event.x >= x0+charCellX+margin and event.x <= x0+2*charCellX+margin:
        if event.y >= y0 and event.y <= y0 + charCellY:
            app.selectedCharacter = 'luigi'
            app.selectedMap = app.map2
            app.itemMap = app.itembox2
            app.mode = 'raceMode'
        elif event.y >= y0+charCellY+margin and event.y <= y0+2*charCellY+margin:
            app.selectedCharacter = 'donkeykong'
            app.selectedMap = app.map2
            app.itemMap = app.itembox2
            app.mode = 'raceMode'
    elif event.x >= x0+2*charCellX+2*margin and event.x <= x0+3*charCellX+2*margin:
        if event.y >= y0 and event.y <= y0 + charCellY:
            app.selectedCharacter = 'peach'
            app.selectedMap = app.map2
            app.itemMap = app.itembox2
            app.mode = 'raceMode'
        elif event.y >= y0+charCellY+margin and event.y <= y0+2*charCellY+margin:
            app.selectedCharacter = 'wario'
            app.selectedMap = app.map2
            app.itemMap = app.itembox2
            app.mode = 'raceMode'
    elif event.x >= x0+3*charCellX+3*margin and event.x <= x0+4*charCellX+3*margin:
        if event.y >= y0 and event.y <= y0 + charCellY:
            app.selectedCharacter = 'toad'
            app.selectedMap = app.map2
            app.itemMap = app.itembox2
            app.mode = 'raceMode'
        elif event.y >= y0+charCellY+margin and event.y <= y0+2*charCellY+margin:
            app.selectedCharacter = 'bowser'
            app.selectedMap = app.map2
            app.itemMap = app.itembox2
            app.mode = 'raceMode'

def specialCup_redrawAll(app, canvas):
    margin = 45//2
    for x in range(margin, app.width, 45):
        for y in range(margin, app.height, 45):
            canvas.create_image(x, y, 
                                image=ImageTk.PhotoImage(app.singleCrown))
    canvas.create_image(app.cx, app.cy,
                        image=ImageTk.PhotoImage(app.characters))

def specialCup_keyPressed(app, event):
    if event.key == 'Escape':
        app.mode = 'mapSelect'

def specialCup_mousePressed(app, event):
    charWidth, charHeight = app.characters.size
    margin = 13
    x0 = (app.width - charWidth)*1/2 + margin
    y0 = (app.height - charHeight)*1/2 + margin
    charCellX = (charWidth - margin*5)/4
    charCellY = (charHeight - margin*3)/2
    
    if event.x >= x0 and event.x <= x0 + charCellX:
        if event.y >= y0 and event.y <= y0 + charCellY:
            app.selectedCharacter = 'mario'
            app.selectedMap = app.map3
            app.itemMap = app.itembox3
            app.mode = 'raceMode'
        elif event.y >= y0+charCellY+margin and event.y <= y0+2*charCellY+margin:
            app.selectedCharacter = 'yoshi'
            app.selectedMap = app.map3
            app.itemMap = app.itembox3
            app.mode = 'raceMode'
    elif event.x >= x0+charCellX+margin and event.x <= x0+2*charCellX+margin:
        if event.y >= y0 and event.y <= y0 + charCellY:
            app.selectedCharacter = 'luigi'
            app.selectedMap = app.map3
            app.itemMap = app.itembox3
            app.mode = 'raceMode'
        elif event.y >= y0+charCellY+margin and event.y <= y0+2*charCellY+margin:
            app.selectedCharacter = 'donkeykong'
            app.selectedMap = app.map3
            app.itemMap = app.itembox3
            app.mode = 'raceMode'
    elif event.x >= x0+2*charCellX+2*margin and event.x <= x0+3*charCellX+2*margin:
        if event.y >= y0 and event.y <= y0 + charCellY:
            app.selectedCharacter = 'peach'
            app.selectedMap = app.map3
            app.itemMap = app.itembox3
            app.mode = 'raceMode'
        elif event.y >= y0+charCellY+margin and event.y <= y0+2*charCellY+margin:
            app.selectedCharacter = 'wario'
            app.selectedMap = app.map3
            app.itemMap = app.itembox3
            app.mode = 'raceMode'
    elif event.x >= x0+3*charCellX+3*margin and event.x <= x0+4*charCellX+3*margin:
        if event.y >= y0 and event.y <= y0 + charCellY:
            app.selectedCharacter = 'toad'
            app.selectedMap = app.map3
            app.itemMap = app.itembox3
            app.mode = 'raceMode'
        elif event.y >= y0+charCellY+margin and event.y <= y0+2*charCellY+margin:
            app.selectedCharacter = 'bowser'
            app.selectedMap = app.map3
            app.itemMap = app.itembox3
            app.mode = 'raceMode'

######################################
# Raycasting
######################################

def almostEqual(d1, d2, epsilon=10**-7):
    return (abs(d2 - d1) < epsilon)
    # Credit: HW 1

def roundHalfUp(d):
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))
    # Credit: HW 1

def drawBackground(app, canvas):
    # draw the sky and road
    canvas.create_rectangle(0, 0, app.width, app.height/2,
                            fill='sky blue',width=0)
    canvas.create_rectangle(0, app.height/2, app.width, app.height,
                            fill='brown', width=0)

def drawPlayer(app, canvas):
    # draw the selected character on the 2D track
    kart = app.karts[app.selectedCharacter]
    canvas.create_image(app.px, app.py, 
                        image=ImageTk.PhotoImage(kart))

def drawGrid(app, cellWidth, map, canvas):
    # draw the 2D track
    for row in range(len(map)):
        for col in range(len(map[0])):
            canvas.create_rectangle(cellWidth * col, cellWidth * row,
                                        cellWidth * (col+1), cellWidth*(row+1),
                                        fill='dark gray', width=0)
            if map[row][col] == 1:
                canvas.create_rectangle(cellWidth * col, cellWidth * row,
                                        cellWidth * (col+1), cellWidth*(row+1),
                                        fill='white', width=0)

    # draw finish line
    rows = len(app.finishline)
    cols = len(app.finishline[0])
    for row in range(rows):
        for col in range(cols):
            if map == app.map1 or map == app.map2:
                if app.finishline[row][col] == 1:
                    canvas.create_rectangle(cellWidth*(2 + (col-1)/rows),
                                            cellWidth*2/rows*row,
                                            cellWidth*(2 + col/rows),
                                            cellWidth*2/rows*(row+1),
                                            fill='white')
                elif app.finishline[row][col] == 0:
                    canvas.create_rectangle(cellWidth*(2 + (col-1)/rows),
                                            cellWidth*2/rows*row,
                                            cellWidth*(2 + col/rows),
                                            cellWidth*2/rows*(row+1),
                                            fill='black')
            else:
                if app.finishline[row][col] == 1:
                    canvas.create_rectangle(cellWidth*(1 + (col-1)/rows),
                                            cellWidth/rows*row,
                                            cellWidth*(1 + col/rows),
                                            cellWidth/rows*(row+1),
                                            fill='white')
                elif app.finishline[row][col] == 0:
                    canvas.create_rectangle(cellWidth*(1 + (col-1)/rows),
                                            cellWidth/rows*row,
                                            cellWidth*(1 + col/rows),
                                            cellWidth/rows*(row+1),
                                            fill='black')

# Raycasting credit: https://www.youtube.com/watch?v=gYRrGTC7GtA

def rayDist(cx, cy, rx, ry):
    # Pythagorean Theorem Distance Formula (HW 1)
    return math.sqrt((rx-cx)**2 + (ry-cy)**2)

def getHorizontalRayEnd(app, angle, px, py, map):
    # Keep extending by one horizontal gridline until the ray reaches a wall
    dof = 0
    maxDof = len(map)
    rx, ry = px, py

    # Looking left or right
    if almostEqual(angle, 0, 10**-3) or almostEqual(angle, math.pi, 10**-3):
        dof = maxDof
    else:
        aTan = -1/math.tan(angle)

        # Looking up
        if angle < math.pi:
            ry = roundHalfUp(py//app.cellWidth)*app.cellWidth
            rx = px + (ry-py)*aTan
            dy = -1*app.cellWidth
            dx = dy*aTan

            # Find ray endpoint
            while dof < maxDof:
                my = roundHalfUp(ry//app.cellWidth-1)
                mx = roundHalfUp(rx//app.cellWidth)
                if mx < len(map[0]) and mx >= 0:
                    if my >= 0 and my < len(map):
                        if map[my][mx] == 1:
                            dof = maxDof
                        else:
                            rx += dx
                            ry += dy
                dof += 1

        # Looking down
        elif angle > math.pi:
            ry = roundHalfUp(py//app.cellWidth)*app.cellWidth + app.cellWidth
            rx = px + (ry-py)*aTan
            dy = app.cellWidth
            dx = dy*aTan

            # Find ray endpoint
            while dof < maxDof:
                my = roundHalfUp(ry//app.cellWidth)
                mx = roundHalfUp(rx//app.cellWidth)
                if mx < len(map[0]) and mx >= 0:
                    if my >= 0 and my < len(map):
                        if map[my][mx] == 1:
                            dof = maxDof
                        else:
                            rx += dx
                            ry += dy
                dof += 1
    return rx, ry

def getVerticalRayEnd(app, angle, px, py, map):
    # Keep extending by one vertical gridline until the ray reaches a wall
    dof = 0
    maxDof = len(map)
    rx, ry = px, py

    # Looking up or down
    if almostEqual(angle, math.pi/2, 10**-3) or almostEqual(angle, math.pi*1.5, 10**-3):
        rx = px
        ry = py
        dof = maxDof
    else:
        nTan = -1*math.tan(angle)

        # Looking left
        if angle > math.pi/2 and angle < math.pi*1.5:
            rx = (px//app.cellWidth)*app.cellWidth
            ry = py + (rx-px)*nTan
            dx = -1*app.cellWidth
            dy = dx*nTan
            
            # Find ray endpoint
            while dof < maxDof:
                mx = roundHalfUp(rx//app.cellWidth-1)
                my = roundHalfUp(ry//app.cellWidth)
                if mx < len(map[0]) and mx >= 0:
                    if my >= 0 and my < len(map):
                        if map[my][mx] == 1:
                            dof = maxDof
                        else:
                            rx += dx
                            ry += dy
                dof += 1

        # Looking right
        elif angle < math.pi/2 or angle > math.pi*1.5:
            rx = (px//app.cellWidth)*app.cellWidth + app.cellWidth
            ry = py + (rx-px)*nTan
            dx = app.cellWidth
            dy = dx*nTan

            # Find ray endpoint
            while dof < maxDof:
                mx = roundHalfUp(rx//app.cellWidth)
                my = roundHalfUp(ry//app.cellWidth)
                if mx < len(map[0]) and mx >= 0:
                    if my >= 0 and my < len(map):
                        if map[my][mx] == 1:
                            dof = maxDof
                        else:
                            rx += dx
                            ry += dy
                dof += 1
    return rx, ry

def draw3D(app, canvas, numDeg):

    ##############################
    # Raycasting
    ##############################
    
    distFinal = 0
    visible, visibleBanana, visibleFake = (0, 0), (0, 0), (0, 0)
    spriteDist, bananaDist, fakeDist = 0, 0, 0
    spriteScale, bananaScale, fakeScale = 0, 0, 0

    for x in range(numDeg+1):
        # Get the angle
        angleDiff = 0.01745329/3*(-1*numDeg/2 + x)
        angle = (app.angle + angleDiff) % (math.pi*2)

        # Get the ray endpoints
        hx, hy = getHorizontalRayEnd(app, angle, app.px, app.py, app.selectedMap)
        vx, vy = getVerticalRayEnd(app, angle, app.px, app.py, app.selectedMap)
        distH = rayDist(app.px, app.py, hx, hy)
        distV = rayDist(app.px, app.py, vx, vy)

        # Find the ray with the shortest distance and set it equal to distFinal
        if distH == 0:
            distFinal = distV
        elif distV == 0:
            distFinal = distH
        elif distV < distH:
            distFinal = distV
        elif distH < distV:
            distFinal = distH

        # multiply by cos(angleDiff) to remove fish-eye effect
        distFinalcos = distFinal * math.cos(angleDiff)

        # 3D line height formula
        lineHeight = app.cellWidth*app.height/distFinalcos
        if lineHeight > app.height:
            lineHeight = app.height

        # 3D line coordinate + offset from top of screen
        xCoord = app.width - (app.width - app.cellWidth*len(app.map1))/numDeg*x
        lineOffset = app.height/2-lineHeight/2

        # draw the rays
        if distH == 0:
            canvas.create_line(xCoord, lineOffset, xCoord, lineOffset+lineHeight,
                           width=app.width/numDeg, fill='lime')
        elif distV == 0:
            canvas.create_line(xCoord, lineOffset, xCoord, lineOffset+lineHeight,
                           width=app.width/numDeg, fill='green')
        elif distV < distH:
            canvas.create_line(xCoord, lineOffset, xCoord, lineOffset+lineHeight,
                           width=app.width/numDeg, fill='lime')
        elif distH < distV:
            canvas.create_line(xCoord, lineOffset, xCoord, lineOffset+lineHeight,
                           width=app.width/numDeg, fill='green')

    ##############################
    # Sprite-casting
    ##############################

    # Sprite-casting credit: https://wynnliam.github.io/raycaster/news/tutorial/2019/04/03/raycaster-part-02.html

        for itembox in app.itemMap:
            spriteDist = rayDist(app.px, app.py, itembox[0], itembox[1])

            dx = itembox[0] - app.px
            dy = itembox[1] - app.py

            p = math.atan2(-1*dy, dx) % (math.pi*2)

            if spriteDist < distFinal and almostEqual(angle, p, math.pi/6):
                visible = itembox
                spriteScale = 266/spriteDist
                break
        
        for banana in app.bananaCoords:
            bananaDist = rayDist(app.px, app.py, banana[0], banana[1])

            bdx = banana[0] - app.px
            bdy = banana[1] - app.py

            bp = math.atan2(-1*bdy, bdx) % (math.pi*2)

            if bananaDist < distFinal and almostEqual(angle, bp, math.pi/6):
                if bananaDist > 0:
                    visibleBanana = banana
                    bananaScale = 200/bananaDist
                    break

        for fake in app.fakeitemboxCoords:
            fakeDist = rayDist(app.px, app.py, fake[0], fake[1])

            fdx = fake[0] - app.px
            fdy = fake[1] - app.py

            fp = math.atan2(-1*fdy, fdx) % (math.pi*2)

            if fakeDist < distFinal and almostEqual(angle, fp, math.pi/6):
                if fakeDist > 0:
                    visibleFake = fake
                    fakeScale = 230/fakeDist
                    break

    distx = visible[0] - app.px
    disty = visible[1] - app.py
    bananaDx = visibleBanana[0] - app.px
    bananaDy = visibleBanana[1] - app.py
    fakeDx = visibleFake[0] - app.px
    fakeDy = visibleFake[1] - app.py

    p = math.atan2(-1*disty, distx) % (math.pi*2)
    q = app.angle + math.pi/6 - p
    bp = math.atan2(-1*bananaDy, bananaDx) % (math.pi*2)
    bq = app.angle + math.pi/6 - bp
    fp = math.atan2(-1*fakeDy, fakeDx) % (math.pi*2)
    fq = app.angle + math.pi/6 - fp

    if app.angle >= 0 and app.angle <= math.pi/2:
        if p >= math.pi*1.5 and p <= math.pi*2:
            q += math.pi*2
        if bp >= math.pi*1.5 and bp <= math.pi*2:
            bq += math.pi*2
        if fp >= math.pi*1.5 and fp <= math.pi*2:
            fq += math.pi*2
    elif app.angle >= math.pi*1.5 and app.angle <= math.pi*2:
        if p >= 0 and p <= math.pi/2:
            q -= math.pi*2
        if bp >= 0 and bp <= math.pi/2:
            bq -= math.pi*2
        if fp >= 0 and fp <= math.pi/2:
            fq -= math.pi*2
        

    spriteX = q * ((app.width-app.height) / (math.pi/3)) + app.height
    bananaX = bq * ((app.width-app.height) / (math.pi/3)) + app.height
    fakeX = fq * ((app.width-app.height) / (math.pi/3)) + app.height

    if spriteScale < app.height/64*3/4 and spriteScale > 0:
        itemboxImg = app.scaleImage(app.itemboxUnscaled, spriteScale)
        canvas.create_image(spriteX, app.cy + 50, 
                            image=ImageTk.PhotoImage(itemboxImg))
    if bananaScale < app.height/60*3/4 and bananaScale > 0:
        bananaImg = app.scaleImage(app.banana, bananaScale)
        canvas.create_image(bananaX, app.cy + 60, 
                            image=ImageTk.PhotoImage(bananaImg))
    if fakeScale < app.height/60*3/4 and fakeScale > 0:
        fakeImg = app.scaleImage(app.fakeItemBox, fakeScale)
        canvas.create_image(fakeX, app.cy + 50, 
                            image=ImageTk.PhotoImage(fakeImg))

######################################
# Lap Properties
######################################

def checkPoint(app, px, py):
    left = app.cellWidth*(len(app.map1)-3)
    right = app.cellWidth*len(app.map1)
    if px > left and px < right:
        if py > left and py < app.height:
            app.checkpoint = True

def isLap(app, px, py):
    # Check if the kart passed the checkpoint
    if app.checkpoint:
    # Check if the kart isn't moving backwards
        if app.angle <= math.pi/2 or app.angle >= math.pi*1.5:
            # Check if kart is on the finish line (map-dependent)
            if app.selectedMap == app.map1 or app.selectedMap == app.map2:
                left = app.cellWidth*(2 - 1/len(app.finishline))
                right = app.cellWidth*(2 + 1/len(app.finishline))
                if px > left and px < right:
                    if py > 0 and py < app.cellWidth*2:
                        app.checkpoint = False
                        return True
            else:
                left = app.cellWidth*(1 - 1/len(app.finishline))
                right = app.cellWidth*(1 + 1/len(app.finishline))
                if px > left and px < right:
                    if py > 0 and py < app.cellWidth:
                        app.checkpoint - False
                        return True
        return False

def changeLap(app):
    # if the kart is on the line and it wasn't immediately before, lap += 1
    if isLap(app, app.px, app.py) and not app.temp:
        app.temp = True
        app.lap += 1

    # if the kart is still on the line, lap shouldn't increment by 1
    elif not isLap(app, app.px, app.py):
        app.temp = False

def drawStats(app, canvas):
    canvas.create_oval((app.width+app.cellWidth*len(app.map1))/2-100, 
                            app.height * 1/10,
                            (app.width+app.cellWidth*len(app.map1))/2+100,
                            app.height * 1/5, fill = 'dodgerblue', width=3)
    canvas.create_text((app.width+app.cellWidth*len(app.map1))/2, 
                       app.height * 3/20, text=f'Lap: {app.lap}/3',
                       font='Roboto 20 bold', fill='black')

def hitItemBox(app, px, py):
    for item in app.itemMap:
        if px >= item[0] - app.cellWidth/3 - 20 and px <= item[0] + app.cellWidth/3:
            if py >= item[1] - app.cellWidth/3 and py <= item[1] + app.cellWidth/3:
                return True
    return False

def getItem(app):
    if hitItemBox(app, app.px, app.py) and not app.itemsTemp:
        app.itemsTemp = True
        index = random.randint(0, len(app.items) - 1)
        app.currentItem = app.items[index]
    elif not hitItemBox(app, app.px, app.py):
        app.itemsTemp = False

def drawItem(app, canvas):
    margin = 20
    itemFrameWidth = 64
    left = app.height + margin
    right = app.height + margin + itemFrameWidth
    top = margin
    bottom = margin + itemFrameWidth
    canvas.create_rectangle(left, top, right, bottom, fill='black',
                            outline = 'white', width=4)
    
    if len(app.currentItem) != 0:
        if app.currentItem == 'mushroom':
            canvas.create_image(app.height+margin+itemFrameWidth/2, margin+itemFrameWidth/2,
                                image=ImageTk.PhotoImage(app.mushroom))
        elif app.currentItem == 'banana':
            canvas.create_image(app.height+margin+itemFrameWidth/2, margin+itemFrameWidth/2,
                                image=ImageTk.PhotoImage(app.banana))
        elif app.currentItem == 'golden mushroom':
            canvas.create_image(app.height+margin+itemFrameWidth/2, margin+itemFrameWidth/2,
                                image=ImageTk.PhotoImage(app.goldenMushroom))
        elif app.currentItem == 'fake-itembox':
            canvas.create_image(app.height+margin+itemFrameWidth/2, margin+itemFrameWidth/2,
                                image=ImageTk.PhotoImage(app.fakeItemBox))

def itemCollision(app, px, py):
    bananaRadius = 4
    fakeRadius = 5
    for banana in app.bananaCoords:
        if px >= banana[0] - bananaRadius and px <= banana[0] + bananaRadius:
            if py >= banana[1] - bananaRadius and py <= banana[1] + bananaRadius:
                app.collision = True
                app.bananaCoords.remove(banana)
    for fake in app.fakeitemboxCoords:
        if px >= fake[0] - fakeRadius and px <= fake[0] + fakeRadius:
            if py >= fake[1] - fakeRadius and py <= fake[1] + fakeRadius:
                app.collision = True
                app.fakeitemboxCoords.remove(fake)

######################################
# raceMode
######################################

def raceMode_keyPressed(app, event):

    # Speed x and y components
    dy = app.speed*math.sin(app.angle)
    dx = app.speed*math.cos(app.angle)

    # Move backwards
    if event.key == 's':
        tempCx = app.px - app.playerHitbox*math.cos(app.angle)
        tempCy = app.py + app.playerHitbox*math.sin(app.angle)
        tempMy = roundHalfUp((tempCy)//app.cellWidth)
        tempMx = roundHalfUp((tempCx)//app.cellWidth)
        if tempCx > 0 and tempCx < app.cellWidth*len(app.selectedMap):
            if tempCy > 0 and tempCy < app.height:
                if app.selectedMap[tempMy][tempMx] == 0:
                    app.py += dy
                    app.px -= dx

    # Pan Left and Right
    elif event.key == 'Left':

        # Slow down forward speed when turning
        app.speed = app.playerRadius * 0.5
        raceMode_timerFired(app)

        if app.angle + 0.05 >= 2*math.pi:
            app.angle -= 2*math.pi
        app.angle += 0.05
    elif event.key == 'Right':
        app.speed = app.playerRadius * 0.5
        raceMode_timerFired(app)
        if app.angle - 0.05 < 0:
            app.angle += 2*math.pi
        app.angle -= 0.05

    # Pause
    elif event.key == 'p':
        app.mode = 'pause'
    
    # Use item
    elif event.key == 'Space':
        if app.currentItem == 'mushroom':
            app.speedboost = True
        elif app.currentItem == 'banana':
            app.currentItem = ''
            bx = app.px-app.playerHitbox*math.cos(app.angle)
            by = app.py+app.playerHitbox*math.sin(app.angle)
            app.bananaCoords.append((bx, by))
        elif app.currentItem == 'golden mushroom':
            app.speedboost = True
        elif app.currentItem == 'fake-itembox':
            app.currentItem = ''
            fx = app.px-app.playerHitbox*math.cos(app.angle)
            fy = app.py+app.playerHitbox*math.sin(app.angle)
            app.fakeitemboxCoords.append((fx, fy))
    
    # Reset speed to normal after turning
    app.speed = app.playerRadius

def raceMode_timerFired(app):
    app.totalTime += 1
    app.totalTimePassed = app.totalTime // (1000/app.timerDelay)

    app.frames += 1
    if not app.speedboost and not app.collision:
        app.frames -= 1
    app.timePassed = app.frames // (1000/app.timerDelay)
    if app.timePassed >= 2 and app.currentItem == 'mushroom':
        app.speedboost = False
        app.frames = 0
        app.currentItem = ''
    elif app.timePassed >= 1 and app.collision:
        app.collision = False
        app.frames = 0
    elif app.timePassed >= 8 and app.currentItem == 'golden mushroom':
        app.speedboost = False
        app.frames = 0
        app.currentItem = ''

    # Keep track of laps
    checkPoint(app, app.px, app.py)
    changeLap(app)
    gameOver(app)

    # Keep track of items and collisions
    getItem(app)
    itemCollision(app, app.px, app.py)

    # Move forwards constantly
    if app.speedboost:
        dy = app.speed*3*math.sin(app.angle)
        dx = app.speed*3*math.cos(app.angle)
        tempCx = app.px + app.playerHitbox*math.cos(app.angle)
        tempCy = app.py - app.playerHitbox*math.sin(app.angle)
        tempMy = roundHalfUp((tempCy)//app.cellWidth)
        tempMx = roundHalfUp((tempCx)//app.cellWidth)
        if tempCx > 0 and tempCx < app.cellWidth*len(app.selectedMap):
            if tempCy > 0 and tempCy < app.cellWidth*len(app.selectedMap):
                if app.selectedMap[tempMy][tempMx] == 0:
                    app.py -= dy
                    app.px += dx
    elif app.collision:
        dy = app.speed*0.3*math.sin(app.angle)
        dx = app.speed*0.3*math.cos(app.angle)
        tempCx = app.px + app.playerHitbox*math.cos(app.angle)
        tempCy = app.py - app.playerHitbox*math.sin(app.angle)
        tempMy = roundHalfUp((tempCy)//app.cellWidth)
        tempMx = roundHalfUp((tempCx)//app.cellWidth)
        if tempCx > 0 and tempCx < app.cellWidth*len(app.selectedMap):
            if tempCy > 0 and tempCy < app.cellWidth*len(app.selectedMap):
                if app.selectedMap[tempMy][tempMx] == 0:
                    app.py -= dy
                    app.px += dx
    else:
        dy = app.speed*math.sin(app.angle)
        dx = app.speed*math.cos(app.angle)
        tempCx = app.px + app.playerHitbox*math.cos(app.angle)
        tempCy = app.py - app.playerHitbox*math.sin(app.angle)
        tempMy = roundHalfUp((tempCy)//app.cellWidth)
        tempMx = roundHalfUp((tempCx)//app.cellWidth)
        if tempCx > 0 and tempCx < app.cellWidth*len(app.selectedMap):
            if tempCy > 0 and tempCy < app.cellWidth*len(app.selectedMap):
                if app.selectedMap[tempMy][tempMx] == 0:
                    app.py -= dy
                    app.px += dx

def raceMode_redrawAll(app, canvas):
    drawBackground(app, canvas)
    draw3D(app, canvas, 180)
    drawItem(app, canvas)
    drawStats(app, canvas)
    drawGrid(app, app.cellWidth, app.selectedMap, canvas)
    drawPlayer(app, canvas)

######################################
# Pause Menu
######################################

def pause_redrawAll(app, canvas):
    # Draw pause menu screen
    canvas.create_rectangle(0, 0, app.width, app.height, fill='black')
    canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(app.pause))
    # Remove watermark
    canvas.create_rectangle(280, 470, 670, app.height, fill='black')
    # Draw text (instructions)
    canvas.create_text(app.cx, app.cy-120, text='Press P again to unpause',
                       font='Impact 40 bold', fill='navy')
    canvas.create_text(app.cx, app.cy-40, text='Press Esc to quit',
                       font='Impact 40 bold', fill='navy')

def pause_keyPressed(app, event):
    if event.key == 'p':
        app.mode = 'raceMode'
    elif event.key == 'Escape':
        app.mode = 'startMenu'
        # reset kart properties
        app.px = app.cellWidth//2
        app.py = app.cellWidth//2
        app.angle = 0
        app.lap = 0
        # reset item properties
        app.bananaCoords = []
        app.fakeitemboxCoords = []

######################################
# Game Over
######################################

def gameOver(app):
    # Game ends after 3 laps
    if app.lap > 3:
        app.mode = 'gameOver'
        # Reset race + track properties
        app.px = app.cellWidth//2
        app.py = app.cellWidth//2
        app.angle = 0
        app.lap = 1
        # Store time into .txt file
        mapScores = app.allTimeScores[app.mapForScore]
        mapScores.append(app.totalTimePassed)
        writeFile('myData.txt', repr(app.allTimeScores))

def gameOver_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='black')
    canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(app.congrats))
    canvas.create_rectangle(app.cx-150, app.height*1/5-40, app.cx+150, 
                            app.height*1/5+40, fill='pink', width=5)
    canvas.create_text(app.cx, app.height * 1/5, text='Game Over!',
                       font='Impact 40 bold', fill='navy')
    canvas.create_rectangle(app.cx-230, app.cy-70, app.cx+230, app.cy+70,
                            fill='beige', width=5)
    # Display current time all-time highscore
    allTimeScores = ast.literal_eval(readFile('myData.txt'))
    mapScores = allTimeScores[app.mapForScore]
    highscore = min(mapScores)
    canvas.create_text(app.cx, app.cy,
                       text=f"Your score: {app.totalTimePassed}s \n Highscore: {highscore}s",
                       font='Roboto 35 bold')
    canvas.create_rectangle(app.cx-250, app.height*4/5-60, app.cx+250, 
                            app.height*4/5+60, fill='yellow', width=5)
    canvas.create_text(app.cx, app.height*4/5, 
                       text='Press R to Play Again \n Press Q twice to exit',
                       font='Roboto 30 bold')

def gameOver_keyPressed(app, event):
    if event.key == 'r':
        app.mode = 'mapSelect'
    elif event.key == 'q':
        quit()

# Basic File IO Credit: https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

runApp(width=1498, height=576)