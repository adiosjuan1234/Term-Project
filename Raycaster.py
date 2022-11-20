from cmu_112_graphics import *
from math import *

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

def appStarted(app):
    app.cx = 32
    app.cy = 32
    app.playerRadius = 5
    app.cellWidth = 64
    app.map = [
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
    app.angle = 0

def drawPlayer(app, canvas):
    canvas.create_rectangle(app.cx-app.playerRadius, app.cy-app.playerRadius, 
                            app.cx+app.playerRadius, app.cy+app.playerRadius, 
                            fill='yellow')
    canvas.create_line(app.cx, app.cy,
                       app.cx + app.playerRadius**2*cos(app.angle), 
                       app.cy - app.playerRadius**2*sin(app.angle),
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
                                        fill='white', width=1)

def rayDist(cx, cy, rx, ry):
    return sqrt((rx-cx)**2 + (ry-cy**2))                

def drawRays(app, canvas):
    # Draw 1 ray for now
    for _ in range(1):

        # Horizontal ray casting
        dof = 0
        hx, hy, distH = app.cx, app.cy, 0
        if almostEqual(app.angle, 0, 0.1) or almostEqual(app.angle, pi, 0.1):
            rx = app.cx
            ry = app.cy
            dof = 8
        else:
            aTan = -1/tan(app.angle)
            print(aTan)
            if app.angle < pi:
                ry = (app.cy//app.cellWidth)*app.cellWidth
                rx = int(app.cx + (app.cy-ry)*aTan)
                y0 = -1*app.cellWidth
                x0 = int(-1*y0*aTan)
            elif app.angle > pi:
                ry = (app.cy//app.cellWidth)*app.cellWidth + app.cellWidth
                rx = int(app.cx + (app.cy-ry)*aTan)
                y0 = app.cellWidth
                x0 = int(-1*y0*aTan)
        while dof < 8:
            mx = rx//app.cellWidth
            my = ry//app.cellWidth
            if mx < len(app.map[0]) and mx >= 0:
                if my >= 0 and my < len(app.map):
                    if app.map[my][mx] == 1:
                        dof = 8
                        hx, hy = rx, ry
                        distH = rayDist(app.cx, app.cy, hx, hy)
                    else:
                        rx += x0
                        ry += y0
                        dof += 1
        
        # Vertical ray casting
        dof = 0
        vx, vy, distV = app.cx, app.cy, 0
        if almostEqual(app.angle, 0, 0.1) or almostEqual(app.angle, pi, 0.1):
            rx = app.cx
            ry = app.cy
            dof = 8
        else:
            nTan = -1*tan(app.angle)
            print(aTan)
            if app.angle > pi/2 and app.angle < pi*1.5:
                rx = (app.cx//app.cellWidth)*app.cellWidth
                ry = int(app.cy + (app.cx-rx)*nTan)
                x0 = -1*app.cellWidth
                y0 = int(-1*x0*nTan)
            elif app.angle < pi/2 or app.angle > pi*1.5:
                rx = (app.cx//app.cellWidth)*app.cellWidth + app.cellWidth
                ry = int(app.cy + (app.cx-rx)*nTan)
                x0 = app.cellWidth
                y0 = int(-1*x0*nTan)
        while dof < 8:
            mx = rx//app.cellWidth
            my = ry//app.cellWidth
            if mx < len(app.map[0]) and mx >= 0:
                if my >= 0 and my < len(app.map):
                    if app.map[my][mx] == 1:
                        dof = 8
                        vx, vy = rx, ry
                        distV = rayDist(app.cx, app.cy, vx, vy)
                    else:
                        rx += x0
                        ry += y0
                        dof += 1
        
        # Find the shortest ray and draw it
        if distH < distV:
            vx, vy = app.cx, app.cy
        elif distV < distH:
            hx, hy = app.cx, app.cy
        canvas.create_line(app.cx, app.cy, rx, ry, fill='green')

def keyPressed(app, event):
    dy = app.playerRadius*sin(app.angle)
    dx = app.playerRadius*cos(app.angle)
    if event.key == 'w':
        app.cy -= dy
        app.cx += dx
    elif event.key == 's':
        app.cy += dy
        app.cx -= dx
    elif event.key == 'Left':
        app.angle += 0.1
        if app.angle >= 2*pi:
            app.angle -= 2*pi
    elif event.key == 'Right':
        app.angle -= 0.1
        if app.angle <= -2*pi:
            app.angle += 2*pi

def timerFired(app):
    pass

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='dark gray')
    drawGrid(app.cellWidth, app.map, app, canvas)
    drawPlayer(app, canvas)
    # drawRays(app, canvas)

runApp(width=1024, height=512)