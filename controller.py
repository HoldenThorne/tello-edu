import keyboard,os
from djitellopy import Tello

# Makes Tello object and connects to wifi 
tello = Tello()
tello.connect()

# Gets battery percentage
print(f"battery = {tello.get_battery()}")

# Direction variables
left_right = 0
forward_backward = 0
up_down = 0
turn = 0

# Takeoff and land variable
take_off_land = False

# Main loop
while True:

    # Takeoff
    if keyboard.is_pressed("space") and take_off_land == False:
        tello.takeoff()
        take_off_land = True

    # Land
    if keyboard.is_pressed("space") and take_off_land == True:
        tello.land()
        take_off_land = False

    # Direction controll forward/backward
    if keyboard.is_pressed("w"):
        forward_backward = 100
    elif keyboard.is_pressed("s"):
        forward_backward = -100
    else:
        forward_backward = 0

    # Direction controll left/right
    if keyboard.is_pressed("a"):
        left_right = -100
    elif keyboard.is_pressed("d"):
        left_right = 100
    else:
        left_right = 0
    
    # Direction controll up/down
    if keyboard.is_pressed("up arrow"):
        up_down = 100
    elif keyboard.is_pressed("down arrow"):
        up_down = -100
    else:
        up_down = 0

    # Direction controll turn
    if keyboard.is_pressed("left arrow"):
        turn = -100
    elif keyboard.is_pressed("right arrow"):
        turn = 100
    else:
        turn = 0

    # Flip controll forward
    if keyboard.is_pressed("i"):
        tello.flip_forward()

    # Flip controll left
    if keyboard.is_pressed("j"):
        tello.flip_left()

    # Flip controll right
    if keyboard.is_pressed("l"):
        tello.flip_right()

    # Flip controll backward
    if keyboard.is_pressed("k"):
        tello.flip_back()

    # Emergency stop
    if keyboard.is_pressed("q"):
        tello.emergency()
        break

    # Drone movment
    tello.send_rc_control(left_right,forward_backward,up_down,turn)

# Clear terminal
os.system("clear")