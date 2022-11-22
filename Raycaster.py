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
                                        fill='white', width=1)

def rayDist(cx, cy, rx, ry):
    return math.sqrt((rx-cx)**2 + (ry-cy)**2)

def getHorizontalRayEnd(app, angle, px, py, map):
    dof = 0
    if almostEqual(angle, 0, 0.1) or almostEqual(angle, math.pi, 0.1):
        rx = px
        ry = py
        dof = 8
    else:
        aTan = -1/math.tan(angle)
        if angle < math.pi:
            ry = (py//app.cellWidth)*app.cellWidth
            rx = px + (py-ry)*aTan
            dy = -1*app.cellWidth
            dx = -1*dy*aTan
        elif angle > math.pi:
            ry = (py//app.cellWidth)*app.cellWidth + app.cellWidth
            rx = px + (py-ry)*aTan
            dy = app.cellWidth
            dx = -1*dy*aTan
    while dof < 8:
        mx = roundHalfUp(rx//app.cellWidth)
        my = roundHalfUp(ry//app.cellWidth)
        if mx < len(map[0]) and mx >= 0:
            if my >= 0 and my < len(map):
                if map[my][mx] == 1:
                    dof = 8
                else:
                    rx += dx
                    ry += dy
                    dof += 1
    return rx, ry

def getVerticalRayEnd(app, angle, px, py, map):
    dof = 0
    if almostEqual(angle, math.pi/2, 0.1) or almostEqual(angle, math.pi*1.5, 0.1):
        rx = px
        ry = py
        dof = 8
    else:
        nTan = -1*math.tan(angle)
        if angle > math.pi/2 and angle < math.pi*1.5:
            rx = (px//app.cellWidth)*app.cellWidth
            ry = py + (px-rx)*nTan
            dx = -1*app.cellWidth
            dy = -1*dx*nTan
        elif angle < math.pi/2 or angle > math.pi*1.5:
            rx = (px//app.cellWidth)*app.cellWidth + app.cellWidth
            ry = py + (px-rx)*nTan
            dx = app.cellWidth
            dy = -1*dx*nTan
    while dof < 8:
        mx = roundHalfUp(rx//app.cellWidth)
        my = roundHalfUp(ry//app.cellWidth)
        if mx < len(map[0]) and mx >= 0:
            if my >= 0 and my < len(map):
                if map[my][mx] == 1:
                    dof = 8
                else:
                    rx += dx
                    ry += dy
                    dof += 1
    return rx, ry

def drawRays(app, canvas):
    hx, hy = getHorizontalRayEnd(app, app.angle, app.cx, app.cy, app.map)
    vx, vy = getVerticalRayEnd(app, app.angle, app.cx, app.cy, app.map)
    distH = rayDist(app.cx, app.cy, hx, hy)
    distV = rayDist(app.cx, app.cy, vx, vy)
    if distH < distV:
        canvas.create_line(app.cx, app.cy, hx, hy)
    else:
        canvas.create_line(app.cy, app.cy, vx, vy)

def keyPressed(app, event):
    dy = app.playerRadius*math.sin(app.angle)
    dx = app.playerRadius*math.cos(app.angle)
    if event.key == 'w':
        app.cy -= dy
        app.cx += dx
    elif event.key == 's':
        app.cy += dy
        app.cx -= dx
    elif event.key == 'Left':
        app.angle += 0.1
        if app.angle >= 2*math.pi:
            app.angle -= 2*math.pi
    elif event.key == 'Right':
        app.angle -= 0.1
        if app.angle < 0:
            app.angle += 2*math.pi

def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='dark gray')
    drawGrid(app.cellWidth, app.map, app, canvas)
    drawPlayer(app, canvas)
    drawRays(app, canvas)

runApp(width=1024, height=512)