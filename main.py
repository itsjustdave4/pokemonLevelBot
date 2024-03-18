import pyautogui
import controls
import sequence

if __name__ == '__main__':

    i = 0
    while i < 1:
        try:
            controls.walk_left()
            controls.walk_right()
            sequence.encounter()
            try:
                sequence.battle()
            except pyautogui.ImageNotFoundException:
                i = 0
        except pyautogui.ImageNotFoundException:
            controls.press_a()
