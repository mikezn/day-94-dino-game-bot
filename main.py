import pygetwindow as gw
import time
import pyautogui
import PIL
import sys

WATCH_CACTUS_PIXEL_POS = (390, 240)
WATCH_BIRD_PIXEL_POS = (390, 207)
GAME_OVER_PIXEL_1 = (470, 200)
GAME_OVER_PIXEL_2 = (497, 225)
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

    pixel_main = pyautogui.pixel(WATCH_CACTUS_PIXEL_POS[0] + get_window_loc()[0], WATCH_CACTUS_PIXEL_POS[1] + get_window_loc()[1])
    pyautogui.press("space")
    while True:

        pixel_cactus_compare = pyautogui.pixel(WATCH_CACTUS_PIXEL_POS[0] + get_window_loc()[0], WATCH_CACTUS_PIXEL_POS[1] + get_window_loc()[1])
        pixel_bird_compare = pyautogui.pixel(WATCH_BIRD_PIXEL_POS[0] + get_window_loc()[0], WATCH_BIRD_PIXEL_POS[1] + get_window_loc()[1])
        pixel_game_over_1 = pyautogui.pixel(GAME_OVER_PIXEL_1[0] + get_window_loc()[0], GAME_OVER_PIXEL_1[1] + get_window_loc()[1])
        pixel_game_over_2 = pyautogui.pixel(GAME_OVER_PIXEL_2[0] + get_window_loc()[0], GAME_OVER_PIXEL_2[1] + get_window_loc()[1])
        print(pixel_main)
        print(pixel_cactus_compare)
        print(get_window_loc()[0], get_window_loc()[1])

        # detect cactus
        if pixel_main != pixel_cactus_compare:
            pyautogui.press("space")
            print("CACTUS")
            print(pixel_cactus_compare)

        # detect bird
        if pixel_main != pixel_bird_compare:
            pyautogui.press("down")
            print("BIRD")
            print(pixel_bird_compare)


        if pixel_game_over_1 != pixel_main and pixel_game_over_2 != pixel_main:
            print("GAME OVER")
            break
        time.sleep(0.005)

if __name__ == "__main__":
    main()