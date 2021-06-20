def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump_up():
    while not is_facing_north():
        turn_left()
    
    while wall_on_right():
        move()
    
    turn_right()
    move()
    turn_right()
    
def jump_down():
    while front_is_clear():
        move()
    turn_left()
    
def jump():
    jump_up()
    jump_down()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

    