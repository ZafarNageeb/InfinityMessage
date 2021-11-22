import time

import pyautogui


def main():
    time_between_messages = float(input("Input an input interval in seconds: "))
    iteration = int(input("How often do you want it to print: "))
    starting_number = (input("What will be the first number to print: "))
    number = int(starting_number)
    time.sleep(5)
    counter = 0

    while counter < iteration:
        time.sleep(time_between_messages)
        pyautogui.typewrite(str(number))
        pyautogui.press('enter')
        number += 1
        counter += 1
    print("Program Finished")
    raise SystemExit


if __name__ == '__main__':
    main()
