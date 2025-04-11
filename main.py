import pygetwindow as gw
import time
import pyautogui
import PIL
import sys

WATCH_PIXEL_POS = (390, 240)
GAME_OVER_PIXEL_1 = (525, 325)
GAME_OVER_PIXEL_2 = (548, 325)
WINDOW_TITLE = 'dino game'
pixel_main = None

def game_ready() -> bool:
    windows = gw.getWindowsWithTitle(WINDOW_TITLE)

    if not windows:
        print("Chrome window not found.")
        return False

    chrome = windows[0]
    chrome.activate()  # Brings to front
    time.sleep(1)  # Give time to focus
    print(f"Window dimensions: {chrome.left}, {chrome.top}, {chrome.width}, {chrome.height}")
    return True

def get_window_loc() -> tuple:
    windows = gw.getWindowsWithTitle(WINDOW_TITLE)
    chrome = windows[0]
    return chrome.left, chrome.top

def main() -> None:
    global pixel_main
    if not game_ready():
        sys.exit()

    pixel_main = pyautogui.pixel(WATCH_PIXEL_POS[0] + get_window_loc()[0], WATCH_PIXEL_POS[1] + get_window_loc()[1])
    while True:

        pixel_compare = pyautogui.pixel(WATCH_PIXEL_POS[0] + get_window_loc()[0], WATCH_PIXEL_POS[1] + get_window_loc()[1])
        pixel_game_over_1 = pyautogui.pixel(GAME_OVER_PIXEL_1[0] + get_window_loc()[0], GAME_OVER_PIXEL_1[1] + get_window_loc()[1])
        pixel_game_over_2 = pyautogui.pixel(GAME_OVER_PIXEL_2[0] + get_window_loc()[0], GAME_OVER_PIXEL_2[1] + get_window_loc()[1])
        print(pixel_main)
        print(pixel_compare)
        print(WATCH_PIXEL_POS[0] + get_window_loc()[0], WATCH_PIXEL_POS[1] + get_window_loc()[1])

        if pixel_main != pixel_compare:
            pyautogui.press("space")
            print("DIFFERENT")
            print(pixel_compare)

        if pixel_game_over_1 != pixel_main and pixel_game_over_2 != pixel_main:
            print("GAME OVER")
            break
        time.sleep(0.005)

if __name__ == "__main__":
    main()