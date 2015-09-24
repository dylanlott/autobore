import time
import pyautogui


def draw_circles():
    x, y = pyautogui.position()
    time.sleep(5)
    pyautogui.click()
    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2)
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0.2)
        pyautogui.dragRel(-distance, 0, duration=0.2)
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=0.2)
    return


if __name__ == "__main__":
    draw_circles()
