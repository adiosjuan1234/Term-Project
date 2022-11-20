from cmu_112_graphics import *

def appStarted(app):

    # Open up the window with the start menu
    app.mode = 'startMenu'

    # Canvas center coords for convenience
    app.cx = app.width/2
    app.cy = app.height/2

    # Start Menu Images
    app.startMenuImage = app.loadImage('Start Menu Image.jpeg')
    app.scaledStartMenu = app.scaleImage(app.startMenuImage, 2)
    app.marioKart112 = app.loadImage('Mario Kart 112.png')

    # Map Select Images
    app.mushroomCupImage= app.loadImage('Mushroom Cup.jpeg')
    app.mushroomCup = app.scaleImage(app.mushroomCupImage, 2/3)
    app.starCupImage = app.loadImage('Star Cup.jpeg')
    app.starCup = app.scaleImage(app.starCupImage, 2/3)
    app.specialCupImage = app.loadImage('Special Cup.jpeg')
    app.specialCup = app.scaleImage(app.specialCupImage, 2/3)

    # Character Select Images
    app.mushroomCellImage = app.loadImage('Mushroom Grid Cell.jpeg')
    app.singleMushroom = app.scaleImage(app.mushroomCellImage, 1/5)
    app.starCellImage = app.loadImage('Star Grid Cell.jpeg')
    app.singleStar = app.scaleImage(app.starCellImage, 1/5)
    app.crownCellImage = app.loadImage('Crown Grid Cell.jpeg')
    app.singleCrown = app.scaleImage(app.crownCellImage, 1/5)
    app.characterSelect = app.loadImage('Character Select.jpeg')
    app.characters = app.scaleImage(app.characterSelect, 3/2)
    app.selectedCharacter = ''

    # Maps
    app.marioCircuit1 = app.loadImage('Mario Circuit 1.png')
    app.chocoIsland2 = app.loadImage('Choco Island 2.png')
    app.bowserCastle3 = app.loadImage('Bowser Castle 3.png')

def startMenu_redrawAll(app, canvas):
    canvas.create_image(app.cx, app.cy, 
                        image=ImageTk.PhotoImage(app.scaledStartMenu))
    canvas.create_image(app.cx, 100,
                        image=ImageTk.PhotoImage(app.marioKart112))
    canvas.create_text(app.cx, 300, text="Press any key to continue",
                       font="impact 40 bold", fill='beige')

def startMenu_keyPressed(app, event):
    app.mode = 'mapSelect'

def mapSelect_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='dodgerblue')
    canvas.create_image(app.width*1/6, app.cy,
                        image=ImageTk.PhotoImage(app.mushroomCup))
    canvas.create_text(app.width*1/6, app.cy+85, text='Mushroom Cup',
                       font='helvetica 17 bold', fill='navy blue')
    canvas.create_image(app.cx, app.cy,
                        image=ImageTk.PhotoImage(app.starCup))
    canvas.create_text(app.cx, app.cy+85, text='Star Cup',
                       font='helvetica 17 bold', fill='navy blue')
    canvas.create_image(app.width*5/6, app.cy,
                        image=ImageTk.PhotoImage(app.specialCup))
    canvas.create_text(app.width*5/6, app.cy+85, text='Special Cup',
                       font='helvetica 17 bold', fill='navy blue')
    canvas.create_text(app.cx, 100, text='Click on the icon to select the map!',
                       font='Impact 20', fill='yellow')
    canvas.create_text(10, 10, text='<< Esc to go back', fill='black',
                       font='impact 10', anchor='nw')

def mapSelect_mousePressed(app, event):
    if event.x >= 37 and event.x <= 187:
        if event.y >= 150 and event.y <= 300:
            app.mode = 'mushroomCup'
    elif event.x >= 263 and event.x <= 413:
        if event.y >= 150 and event.y <= 300:
            app.mode = 'starCup'
    elif event.x >= 488 and event.x <= 638:
        if event.y >= 150 and event.y <= 300:
            app.mode = 'specialCup'

def mapSelect_keyPressed(app, event):
    if event.key == 'Escape':
        app.mode = 'startMenu'

def mushroomCup_redrawAll(app, canvas):
    margin = 45//2
    for x in range(margin, app.width, 45):
        for y in range(margin, app.height, 45):
            canvas.create_image(x, y, 
                                image=ImageTk.PhotoImage(app.singleMushroom))
    canvas.create_image(app.cx, app.cy,
                        image=ImageTk.PhotoImage(app.characters))

def mushroomCup_keyPressed(app, event):
    if event.key == 'Escape':
        app.mode = 'mapSelect'

def mushroomCup_mousePressed(app, event):
    if event.x >= 48 and event.x <= 181:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'mario'
            app.mode = 'marioCircuitOne'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'yoshi'
            app.mode = 'marioCircuitOne'
    elif event.x >= 196 and event.x <= 329:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'luigi'
            app.mode = 'marioCircuitOne'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'donkeykong'
            app.mode = 'marioCircuitOne'
    elif event.x >= 344 and event.x <= 477:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'peach'
            app.mode = 'marioCircuitOne'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'wario'
            app.mode = 'marioCircuitOne'
    elif event.x >= 492 and event.x <= 625:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'toad'
            app.mode = 'marioCircuitOne'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'bowser'
            app.mode = 'marioCircuitOne'

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
    if event.x >= 48 and event.x <= 181:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'mario'
            app.mode = 'chocoIslandTwo'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'yoshi'
            app.mode = 'chocoIslandTwo'
    elif event.x >= 196 and event.x <= 329:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'luigi'
            app.mode = 'chocoIslandTwo'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'donkeykong'
            app.mode = 'chocoIslandTwo'
    elif event.x >= 344 and event.x <= 477:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'peach'
            app.mode = 'chocoIslandTwo'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'wario'
            app.mode = 'chocoIslandTwo'
    elif event.x >= 492 and event.x <= 625:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'toad'
            app.mode = 'chocoIslandTwo'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'bowser'
            app.mode = 'chocoIslandTwo'

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
    if event.x >= 48 and event.x <= 181:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'mario'
            app.mode = 'bowserCastleThree'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'yoshi'
            app.mode = 'bowserCastleThree'
    elif event.x >= 196 and event.x <= 329:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'luigi'
            app.mode = 'bowserCastleThree'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'donkeykong'
            app.mode = 'bowserCastleThree'
    elif event.x >= 344 and event.x <= 477:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'peach'
            app.mode = 'bowserCastleThree'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'wario'
            app.mode = 'bowserCastleThree'
    elif event.x >= 492 and event.x <= 625:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'toad'
            app.mode = 'bowserCastleThree'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'bowser'
            app.mode = 'bowserCastleThree'

def marioCircuitOne_redrawAll(app, canvas):
    canvas.create_image(app.cx, app.cy,
                        image=ImageTk.PhotoImage(app.marioCircuit1))

def chocoIslandTwo_redrawAll(app, canvas):
    canvas.create_image(app.cx, app.cy,
                        image=ImageTk.PhotoImage(app.chocoIsland2))

def bowserCastleThree_redrawAll(app, canvas):
    canvas.create_image(app.cx, app.cy,
                        image=ImageTk.PhotoImage(app.bowserCastle3))

def floorCasting():
    hres = 120
    halfvres = 100

    mod = hres/60
    posx, posy, angle = 0, 0, 0

    for i in range(hres):
        rot_i = rot + mod

runApp(width=676, height=450)