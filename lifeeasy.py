#####                           LIFEEASY
#####
##### © Anime no Sekai - 2020
##### for Python 3
#####


## IMPORTS
import subprocess
import os
import threading
import time

#VARIABLES
stop_displaying = False
multi_thread_display_waiting_time = 2
title = 'Loading'
body = []

## SAME AS TIME.SLEEP()
def sleep(seconds):
    time.sleep(seconds)

## SAME AS CLEAR COMMAND IN BASH
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


## DISPLAY ACTIONS
def display_action(action_to_display, times=3, delay=0.2):
    for _ in range(times-1):
        clear()
        print(action_to_display + ".")
        sleep(delay)
        clear()
        print(action_to_display + "..")
        sleep(delay)
        clear()
        print(action_to_display + "...")
        sleep(delay)


## DISPLAY IN ANOTHER THREAD

# SETTING VARIABLES
def display_title(title_string):
    global title
    title = title_string

def display_body(body_list):
    global body
    body = body_list

def display(wait=2, delay=0.1):
    global multi_thread_display_waiting_time
    multi_thread_display_waiting_time = wait
    if stop_displaying == False:
        for number in range(len(title) + 1):
            clear()
            display_title = ''
            for i in range(number):
                display_title = display_title + title[i]
            print(display_title)
            print('')
            for line in body:
                print(line)
            sleep(delay)
        if stop_displaying == False:
            t = threading.Timer(wait, display, args=[wait, delay])
            t.start()
    else:
        return 'Another instance is already running.'

# STOPPING THE THREAD
def stop_multi_thread_display():
    global stop_displaying
    if stop_displaying == False: 
        stop_displaying = True
        sleep(multi_thread_display_waiting_time)
        stop_displaying = False



## FILE ACTIONS

# MOVING A FILE
def move(origin, destination):
    indexes_of_slash = [i for i, ltr in enumerate(origin) if ltr == "\\"]
    number_of_iterations = 0
    for index in indexes_of_slash:
        character_after_slash = origin[index + 1 - number_of_iterations]
        #print(character_after_slash)
        if character_after_slash == ' ' or character_after_slash == '/':
            origin = origin[:index - number_of_iterations] + origin[index + 1 - number_of_iterations:]
            number_of_iterations += 1
    indexes_of_slash = [i for i, ltr in enumerate(destination) if ltr == "\\"]
    number_of_iterations = 0
    for index in indexes_of_slash:
        character_after_slash = destination[index + 1 - number_of_iterations]
        #print(character_after_slash)
        if character_after_slash == ' ' or character_after_slash == '/':
            destination = destination[:index - number_of_iterations] + destination[index + 1 - number_of_iterations:]
            number_of_iterations += 1
    try:
        shutil.move(correct_path_of_origin, correct_path_of_destination)
        return 0
    except:
        return 1

# DELETING A FILE
def delete(file):
    indexes_of_slash = [i for i, ltr in enumerate(file) if ltr == "\\"]
    number_of_iterations = 0
    for index in indexes_of_slash:
        character_after_slash = file[index + 1 - number_of_iterations]
        #print(character_after_slash)
        if character_after_slash == ' ' or character_after_slash == '/':
            file = file[:index - number_of_iterations] + file[index + 1 - number_of_iterations:]
            number_of_iterations += 1
    if os.path.isdir(file):
        try:
            shutil.rmtree(file)
            return 0
        except:
            return 3
    elif os.path.isfile(file):
        try:
            os.remove(file)
            return 0
        except:
            return 2
    else:
        return 1

# OPENING A FILE
def open(file):
    indexes_of_slash = [i for i, ltr in enumerate(file) if ltr == "\\"]
    number_of_iterations = 0
    for index in indexes_of_slash:
        character_after_slash = file_path[index + 1 - number_of_iterations]
        #print(character_after_slash)
        if character_after_slash == ' ' or character_after_slash == '/':
            file_path = file_path[:index - number_of_iterations] + file_path[index + 1 - number_of_iterations:]
            number_of_iterations += 1
    try:
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', file_path))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(file_path)
        else:                                   # linux variants
            subprocess.call(('xdg-open', file_path))
        return 0
    except:
        return 1


## CONVERTING

# CONVERTING SIZE FROM BYTES
def get_size_from_bytes(bytes, suffix="B"):
    """
    Credit to PythonCode for this function.
    > https://www.thepythoncode.com/article/get-hardware-system-information-python
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
        