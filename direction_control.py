from microbit import display, Image, sleep
import tinybit

# Define movement patterns
MOVEMENTS = [
    (tinybit.car_run, 150, Image.ARROW_S, 1000),  # Forward
    (tinybit.car_back, 150, Image.ARROW_N, 1000),  # Backward
    (tinybit.car_left, 150, Image.ARROW_E, 1000),  # Left
    (tinybit.car_right, 150, Image.ARROW_W, 1000),  # Right
    (tinybit.car_spinleft, 150, Image.ARROW_E, 1000),  # Spin left
    (tinybit.car_spinright, 150, Image.ARROW_W, 1000)  # Spin right
]

while True:
    for move_func, speed, arrow, duration in MOVEMENTS:
        move_func(speed)  # Execute movement
        display.show(arrow)  # Show corresponding arrow
        sleep(duration)  # Wait

    # Stop between movement sequences
    tinybit.car_stop()
    display.clear()
    sleep(1000)
