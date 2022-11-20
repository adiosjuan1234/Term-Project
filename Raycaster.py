from cmu_112_graphics import *
from math import *

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

def appStarted(app):
    app.cx = 300
    app.cy = 300
    app.playerRadius = 5
    app.cellWidth = 64
    app.map = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
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
                                        fill='dark gray', width=1)
            if map[row][col] == 1:
                canvas.create_rectangle(cellWidth * col, cellWidth * row,
                                        cellWidth * (col+1), cellWidth*(row+1),
                                        fill='white', width=1)
                

def drawRays(app, canvas):
    for _ in range(1):
        dof = 0
        if app.angle == 0 or app.angle == pi:
            rx = app.cx
            ry = app.cy
            dof = 8
        elif almostEqual(app.angle, pi/2, 0.001) or almostEqual(app.angle, pi*1.5, 0.001):
            ry = app.cy//64*64
            rx = app.cx
            y0 = -64
            x0 = 0
        aTan = -1/tan(app.angle)
        if app.angle < pi:
            ry = app.cy//64*64
            rx = int((app.cy-ry)*aTan+app.cx)
            y0 = -64
            x0 = int(-y0*aTan)
        elif app.angle > pi:
            ry = app.cy//64*64 + 64
            rx = int((app.cy-ry)*aTan+app.cx)
            y0 = 64
            x0 = int(-y0*aTan)
        while dof < 8:
            mx = rx//64
            my = ry//64
            if mx < len(app.map[0]) and mx >= 0:
                if my >= 0 and my < len(app.map):
                    if app.map[my][mx] == 1:
                        dof = 8
                    else:
                        rx += x0
                        ry += y0
                        dof += 1
        canvas.create_line(app.cx, app.cy, rx, ry, fill='yellow', width=5)

def keyPressed(app, event):
    if event.key == 'w':
        dy = app.playerRadius*sin(app.angle)
        dx = app.playerRadius*cos(app.angle)
        app.cy -= dy
        app.cx += dx
    elif event.key == 's':
        dy = app.playerRadius*sin(app.angle)
        dx = app.playerRadius*cos(app.angle)
        app.cy += dy
        app.cx -= dx
    elif event.key == 'Left':
        app.angle += pi/32
        if app.angle >= 2*pi:
            app.angle -= 2*pi
    elif event.key == 'Right':
        app.angle -= pi/32
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