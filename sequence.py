import pyautogui
import time


def encounter() -> None:
    pyautogui.locateOnScreen("encounter_start.png", confidence=0.9)
    time.sleep(2)
    pyautogui.keyDown("a")
    pyautogui.keyUp("a")


def battle() -> None:
    pyautogui.locateOnScreen("battle_menu.png", confidence=0.9)
    pyautogui.keyDown("a")
    pyautogui.keyUp("a")
