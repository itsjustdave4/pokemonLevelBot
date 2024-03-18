import pyautogui
import time


def walk_left() -> None:
    pyautogui.keyDown("Left")
    pyautogui.keyUp("Left")
    time.sleep(1)


def walk_right() -> None:
    pyautogui.keyDown("Right")
    pyautogui.keyUp("Right")
    time.sleep(1)


def press_a() -> None:
    pyautogui.keyDown("a")
    pyautogui.keyUp("a")