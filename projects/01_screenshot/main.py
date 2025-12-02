# Goal: Master file I/O and System Interaction.
# 1. The Auto-Screenshot Reminder
# Concept: Infinite loops, timestamps, binary file writing.

# Lesson learned: automation doesn't have to be big, it just has to be useful.

# Personal notes:
# This is an infinite loop, using CLI maybe using a button to start / stop would be best?
# What happens when you have multiple monitors? What is being captured? Should we notify the user?
# Maybe next versions will include using parameters to change the directory, add specific name,
# and even reduce the time for the screenshots.


import pyautogui
import time
from pathlib import Path

DEFAULT_TIME_BETWEEN_SCREENSHOTS = 300  # Expressed in seconds, meaning 5 minutes.


def main():
    directory_storing_screenshots = "automated_screenshots"
    my_dir = Path(directory_storing_screenshots)
    try:
        my_dir.mkdir()
        print(f"Directory {directory_storing_screenshots} created.")
    except FileExistsError:
        print(f"Directory {directory_storing_screenshots} already exists.")

    while True:
        file_name = time.strftime("%Y-%m-%d_%H-%M-%S") + ".png"

        pyautogui.screenshot(my_dir.joinpath(file_name))

        time.sleep(DEFAULT_TIME_BETWEEN_SCREENSHOTS)


if __name__ == "__main__":
    main()
