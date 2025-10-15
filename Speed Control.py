# Import libraries
from microbit import display, Image, sleep
import tinybit

# Show "happy face" to confirm program startup
display.show(Image.HAPPY)
sleep(1000)  # Keep face for 1 second

# Define speed profiles: (left motor speed, right motor speed, duration)
# Speed range: 0 (stop) - 255 (max speed); equal left/right = straight movement
SPEED_LEVELS = [
    (0, 0, 1000),    # Level 1: Stop
    (50, 50, 1000),  # Level 2: Very slow
    (100, 100, 1000),# Level 3: Slow
    (180, 180, 1000),# Level 4: Medium
    (255, 255, 1000) # Level 5: Max speed
]

# Cycle through speed levels repeatedly
while True:
    for left_speed, right_speed, wait_time in SPEED_LEVELS:
        tinybit.car_run(left_speed, right_speed)  # Set motor speed
        sleep(wait_time)                          # Hold speed for set time
