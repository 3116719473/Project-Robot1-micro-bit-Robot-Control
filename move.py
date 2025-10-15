# Import required libraries for Micro:bit and Tinybit robot
from microbit import display, Image, sleep
import tinybit

# Display downward arrow (indicates robot will move forward)
display.show(Image.ARROW_S)

# Move robot forward at speed 150 (range: 0-255, 255 = max speed)
tinybit.car_run(150)

# Keep moving for 2 seconds (sleep() uses milliseconds: 2000ms = 2s)
sleep(2000)

# Stop the robot after movement
tinybit.car_stop()

# Clear LED display to end the program
display.clear()
