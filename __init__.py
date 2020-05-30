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
    """
    Blocks the function/Waits for a given number of second before resuming the function.
    """
    time.sleep(seconds)

## SAME AS CLEAR COMMAND IN BASH
def clear():
    """
    Clears the console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

## CHANGE WORKING DIR
def change_working_dir(new_dir):
    """
    Changes the working directory.
    Returns 0 if succeded, 1 if failed.
    """
    try:
        os.chdir(new_dir)
        return 0
    except:
        return 1

def working_dir():
    """
    Returns the working directory.
    """
    return os.getcwd()

## COMMANDS
def command_output(command_list):
    """
    Executes a command and returns the output of the command.
    """
    result = subprocess.check_output(command, universal_newlines=True)
    return result

def command(command):
    """
    Executes a command and returns the response code.
    """
    result = os.system(command)
    return result

## MAKE HTTP REQUESTS
def request(url, type, parameters=None, data=None, headers=None, json_body=None):
    """
    Makes an HTTP request.
    This function needs at least an url and the method (called type here).
    Returns a value of type <Response>
    See the requests module documentation to learn more about this response type.
    """
    if type.lower() == 'get':
        r = requests.get(url=url, params=parameters, headers=headers)
        return r
    elif type.lower() == 'post':
        r = requests.post(url=url, data=data, json=json_body, headers=headers)
        return r
    elif type.lower() == 'delete':
        r = requests.delete(url=url, headers=headers)
        return r
    elif type.lower() == 'patch':
        r = requests.patch(url=url, data=data, headers=headers, json=json_body)
        return r
    elif type.lower() == 'put':
        r = requests.put(url=url, data=data, headers=headers, json=json_body)
        return r
    elif type.lower() == 'head':
        r = requests.head(url=url)
        return r
    elif type.lower() == 'options':
        r = requests.options(url=url)
        return r
    else:
        return "Sorry but this HTTP Request Type is not available yet."


## DATE AND TIME

# TODAY'S DATE
def today():
    """
    Returns the current date.
    """
    today = datetime.date.today()
    return str(today)

# CURRENT TIME
def current_time():
    """
    Returns the current time with the format HOURs:MINUTEs:SECONDs
    """
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    return time

# SYSTEM TIMEZONE
def timezone():
    """
    Returns the timezone of the system.
    """
    return time.strftime("%Z", time.gmtime())

def hours_from_greenwich():
    """
    Returns the number of hours between greenwitch and the computer.
    """
    hours = time.strftime("%z", time.gmtime())
    return hours[:3]

## DISPLAY ACTIONS
def display_action(action_to_display, times=3, delay=0.2):
    """
    Used to display an action (three dots will be animated after your message)
    Warning: this is a blocking function, which means the program will only continue when the message disappear.
    To display a message with a non-blocking function, try display().
    """
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
    """
    Sets the title for the message to be displayed with display()
    """
    global title
    title = title_string

def display_body(body_list):
    """
    Sets the body for the message to be displayed with display()
    The body needs to be a list with each element of the list being a line.
    """
    global body
    body = body_list

def display(wait=2, delay=0.1):
    """
    Displays a message with his title (set with the display_title() function) and his body (set with the display_body() function)
    This message will be displayed in another thread and therefore will be non-blocking (code after this function will continue running normally)
    """
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
def stop_display():
    """
    Stops displaying the multi-threaded status message (if launch through the display() function)
    """
    global stop_displaying
    if stop_displaying == False:
        stop_displaying = True
        sleep(multi_thread_display_waiting_time)
        stop_displaying = False



## FILE ACTIONS

# MOVING A FILE
def move(origin, destination):
    """
    Moves a given file to a given destination (you can use file_info too)
    """
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
    """
    Deletes a given file (you can use file_info too)
    """
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
    """
    Opens a given file (you can use file_info too)
    """
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

# CONVERTING WAVELENGTH TO RGB
def wavelength_to_rgb(wavelength, gamma=0.8):
    '''
    Code by Noah.org
    http://www.noah.org/wiki/Wavelength_to_RGB_in_Python

    This converts a given wavelength of light to an 
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Returns a list of 3 values (R, G and B)

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    '''

    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return [int(R), int(G), int(B)]

## OPERATIONS

# SUM
def sum(numbers):
    """
    Returns the sum of the provided list of numbers
    """
    final_result = numbers[0]
    list = numbers
    del list[0]
    for number in list:
        final_result += number
    return final_result

def substract(numbers):
    """
    Returns the substraction of the provided list of numbers
    """
    final_result = numbers[0]
    list = numbers
    del list[0]
    for number in list:
        final_result -= number
    return final_result

def multiply(numbers):
    """
    Returns the multiplication of the provided list of numbers
    """
    final_result = numbers[0]
    list = numbers
    del list[0]
    for number in list:
        final_result = final_result * number
    return final_result

def divide(numbers):
    """
    Returns the division of the provided list of numbers
    """
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
    """
    Returns the system name
    """
    return platform.uname().system

def node():
    """
    Returns the node name
    """
    return platform.uname().node

def release():
    """
    Returns the system release name
    """
    return platform.uname().release

def version():
    """
    Returns the system version
    """
    return platform.uname().version

def machine():
    """
    Returns the machine name
    """
    return platform.uname().machine

def processor():
    """
    Returns the processor (CPU) name
    """
    return platform.uname().processor

def boot_time():
    """
    Returns the boot time with the format YEAR/MONTH/DAY HOUR:MIN:SECOND
    """
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.datetime.fromtimestamp(boot_time_timestamp)
    return f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"

def number_of_physical_cores():
    """
    Returns the number of physical CPU cores
    """
    return psutil.cpu_count(logical=False)

def number_of_cores():
    """
    Returns the total number of CPU cores
    """
    return psutil.cpu_count(logical=True)

def cpu_max_frequency():
    """
    Returns the processor maximum frequency
    """
    return psutil.cpu_freq().max

def cpu_min_frequency():
    """
    Returns the processor minimum frequency
    """
    return psutil.cpu_freq().min

def cpu_current_frequency():
    """
    Returns the current processor frequency
    """
    return psutil.cpu_freq().current

def cpu_usage_per_core():
    """
    Returns the dict of the percent of processor usage for each core 
    """
    usage = {}
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        usage["core" + i] = percentage
    return usage

def cpu_usage():
    """
    Returns the processor usage in percentage
    """
    return psutil.cpu_percent()

def total_ram():
    """
    Returns the total RAM installed
    """
    return get_size_from_bytes(psutil.virtual_memory().total)

def available_ram():
    """
    Returns the available RAM
    """
    return get_size_from_bytes(psutil.virtual_memory().available)

def used_ram():
    """
    Returns the used RAM
    """
    return get_size_from_bytes(psutil.virtual_memory().used)

def used_ram_percentage():
    """
    Returns the used RAM in percentage
    """
    return psutil.virtual_memory().percent

def total_swap_memory():
    """
    Returns the SWAP memory if available
    """
    return get_size_from_bytes(psutil.swap_memory().total)

def free_swap_memory():
    """
    Returns the free SWAP memory if available
    """
    return get_size_from_bytes(psutil.swap_memory().free)

def used_swap_memory():
    """
    Returns the used SWAP memory if available
    """
    return get_size_from_bytes(psutil.swap_memory().used)

def used_swap_memory_percentage():
    """
    Returns the used SWAP memory in percentage if available
    """
    return get_size_from_bytes(psutil.swap_memory().percent)

def disks_infos():
    """
    Returns the a dict of infos for each disks
    """
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
    """
    Returns the total read for the disk
    """
    return get_size_from_bytes(psutil.disk_io_counters().read_bytes)

def disk_total_write():
    """
    Returns the total write for the disk
    """
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
    """
    Returns the number of network interfaces
    """
    number = 0
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for _, interface_addresses in if_addrs.items():
        for _ in interface_addresses:
            number += 1
    return number

def net_total_bytes_sent():
    """
    Returns the total bytes sent over the network
    """
    return get_size_from_bytes(psutil.net_io_counters().bytes_sent)
                
def net_total_bytes_received():
    """
    Returns the total bytes received over the network
    """
    return get_size_from_bytes(psutil.net_io_counters().bytes_recv)