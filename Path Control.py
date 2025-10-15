# Import libraries
from microbit import display, Image, sleep, button_a, button_b
import tinybit

# Step 1: Define LED images for letters (L/O/D/Z)
LETTER_IMAGES = {
    "L": Image("90000:90000:90000:90000:99999"),  # Letter L
    "O": Image("09990:90009:90009:90009:09990"),  # Letter O
    "D": Image("99000:90900:90090:90009:99999"),  # Letter D
    "Z": Image("99999:00090:00900:09000:99999")   # Letter Z
}

# Step 2: Define movement sequences for each letter (action, speed, duration)
LETTER_PATHS = {
    "L": [("run", 80, 1000), ("spinleft", 180, 400), ("run", 80, 1000), ("stop", 0, 0)],
    "O": [("run", 80, 1000), ("spinleft", 180, 400)] * 4 + [("stop", 0, 0)],  # Circle for O
    "D": [("run", 80, 1000), ("spinleft", 180, 500), ("run", 80, 1500), ("stop", 0, 0)],
    "Z": [("run", 80, 1000), ("spinright", 120, 500), ("run", 80, 1300), ("stop", 0, 0)]
}

# Step 3: Initialize program
display.show(Image.HAPPY)
sleep(1000)
current_letter_idx = 0  # Track selected letter (0=L, 1=O, 2=D, 3=Z)
letter_list = list(LETTER_IMAGES.keys())  # Convert dict keys to list

# Step 4: Button control loop
while True:
    # Button A: Switch between letters
    if button_a.was_pressed():
        current_letter_idx = (current_letter_idx + 1) % len(letter_list)
        current_letter = letter_list[current_letter_idx]
        display.show(LETTER_IMAGES[current_letter])  # Show selected letter

    # Button B: Execute path for selected letter
    if button_b.was_pressed():
        current_letter = letter_list[current_letter_idx]
        display.show(LETTER_IMAGES[current_letter])
        sleep(1000)  # Show letter before moving

        # Run movement sequence
        for action, speed, duration in LETTER_PATHS[current_letter]:
            if action == "run":
                tinybit.car_run(speed)
            elif action == "spinleft":
                tinybit.car_spinleft(speed)
            elif action == "spinright":
                tinybit.car_spinright(speed)
            elif action == "stop":
                tinybit.car_stop()
            if duration > 0:
                sleep(duration)

        # Reset after path completion
        display.clear()
        sleep(500)
        display.show(LETTER_IMAGES[current_letter])  # Re-show selected letter
