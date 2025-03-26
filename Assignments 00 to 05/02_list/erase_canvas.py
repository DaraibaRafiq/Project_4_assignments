from graphics import *
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    mouse_x = canvas.getMouse().getX()
    mouse_y = canvas.getMouse().getY()
    
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    overlapping_objects = canvas.items[:]
    for obj in overlapping_objects:
        if isinstance(obj, Rectangle):
            obj_left = obj.getP1().getX()
            obj_top = obj.getP1().getY()
            obj_right = obj.getP2().getX()
            obj_bottom = obj.getP2().getY()
            
            if obj_left < right_x and obj_right > left_x and obj_top < bottom_y and obj_bottom > top_y:
                obj.setFill("white")

canvas = GraphWin("Eraser Canvas", CANVAS_WIDTH, CANVAS_HEIGHT)

num_rows = CANVAS_HEIGHT // CELL_SIZE
num_cols = CANVAS_WIDTH // CELL_SIZE

for row in range(num_rows):
    for col in range(num_cols):
        left_x = col * CELL_SIZE
        top_y = row * CELL_SIZE
        right_x = left_x + CELL_SIZE
        bottom_y = top_y + CELL_SIZE
        
        cell = Rectangle(Point(left_x, top_y), Point(right_x, bottom_y))
        cell.setFill("blue")
        cell.draw(canvas)

eraser = Rectangle(Point(0, 0), Point(ERASER_SIZE, ERASER_SIZE))
eraser.setFill("pink")
eraser.draw(canvas)

while True:
    mouse_point = canvas.checkMouse()
    if mouse_point is not None:
        mouse_x = mouse_point.getX()
        mouse_y = mouse_point.getY()
        
        eraser.move(mouse_x - eraser.getP1().getX(), mouse_y - eraser.getP1().getY())
        erase_objects(canvas, eraser)
    
    time.sleep(0.05)
