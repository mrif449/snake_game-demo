from tkinter import *
import random
from turtle import speed

#taking measurement
height = 700
witdth = 700
start_size = 3
move_speed = 90
spacing = 50

#color selection
background_color = "#add644"
snake_color = "#5b7afa"
food_color = "#0000ff"
gameover_message = "#ff0000"

#font declaration
font = "Showcard Gothic"
size = "70"
show = "Game Over!"

#designing class(elements)
class Snake:
    def __init__(self) -> None:
        self.start_size = start_size
        self.path = []
        self.coordinates = []
        for x in range(start_size):
            self.coordinates.append([0,0])
        for y,z in self.coordinates:
            path = canvas.create_rectangle(y,z,y+spacing,z+spacing,fill=snake_color,tag="snake")
            self.path.append(path)

class Food:
    def __init__(self) -> None:
        a = random.randint(0,(witdth/spacing)-1)*spacing
        b = random.randint(0,(height/spacing)-1)*spacing
        self.coordinates = [a,b]
        canvas.create_oval(a,b,a+spacing,b+spacing,fill=food_color,tag="food")

#creating functions
def move(snake,food):
    a,b = snake.coordinates[0]
    if direction == "right":
        a += spacing
    elif direction == "left":
        a -= spacing
    elif direction == "down":
        b += spacing
    elif direction == "up":
        b -= spacing
    
    
    snake.coordinates.insert(0,(a,b))
    path = canvas.create_rectangle(a,b,a+spacing,b+spacing,fill=snake_color)
    snake.path.insert(0,path)
    if a == food.coordinates[0] and b == food.coordinates[1]:
        global point
        point += 1
        label.config(text="Point:{}".format(point))
        canvas.delete("food")
        food= Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.path[-1])
        del snake.path[-1]
    if crash(snake):
        game_end()
    else:
        display.after(move_speed,move,snake,food)

def change_move(new_move):
    global direction
    if new_move == "right":
        if direction != "left":
            direction = new_move
    elif new_move == "left":
        if direction != 'right':
                direction = new_move
    elif new_move == 'down':
        if direction != 'up':
            direction = new_move
    elif new_move == 'up':
        if direction != 'down':
            direction = new_move
    
def crash(snake):
    a,b = snake.coordinates[0]
    if a<0 or a>=witdth:
        return True
    elif b<0 or b>=height:
        return True
    for start_size in snake.coordinates[1:]:
        if a == start_size[0] and b == start_size[1]:
            return True
    return False

def game_end():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,font=("Consolas",70), text=show, fill=gameover_message, tag="gameend")

#build up properties
display = Tk()
display.title("Snake Mania")
display.resizable(False,False)

point = 0
direction = "down"

label = Label(display,text="Point:{}".format(point),font=("Consolas",40))
label.pack()

canvas = Canvas(display, bg=background_color, height=height,width=witdth)
canvas.pack()

display.update()

display_height = display.winfo_width()
display_width = display.winfo_height()
screen_width = display.winfo_screenwidth()
screen_height = display.winfo_screenheight()

a = int((screen_width/2)-(display_width/2))
b = int((screen_height/2)-(display_height/2))

display.geometry(f"{display_width}x{display_height}+{a}+{b}")

#accessing controls
display.bind("<Right>",lambda event: change_move("right"))
display.bind("<Left>",lambda event: change_move("left"))
display.bind("<Down>",lambda event: change_move("down"))
display.bind("<Up>",lambda event: change_move("up"))

#runner
snake = Snake()
food = Food()
move(snake,food)
display.mainloop()