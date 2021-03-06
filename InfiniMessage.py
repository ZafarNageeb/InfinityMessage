import time
import PySimpleGUI as sg
import pyautogui


def infini_message_main():
    option = str(input("Would you like to iterate a string or a number ? 'number' or 'string': \n-->"))
    while option != "number" and option != "string":
        print("Invalid input, choose a correct option.")
        option = str(input("Would you like to iterate a string or a number ? 'number' or 'string': \n-->"))

    print("\n")
    time_between_output = float(input("Input an input interval in seconds:  \n-->"))
    while time_between_output < 0:
        print("Time can not be less than 0 seconds.")
        time_between_output = float(input("Input an input interval in seconds:  \n-->"))

    print("\n")
    iteration = int(input("How often do you want it to print:  \n-->"))
    while iteration < 0:
        print("Amount to iterate can not be less than 0.")
        iteration = int(input("How often do you want it to print:  \n-->"))

    if option == "number":
        infini_message_numbers(iteration, time_between_output)
    else:
        infini_message_string(iteration, time_between_output)


def infini_message_string(iteration, time_between_output):
    print("\n")
    string_to_print = str(input("What message do you want to output:  \n-->"))
    print("\n")
    print("output commencing in 5 seconds")
    time.sleep(5)
    counter = 0

    while counter < iteration:
        time.sleep(time_between_output)
        pyautogui.typewrite(string_to_print)
        pyautogui.press('enter')
        counter += 1
    print("Program Finished")
    raise SystemExit


def infini_message_numbers(iteration, time_between_output):
    print("\n")
    starting_number = int(input("What will be the first number to output:  \n-->"))
    number = int(starting_number)
    print("\n")
    print("output commencing in 5 seconds")
    time.sleep(5)
    counter = 0

    while counter < iteration:
        time.sleep(time_between_output)
        pyautogui.typewrite(str(number))
        pyautogui.press('enter')
        number += 1
        counter += 1
    print("Program Finished")
    raise SystemExit


if __name__ == "__main__":
    infini_message_main()
