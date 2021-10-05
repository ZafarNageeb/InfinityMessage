import pyautogui
import time
import tkinter as tk


def main():
    tijd = float(input("Input an input interval in seconds: "))
    iteration = int(input("How often do you want it to print: "))
    stringToPrint = (input("What message do you want to print: "))
    time.sleep(5)
    counter = 0

    while counter < iteration:
        time.sleep(tijd)
        pyautogui.typewrite(stringToPrint)
        pyautogui.press('enter')
        counter += 1
    print("Program Finished")
    raise SystemExit


if __name__ == '__main__':
    main()
