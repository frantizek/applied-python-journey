# Goal: Master file I/O and System Interaction.
# 1. The Auto-Screenshot Reminder
# Concept: Infinite loops, timestamps, binary file writing.

# Lesson learned: automation doesn't have to be big, it just has to be useful.

# Personal notes:
# This is an infinite loop, using CLI maybe using a button to start / stop would be best?
# What happens when you have multiple monitors? What is being captured? Should we notify the user?
# Maybe next versions will include using parameters to change the directory, add specific name,
# and even reduce the time for the screenshots.

import argparse
import pyautogui
import time
import signal
import sys
import logging
from pathlib import Path


DEFAULT_TIME_BETWEEN_SCREENSHOTS = 300  # Expressed in seconds, meaning 5 minutes.


logging.basicConfig(
    filename="screenshot_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)


def parse_args():
    parser = argparse.ArgumentParser(description="Auto-Screenshot Reminder")
    parser.add_argument(
        "--dir", default="automated_screenshots", help="Directory to store screenshots"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=DEFAULT_TIME_BETWEEN_SCREENSHOTS,
        help="Time between screenshots (seconds)",
    )
    return parser.parse_args()


def signal_handler(sig, frame):
    print("\nExiting gracefully. The Force will be with you, always.")
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    args = parse_args()
    my_dir = Path(args.dir)
    try:
        my_dir.mkdir(exist_ok=True)
        print(f"Directory {args.dir} created.")
        logging.info(f"Directory: {my_dir}")
    except FileExistsError:
        print(f"Directory {args.dir} already exists.")

    while True:
        file_name = time.strftime("%Y-%m-%d_%H-%M-%S") + ".png"

        try:
            screen_width, screen_height = pyautogui.size()
            logging.info(
                f"Capturing screen: {screen_width}x{screen_height}. Multi-monitor setups may need manual cropping."
            )

            # pyautogui.screenshot() captures the primary monitor by default.
            pyautogui.screenshot(my_dir.joinpath(file_name))
            print(f"Screenshot saved: {file_name}")
            # Inside the loop:
            logging.info(f"Screenshot saved: {file_name}")
        except Exception as e:
            print(f"Failed to capture screenshot: {e}")

        time.sleep(DEFAULT_TIME_BETWEEN_SCREENSHOTS)


if __name__ == "__main__":
    main()
