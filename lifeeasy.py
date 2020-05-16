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
import datetime
import platform

# imports from pip
import requests
import psutil

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

## CHANGE WORKING DIR
def change_working_dir(new_dir):
    try:
        os.chdir(new_dir)
        return 0
    except:
        return 1

def working_dir():
    return os.getcwd()

## COMMANDS
def command_output(command_list):
    result = subprocess.check_output(command, universal_newlines=True)
    return result

def command(command):
    result = os.system(command)
    return result

## MAKE HTTP REQUESTS
def request(url, type, parameters=None, data=None, headers=None, json_body=None):
    if type.lower() == 'get':
        r = requests.get(url=url, params=parameters, headers=headers)
        return r
    elif type.lower() == 'post':
        r = requests.post(url=url, data=data, json=json_body, headers=headers)
        return r
    else:
        return "Sorry but this HTTP Request Type is not available yet."


## DATE AND TIME

# TODAY'S DATE
def today():
    today = datetime.date.today()
    return str(today)

# CURRENT TIME
def current_time():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    return time

# SYSTEM TIMEZONE
def timezone():
    return time.strftime("%Z", time.gmtime())

def hours_from_greenwich():
    hours = time.strftime("%z", time.gmtime())
    return hours[:3]

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
            t.daemon = True
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


## OPERATIONS

# SUM
def sum(numbers):
    final_result = numbers[0]
    list = numbers
    del list[0]
    for number in list:
        final_result += number
    return final_result

def substract(numbers):
    final_result = numbers[0]
    list = numbers
    del list[0]
    for number in list:
        final_result -= number
    return final_result

def multiply(numbers):
    final_result = numbers[0]
    list = numbers
    del list[0]
    for number in list:
        final_result = final_result * number
    return final_result

def divide(numbers):
    final_result = numbers[0]
    list = numbers
    del list[0]
    for number in list:
        if number == 0:
            return "Error: Division by zero"
        else:
            final_result = final_result / number
    return final_result


## SYSTEM AND HARDWARE INFO

def system():
    return platform.uname().system

def node():
    return platform.uname().node

def release():
    return platform.uname().release

def version():
    return platform.uname().version

def machine():
    return platform.uname().machine

def processor():
    return platform.uname().processor

def boot_time():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.datetime.fromtimestamp(boot_time_timestamp)
    return f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"

def number_of_physical_cores():
    return psutil.cpu_count(logical=False)

def number_of_cores():
    return psutil.cpu_count(logical=True)

def cpu_max_frequency():
    return psutil.cpu_freq().max

def cpu_min_frequency():
    return psutil.cpu_freq().min

def cpu_current_frequency():
    return psutil.cpu_freq().current

def cpu_usage_per_core():
    usage = {}
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        usage["core" + i] = percentage
    return usage

def cpu_usage():
    return psutil.cpu_percent()

def total_ram():
    return get_size_from_bytes(psutil.virtual_memory().total)

def available_ram():
    return get_size_from_bytes(psutil.virtual_memory().available)

def used_ram():
    return get_size_from_bytes(psutil.virtual_memory().used)

def used_ram_percentage():
    return psutil.virtual_memory().percent

def total_swap_memory():
    return get_size_from_bytes(psutil.swap_memory().total)

def free_swap_memory():
    return get_size_from_bytes(psutil.swap_memory().free)

def used_swap_memory():
    return get_size_from_bytes(psutil.swap_memory().used)

def used_swap_memory_percentage():
    return get_size_from_bytes(psutil.swap_memory().percent)

def disks_infos():
    partion_infos = {}
    results = {}
    partitions = psutil.disk_partitions()
    for partition in partitions: 
        partion_infos["mountpoint"] = partition.mountpoint 
        partion_infos["filesystem_type"] = partition.fstype 
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            results[partition.device] = partion_infos
            continue
        partion_infos["total_size"] = get_size_from_bytes(partition_usage.total) 
        partion_infos["used_space"] = get_size_from_bytes(partition_usage.used)
        partion_infos["free_space"] = get_size_from_bytes(partition_usage.free)
        partion_infos["space_percentage"] = get_size_from_bytes(partition_usage.percent)
        
        results[partition.device] = partion_infos
    return results

def disk_total_read():
    return get_size_from_bytes(psutil.disk_io_counters().read_bytes)

def disk_total_write():
    return get_size_from_bytes(psutil.disk_io_counters().write_bytes)

def ip_address():
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for _, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                if f"{address.broadcast}" != "None":
                    return(f"{address.address}")

def number_of_network_interfaces():
    number = 0
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for _, interface_addresses in if_addrs.items():
        for _ in interface_addresses:
            number += 1
    return number

def net_total_bytes_sent():
    return get_size_from_bytes(psutil.net_io_counters().bytes_sent)
                
def net_total_bytes_received():
    return get_size_from_bytes(psutil.net_io_counters().bytes_recv)