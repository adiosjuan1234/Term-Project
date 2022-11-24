from cmu_112_graphics import *
import math
import decimal

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def appStarted(app):
    app.cx = 32
    app.cy = 32
    app.playerRadius = 5
    app.map = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
            [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1],
            [0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1],
            [0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1],
            [0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1],
            [0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
            [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
            [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
    app.cellWidth = app.height/len(app.map)
    app.angle = 0
    app.timerDelay = 20

def drawBackground(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height/2,
                            fill='sky blue',width=0)
    canvas.create_rectangle(0, app.height/2, app.width, app.height,
                            fill='dark gray', width=0)

def drawPlayer(app, canvas):
    canvas.create_rectangle(app.cx-app.playerRadius, app.cy-app.playerRadius, 
                            app.cx+app.playerRadius, app.cy+app.playerRadius, 
                            fill='yellow')
    canvas.create_line(app.cx, app.cy,
                       app.cx + app.playerRadius**2*math.cos(app.angle), 
                       app.cy - app.playerRadius**2*math.sin(app.angle),
                       width=5, fill='yellow')

def drawGrid(cellWidth, map, app, canvas):
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

def drawRays(app, canvas, numDeg):
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
        hx, hy = getHorizontalRayEnd(app, angle, app.cx, app.cy, app.map)
        vx, vy = getVerticalRayEnd(app, angle, app.cx, app.cy, app.map)
        distH = rayDist(app.cx, app.cy, hx, hy)
        distV = rayDist(app.cx, app.cy, vx, vy)

        # Draw the ray with the shortest distance
        if distH == 0:
            distFinal = distV
            canvas.create_line(app.cx, app.cy, vx, vy, fill='lime', width=1)
        elif distV == 0:
            distFinal = distH
            canvas.create_line(app.cx, app.cy, hx, hy, fill='lime', width=1)
        elif distV < distH:
            distFinal = distV
            canvas.create_line(app.cx, app.cy, vx, vy, fill='lime', width=1)
        elif distH < distV:
            distFinal = distH
            canvas.create_line(app.cx, app.cy, hx, hy, fill='lime', width=1)

        distFinal = distFinal * math.cos(angleDiff)
        lineHeight = app.cellWidth*app.height/distFinal
        if lineHeight > app.height:
            lineHeight = app.height

        newX0 = len(app.map)*app.cellWidth
        xCoord = app.width - newX0/numDeg*x
        lineOffset = app.height/2-lineHeight/2

        if distH == 0:
            distFinal = distV
            canvas.create_line(xCoord, lineOffset, xCoord, lineOffset+lineHeight,
                           width=newX0/numDeg, fill='lime')
        elif distV == 0:
            distFinal = distH
            canvas.create_line(xCoord, lineOffset, xCoord, lineOffset+lineHeight,
                           width=newX0/numDeg, fill='green')
        elif distV < distH:
            distFinal = distV
            canvas.create_line(xCoord, lineOffset, xCoord, lineOffset+lineHeight,
                           width=newX0/numDeg, fill='lime')
        elif distH < distV:
            distFinal = distH
            canvas.create_line(xCoord, lineOffset, xCoord, lineOffset+lineHeight,
                           width=newX0/numDeg, fill='green')

def keyPressed(app, event):
    dy = app.playerRadius*math.sin(app.angle)
    dx = app.playerRadius*math.cos(app.angle)
    if event.key == 'w':
        tempMy = roundHalfUp((app.cy - dy)//app.cellWidth)
        tempMx = roundHalfUp((app.cx + dx)//app.cellWidth)
        tempCx = app.cx + dx
        tempCy = app.cy - dy
        if tempCx > 0 and tempCx < app.cellWidth*len(app.map):
            if tempCy > 0 and tempCy < app.height:
                if app.map[tempMy][tempMx] == 0:
                    app.cy -= dy
                    app.cx += dx
    if event.key == 's':
        tempMy = roundHalfUp((app.cy + dy)//app.cellWidth)
        tempMx = roundHalfUp((app.cx - dx)//app.cellWidth)
        tempCx = app.cx - dx
        tempCy = app.cy + dy
        if tempCx > 0 and tempCx < app.cellWidth*len(app.map):
            if tempCy > 0 and tempCy < app.height:
                if app.map[tempMy][tempMx] == 0:
                    app.cy += dy
                    app.cx -= dx
    elif event.key == 'a':
        pass
    elif event.key == 'd':
        pass
    elif event.key == 'Left':
        if app.angle + 0.05 >= 2*math.pi:
            app.angle -= 2*math.pi
        app.angle += 0.05
    elif event.key == 'Right':
        if app.angle - 0.05 < 0:
            app.angle += 2*math.pi
        app.angle -= 0.05

def timerFired(app):
    dy = 4*math.sin(app.angle)
    dx = 4*math.cos(app.angle)
    tempMy = roundHalfUp((app.cy - dy)//app.cellWidth)
    tempMx = roundHalfUp((app.cx + dx)//app.cellWidth)
    tempCx = app.cx + dx
    tempCy = app.cy - dy
    if tempCx > 0 and tempCx < app.cellWidth*len(app.map):
        if tempCy > 0 and tempCy < app.height:
            if app.map[tempMy][tempMx] == 0:
                app.cy -= dy
                app.cx += dx

def redrawAll(app, canvas):
    drawBackground(app, canvas)
    drawGrid(app.cellWidth, app.map, app, canvas)
    drawRays(app, canvas, 180)
    drawPlayer(app, canvas)

runApp(width=1024, height=512)