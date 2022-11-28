from cmu_112_graphics import *
import math
import decimal

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

    # Race things
    app.playerRadius = 1.5
    app.speed = app.playerRadius*0.6
    app.playerHitbox = 5
    app.cellWidth = 8
    app.px = app.cellWidth//2
    app.py = app.cellWidth//2
    app.angle = 0
    app.timerDelay = 16

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
            app.selectedMap = app.map1
            app.mode = 'raceMode'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'yoshi'
            app.selectedMap = app.map1
            app.mode = 'raceMode'
    elif event.x >= 196 and event.x <= 329:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'luigi'
            app.selectedMap = app.map1
            app.mode = 'raceMode'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'donkeykong'
            app.selectedMap = app.map1
            app.mode = 'raceMode'
    elif event.x >= 344 and event.x <= 477:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'peach'
            app.selectedMap = app.map1
            app.mode = 'raceMode'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'wario'
            app.selectedMap = app.map1
            app.mode = 'raceMode'
    elif event.x >= 492 and event.x <= 625:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'toad'
            app.selectedMap = app.map1
            app.mode = 'raceMode'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'bowser'
            app.selectedMap = app.map1
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
    if event.x >= 48 and event.x <= 181:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'mario'
            app.selectedMap = app.map2
            app.mode = 'raceMode'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'yoshi'
            app.selectedMap = app.map2
            app.mode = 'raceMode'
    elif event.x >= 196 and event.x <= 329:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'luigi'
            app.selectedMap = app.map2
            app.mode = 'raceMode'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'donkeykong'
            app.selectedMap = app.map2
            app.mode = 'raceMode'
    elif event.x >= 344 and event.x <= 477:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'peach'
            app.selectedMap = app.map2
            app.mode = 'raceMode'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'wario'
            app.selectedMap = app.map2
            app.mode = 'raceMode'
    elif event.x >= 492 and event.x <= 625:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'toad'
            app.selectedMap = app.map2
            app.mode = 'raceMode'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'bowser'
            app.selectedMap = app.map2
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
    if event.x >= 48 and event.x <= 181:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'mario'
            app.selectedMap = app.map3
            app.mode = 'raceMode'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'yoshi'
            app.selectedMap = app.map3
            app.mode = 'raceMode'
    elif event.x >= 196 and event.x <= 329:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'luigi'
            app.selectedMap = app.map3
            app.mode = 'raceMode'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'donkeykong'
            app.selectedMap = app.map3
            app.mode = 'raceMode'
    elif event.x >= 344 and event.x <= 477:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'peach'
            app.selectedMap = app.map3
            app.mode = 'raceMode'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'wario'
            app.selectedMap = app.map3
            app.mode = 'raceMode'
    elif event.x >= 492 and event.x <= 625:
        if event.y >= 68 and event.y <= 217:
            app.selectedCharacter = 'toad'
            app.selectedMap = app.map3
            app.mode = 'raceMode'
        elif event.y >= 232 and event.y <= 382:
            app.selectedCharacter = 'bowser'
            app.selectedMap = app.map3
            app.mode = 'raceMode'

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def drawBackground(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height/2,
                            fill='sky blue',width=0)
    canvas.create_rectangle(0, app.height/2, app.width, app.height,
                            fill='dark gray', width=0)

def drawPlayer(app, canvas):
    canvas.create_rectangle(app.px-app.playerRadius, app.py-app.playerRadius, 
                            app.px+app.playerRadius, app.py+app.playerRadius, 
                            fill='yellow')
    canvas.create_line(app.px, app.py,
                       app.px + app.playerHitbox*math.cos(app.angle), 
                       app.py - app.playerHitbox*math.sin(app.angle),
                       width=2, fill='yellow')

def drawGrid(cellWidth, map, canvas):
    for row in range(len(map)):
        for col in range(len(map[0])):
            canvas.create_rectangle(cellWidth * col, cellWidth * row,
                                        cellWidth * (col+1), cellWidth*(row+1),
                                        fill='black', width=1)
            if map[row][col] == 1:
                canvas.create_rectangle(cellWidth * col, cellWidth * row,
                                        cellWidth * (col+1), cellWidth*(row+1),
                                        fill='white', width=0)

def rayDist(cx, cy, rx, ry):
    return math.sqrt((rx-cx)**2 + (ry-cy)**2)

def getHorizontalRayEnd(app, angle, px, py, map):
    dof = 0
    maxDof = len(map)
    rx, ry = px, py
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
    dof = 0
    maxDof = len(map)
    rx, ry = px, py
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

def drawRays3D(app, canvas, numDeg):
    distFinal = 0
    
    for x in range(numDeg+1):
        # Get the angle
        angleDiff = 0.01745329/3*(-1*numDeg/2 + x)
        angle = app.angle + angleDiff
        if angle < 0:
            angle += 2*math.pi
        elif angle > 2*math.pi:
            angle -= 2*math.pi

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
        distFinal = distFinal * math.cos(angleDiff)

        # 3D line height formula
        lineHeight = app.cellWidth*app.height/distFinal
        if lineHeight > app.height:
            lineHeight = app.height

        # 3D line coordinate + offset from top of screen
        xCoord = app.width - app.width/numDeg*x
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

def raceMode_keyPressed(app, event):
    dy = app.speed*math.sin(app.angle)
    dx = app.speed*math.cos(app.angle)
    if event.key == 'w':
        tempCx = app.px + app.playerHitbox*math.cos(app.angle)
        tempCy = app.py - app.playerHitbox*math.sin(app.angle)
        tempMy = roundHalfUp((tempCy)//app.cellWidth)
        tempMx = roundHalfUp((tempCx)//app.cellWidth)
        if tempCx > 0 and tempCx < app.cellWidth*len(app.selectedMap):
            if tempCy > 0 and tempCy < app.height:
                if app.selectedMap[tempMy][tempMx] == 0:
                    app.py -= dy
                    app.px += dx
    elif event.key == 's':
        tempCx = app.px - app.playerHitbox*math.cos(app.angle)
        tempCy = app.py + app.playerHitbox*math.sin(app.angle)
        tempMy = roundHalfUp((tempCy)//app.cellWidth)
        tempMx = roundHalfUp((tempCx)//app.cellWidth)
        if tempCx > 0 and tempCx < app.cellWidth*len(app.selectedMap):
            if tempCy > 0 and tempCy < app.height:
                if app.selectedMap[tempMy][tempMx] == 0:
                    app.py += dy
                    app.px -= dx
    elif event.key == 'Left':
        if app.angle + 0.04 >= 2*math.pi:
            app.angle -= 2*math.pi
        app.angle += 0.04
    elif event.key == 'Right':
        if app.angle - 0.04 < 0:
            app.angle += 2*math.pi
        app.angle -= 0.04

def raceMode_timerFired(app):
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
    drawRays3D(app, canvas, 180)
    drawGrid(app.cellWidth, app.selectedMap, canvas)
    drawPlayer(app, canvas)

runApp(width=676, height=450)