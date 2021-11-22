import time

import pyautogui


def main():
    time_between_messages = float(input("Input an input interval in seconds: "))
    iteration = int(input("How often do you want it to print: "))
    string_to_print = (input("What message do you want to print: "))
    time.sleep(5)
    counter = 0

    while counter < iteration:
        time.sleep(time_between_messages)
        pyautogui.typewrite(string_to_print)
        pyautogui.press('enter')
        counter += 1
    print("Program Finished")
    raise SystemExit


if __name__ == '__main__':
    main()
