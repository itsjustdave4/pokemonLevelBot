import time
import pyautogui

if __name__ == '__main__':

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


    def encounter() -> None:
        pyautogui.locateOnScreen("encounter_start.png", confidence=0.9)
        time.sleep(2)
        pyautogui.keyDown("a")
        pyautogui.keyUp("a")


    def battle() -> None:
        pyautogui.locateOnScreen("battle_menu.png", confidence=0.9)
        pyautogui.keyDown("a")
        pyautogui.keyUp("a")


    i = 0
    while i < 1:
        try:
            walk_left()
            walk_right()
            encounter()
            try:
                battle()
            except:
                i = 0
        except pyautogui.ImageNotFoundException:
            press_a()
            print("No encounter")
