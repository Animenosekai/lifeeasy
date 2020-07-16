#####                                       LIFEEASY
#####
##### © Anime no Sekai - 2020
##### for Python 3
#####

## IMPORTS
import subprocess
import os
import shutil
import threading
import time
import datetime
import platform
import sys
import base64
from io import BytesIO
import json

# imports from pip
import requests
import psutil
import imagehash
from PIL import Image, ImageEnhance, ImageOps
import numpy as np

#VARIABLES
stop_displaying = False
multi_thread_display_waiting_time = 2
title = 'Loading'
body = []

## SAME AS TIME.SLEEP()
def sleep(seconds):
    """
    Blocks the function/Waits for a given number of second before resuming the function. (> int)
    """
    try:
        time.sleep(seconds)
        return seconds
    except:
        return 1

## SAME AS CLEAR COMMAND IN BASH
def clear():
    """
    Clears the console. (> int)
    Returns 0 if succeded, 1 if failed. (> int)
    """
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        return 0
    except:
        return 1

## CHANGE WORKING DIR
def change_working_dir(new_dir):
    """
    Changes the working directory.\n
    Returns the new working directory if succeded, 1 if failed. (> str/int)
    """
    try:
        os.chdir(new_dir)
        return new_dir
    except:
        return 1

def working_dir():
    """
    Returns the working directory. (> string)
    """
    return os.getcwd()

## COMMANDS
def command_output(commands, capture_errors=True, hide_error=False, shell=False, universal_newlines=True):
    """
    Executes a command and returns the output of the command. (> mostly string)
    """
    if capture_errors:
        stderr_var = subprocess.STDOUT
    elif hide_error:
        stderr_var = subprocess.DEVNULL
    else:
        stderr_var = None
    if type(commands) == type(['hey', 'hey']):
        result = subprocess.check_output(commands, universal_newlines=universal_newlines, shell=shell, stderr=stderr_var)
        return result
    elif type(commands) == type('hey hey'):
        new_commands = commands.split(' ')
        result = subprocess.check_output(new_commands, universal_newlines=universal_newlines, shell=shell, stderr=stderr_var)
        return result
    else:
        return 'error'

def command(command, hide_output=False, hide_error=False, shell=False):
    """
    Executes a command and returns the response code. (> mostly int)
    """
    if type(command) == type(['hey', 'hey']):
        if hide_output:
            if hide_error:
                result = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=shell)
                return result
            else:
                result = subprocess.call(command, stdout=subprocess.DEVNULL, shell=shell)
                return result
        else:
            if hide_error:
                result = subprocess.call(command, stderr=subprocess.DEVNULL, shell=shell)
                return result
            else:
                result = subprocess.call(command, shell=shell)
                return result
    elif type(command) == type('hey hey'):
        commands = command.split(' ')
        if hide_output:
            if hide_error:
                result = subprocess.call(commands, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=shell)
                return result
            else:
                result = subprocess.call(commands, stdout=subprocess.DEVNULL, shell=shell)
                return result
        else:
            if hide_error:
                result = subprocess.call(commands, stderr=subprocess.DEVNULL, shell=shell)
                return result
            else:
                result = subprocess.call(commands, shell=shell)
                return result
    else:
        return 1

def pip_install(packages_to_install, upgrade=False, hide_output=False, hide_error=False):
    """
    Install the given PyPi (pip) packages.
    """
    list_of_packages = ''
    try:
        if type(packages_to_install) == type(['hey', 'hey']):
            for package in packages_to_install:
                list_of_packages = ' ' + package
        elif type(packages_to_install) == type('hey hey'):
            list_of_packages = packages_to_install
        if list_of_packages != '':
            if upgrade:
                result = command('pip install ' + list_of_packages + ' --upgrade', hide_output=hide_output, hide_error=hide_error)
                return result
            else:
                result = command('pip install ' + list_of_packages, hide_output=hide_output, hide_error=hide_error)
                return result
        else:
            return -2
    except:
        return -1

def ping(domain, number_of_pings=1, raw=False):
    """
    Pings a server for the specified number of times and returns its minimum, average and maximum latency (in ms).\n

    Returns a dictionnary with the minimum, average and maximum latency (in ms).
    """
    try:
        if system_name() == 'nt':
            ping_results = command_output('ping -n ' + str(number_of_pings) + ' ' + str(domain))
            results = {}
            min_avg_max_results_console = ping_results.split('\n')[6+number_of_pings].split(', ')
            minimum = min_avg_max_results_console[0].split(' = ')[1].replace('ms', '')
            maximum = min_avg_max_results_console[1].split(' = ')[1].replace('ms', '')
            average = min_avg_max_results_console[2].split(' = ')[1].replace('ms', '')
            results['minimum'] = minimum
            results['average'] = average
            results['maximum'] = maximum
            if raw:
                results['system'] = system()
                results['system_name'] = system_name()
                results['ping_results'] = ping_results
                results['min_avg_max_results_console'] = min_avg_max_results_console
        else:
            results = {}
            ping_results = command_output('ping ' + str(domain) + ' -c ' + str(number_of_pings))
            ping_results_list = str(ping_results).split('\n')
            min_avg_max_results_console_raw = ping_results_list[4 + number_of_pings]
            min_avg_max_results_console = min_avg_max_results_console_raw.split(' ')[3]
            min_avg_max = min_avg_max_results_console.split('/')
            minimum = min_avg_max[0]
            average = min_avg_max[1]
            maximum = min_avg_max[2]
            results['minimum'] = minimum
            results['average'] = average
            results['maximum'] = maximum
            if raw:
                results['system'] = system()
                results['system_name'] = system_name()
                results['ping_results'] = ping_results
                results['ping_results_list'] = ping_results_list
                results['min_avg_max_results_console_raw'] = min_avg_max_results_console_raw
                results['min_avg_max_results_console'] = min_avg_max_results_console
                results['min_avg_max'] = min_avg_max
    except:
        results = {}
        results['system'] = system()
        results['system_name'] = system_name()
        results['timestamp'] = timing()
        results['error'] = 'Results not available.'
        results['details'] = 'The process returned a non-zero exit status code. This might come from a server which is down, a request which timed out or an incorrect domain.'
        if system_name() == 'nt':
            results['try'] = 'Try to execute "ping -n ' + str(number_of_pings) + ' ' + str(domain) 
        else:
            results['try'] = 'Try to execute "ping -c ' + str(number_of_pings) + ' ' + str(domain)
        results['if'] = 'If it did work in your command-line/terminal then it might be a bug with lifeeasy, please go to the GitHub repository and create an issue.'
        results['github'] = 'https://github.com/Animenosekai/lifeeasy'
    return results


## MAKE HTTP REQUESTS
def request(url, method='get', parameters=None, data=None, headers=None, json_body=None):
    """
    Makes an HTTP request.\n
    This function needs at least an url.\n
    Returns a value of type <Response>\n
    See the requests module documentation to learn more about this response type.
    """
    if method.lower() == 'get':
        r = requests.get(url=url, params=parameters, headers=headers)
        return r
    elif method.lower() == 'post':
        r = requests.post(url=url, data=data, json=json_body, headers=headers)
        return r
    elif method.lower() == 'delete':
        r = requests.delete(url=url, headers=headers)
        return r
    elif method.lower() == 'patch':
        r = requests.patch(url=url, data=data, headers=headers, json=json_body)
        return r
    elif method.lower() == 'put':
        r = requests.put(url=url, data=data, headers=headers, json=json_body)
        return r
    elif method.lower() == 'head':
        r = requests.head(url=url)
        return r
    elif method.lower() == 'options':
        r = requests.options(url=url)
        return r
    else:
        return "Sorry but this HTTP Request method is not available yet."

def request_statuscode(url, method='get', parameters=None, data=None, headers=None, json_body=None):
    """
    Makes an HTTP request and returns its status code. (> int)\n
    This function needs at least an url.
    """
    if method.lower() == 'get':
        r = requests.get(url=url, params=parameters, headers=headers)
        return r.status_code
    elif method.lower() == 'post':
        r = requests.post(url=url, data=data, json=json_body, headers=headers)
        return r.status_code
    elif method.lower() == 'delete':
        r = requests.delete(url=url, headers=headers)
        return r.status_code
    elif method.lower() == 'patch':
        r = requests.patch(url=url, data=data, headers=headers, json=json_body)
        return r.status_code
    elif method.lower() == 'put':
        r = requests.put(url=url, data=data, headers=headers, json=json_body)
        return r.status_code
    elif method.lower() == 'head':
        r = requests.head(url=url)
        return r.status_code
    elif method.lower() == 'options':
        r = requests.options(url=url)
        return r.status_code
    else:
        return "Sorry but this HTTP Request method is not available yet."

## DATE AND TIME

# TODAY'S DATE
def today():
    """
    Returns the current date. (> string)
    """
    today = datetime.date.today()
    return str(today)

def today_raw():
    """
    Returns the current date as a datetime object (> datetime).
    """
    return datetime.date.today()

# CURRENT TIME
def current_time():
    """
    Returns the current time with the format HOURs:MINUTEs:SECONDs (> string)
    """
    now = datetime.datetime.now()
    time_var = now.strftime("%H:%M:%S")
    return time_var

def current_time_raw():
    """
    Returns the current time as a datetime object (> datetime)
    """
    return datetime.datetime.now()

def timing():
    """
    Returns the current time in seconds since 1970.
    """
    return time.time()

def process_time():
    """
    Returns the time since the beginning of the process.
    """
    return time.process_time()

def pid():
    """
    Returns the PID (process identifier) of the current process (python process).

    > Might, for example, differ in the same python script if using multiprocessing.
    """
    return os.getpid()

# SYSTEM TIMEZONE
def timezone():
    """
    Returns the timezone of the system. (> string)
    """
    return time.strftime("%Z", time.gmtime())

def hours_from_greenwich():
    """
    Returns the number of hours between greenwitch and the computer. (> string)\n
    The string is formatted following this format: < + or - > and < two digit integer >
    """
    hours = time.strftime("%z", time.gmtime())
    return hours[:3]

## DISPLAY ACTIONS
def display_action(action_to_display, times=3, delay=0.2):
    """
    Used to display an action (three dots will be animated after your message)\n
    Warning: this is a blocking function, which means the program will only continue when the message disappear.\n
    To display a message with a non-blocking function, try display().

    > Returns 0 when done (> int)
    """
    for _ in range(times):
        #clear()
        print(action_to_display + ".", end="\r")
        sleep(delay)
        #clear()
        print(action_to_display + "..", end="\r")
        sleep(delay)
        #clear()
        print(action_to_display + "...", end="\r")
        sleep(delay)
        clear()
    return 0


## DISPLAY IN ANOTHER THREAD

# SETTING VARIABLES
def display_title(title_string):
    """
    Sets the title for the message to be displayed with display()
    """
    global title
    if type(title_string) == type('Hey hey'):
        title = title_string
        return title
    else:
        return f'Error: unsupported argument type {type(title_string)}'

def display_body(body_list):
    """
    Sets the body for the message to be displayed with display()\n
    The body needs to be a list with each element of the list being a line.
    """
    global body
    if type(body_list) == type(['hey', 'hey']):
        body = body_list
        return body
    elif type(body_list) == type('Hey hey'):
        body = [body_list]
        return body
    else:
        return f'Error: non supported argument type {type(body_list)}'        

def display(wait=2, delay=0.1):
    """
    Displays a message with his title (set with the display_title() function) and his body (set with the display_body() function)\n
    This message will be displayed in another thread and therefore will be non-blocking (code after this function will continue running normally)\n
    (> string if error)
    """
    global multi_thread_display_waiting_time
    multi_thread_display_waiting_time = wait
    if not stop_displaying:
        for number in range(len(title) + 1):
            clear()
            display_title_var = ''
            for i in range(number):
                display_title_var = display_title_var + title[i]
            print(display_title_var)
            print('')
            for line in body:
                print(line)
            sleep(delay)
        if not stop_displaying:
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
    if not stop_displaying:
        stop_displaying = True
        sleep(multi_thread_display_waiting_time)
        stop_displaying = False



## FILE ACTIONS

# MOVING A FILE
def move_file(origin, destination):
    """
    Moves a given file to a given destination (you can use filecenter too) (> string)
    """
    correct_path_of_origin = origin
    correct_path_of_destination = destination
    indexes_of_slash = [i for i, ltr in enumerate(origin) if ltr == "\\"]
    number_of_iterations = 0
    for index in indexes_of_slash:
        character_after_slash = origin[index + 1 - number_of_iterations]
        #print(character_after_slash)
        if character_after_slash == ' ' or character_after_slash == '/':
            correct_path_of_origin = origin[:index - number_of_iterations] + origin[index + 1 - number_of_iterations:]
            number_of_iterations += 1
    indexes_of_slash = [i for i, ltr in enumerate(destination) if ltr == "\\"]
    number_of_iterations = 0
    for index in indexes_of_slash:
        character_after_slash = destination[index + 1 - number_of_iterations]
        #print(character_after_slash)
        if character_after_slash == ' ' or character_after_slash == '/':
            correct_path_of_destination = destination[:index - number_of_iterations] + destination[index + 1 - number_of_iterations:]
            number_of_iterations += 1
    try:
        shutil.move(correct_path_of_origin, correct_path_of_destination)
        return correct_path_of_destination
    except:
        return 1

# DELETING A FILE
def delete_file(file):
    """
    Deletes a given file (you can use filecenter too) (> int)
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
def open_file(file):
    """
    Opens a given file (you can use filecenter too) (> int)
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

def make_dir(path_of_new_dir):
    """
    Makes a directory at the given path. (> str)
    """
    try:
        os.makedirs(path_of_new_dir)
        return path_of_new_dir
    except:
        return 'Error while making the new folder'

### WRITING A TEXT FILE

def write_file(file_title, text, destination=None, append=False):
    """
    To write a text file.\n
    Takes 3 arguments: file_title, text and destination(optional)\n
    Returns an integer (0 if success, 1 if text isn't in the right format)
    """
    if destination is None:
        if not append:
            writing_file = open(file_title, 'w+')
        else:
            writing_file = open(file_title, 'a+')
        if type(text) == type('Example of string'):
            writing_file.write(text)
        elif type(text) == type(['Example', 'of', 'list']):
            for line in text:
                writing_file.write(line + '\n')
        else:
            return 1
        writing_file.close()
        return 0
    else:
        current_working_dir = working_dir()
        change_working_dir(destination)
        if not append:
            writing_file = open(file_title, 'w+')
        else:
            writing_file = open(file_title, 'a+')
        if type(text) == type('Example of string'):
            writing_file.write(text)
        elif type(text) == type(['Example', 'of', 'list']):
            for line in text:
                writing_file.write(line + '\n')
        else:
            return 1
        writing_file.close()
        change_working_dir(current_working_dir)
        return 0

def read_file(file_path):
    """
    Outputs the content of a text file (> string)
    """
    reading_file = open(file_path)
    result = reading_file.read()
    reading_file.close()
    return result

def read_file_line(file_path, lines_to_read=1):
    """
    Outputs a certain, or multiple lines of a text file (> list of string)

    > lines_to_read is an integer or a list of integer which represents the wanted line number.
    """
    results = []
    if type(lines_to_read) == type(1):
        reading_lines = [lines_to_read]
    elif type(lines_to_read) == type([1]):
        reading_lines = lines_to_read
    reading_file = open(file_path)
    for position, line in enumerate(reading_file):
        if position + 1 in reading_lines:
            results.append(line) 
    reading_file.close()
    return results


def find_inside_file(file_path, search_query, whole_document=False):
    """
    Searches through a file for the given search term (search query).

    > The search stops at the first result if whole_document is False (default).
    > Returns a dictionnary or a list of dictionnary.
    """
    file = open(file_path)
    line = file.readline()
    line_no = 1
    if whole_document == False:
        result = {} 
        while line != '' :
            index = line.find(search_query)
            if index != -1:
                result = {'line_number': line_no, 'line': line, 'file': file_path, 'search_term': search_query}
                break
            line = file.readline()
            line_no += 1
        file.close()
        return result
    else:
        results = []
        while line != '':
            index = line.find(search_query)
            if index != -1:
                results.append({'line_number': line_no, 'line': line, 'file': file_path, 'search_term': search_query})
            line = file.readline()
            line_no += 1
        file.close()
        return results



## CONVERTING

# CONVERTING SIZE FROM BYTES
def get_scaled_size(bytes, suffix="B"):
    """
    Credit to PythonCode for this function.\n
    > https://www.thepythoncode.com/article/get-hardware-system-information-python\n
    Scale bytes to its proper format\n
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    (> string)
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# CONVERTING WAVELENGTH TO RGB
def wavelength_to_rgb(wavelength, gamma=0.8):
    '''
    Code by Noah.org\n
    http://www.noah.org/wiki/Wavelength_to_RGB_in_Python\n

    This converts a given wavelength of light to an 
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Returns a list of 3 values (R, G and B) (> list[int])

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
    Returns the sum of the provided list of numbers (> float/int)
    """
    final_result = numbers[0]
    list = numbers
    del list[0]
    for number in list:
        final_result += number
    return final_result

def substract(numbers):
    """
    Returns the substraction of the provided list of numbers (> float/int)
    """
    final_result = numbers[0]
    list = numbers
    del list[0]
    for number in list:
        final_result -= number
    return final_result

def multiply(numbers):
    """
    Returns the multiplication of the provided list of numbers (> float/int)
    """
    final_result = numbers[0]
    list = numbers
    del list[0]
    for number in list:
        final_result = final_result * number
    return final_result

def divide(numbers):
    """
    Returns the division of the provided list of numbers (> float)
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

### OTHER

def fibonacci(n):
    """
    Returns the n th number of the fibonacci sequence. (> int) 
    """
    n = int(n)
    if n == 0:
        result = -1
    elif n == 1 or n == 2:
        result = 1
    elif n > 2:
        sys.setrecursionlimit(10**6)
        memo = [None] * n
        def fib(n,memo):
            if memo[n - 1] != None:
                result = memo[n - 1]
            elif n == 1 or n == 2:
                result = 1
            elif n > 2:
                result = fib(n-1, memo) + fib(n-2, memo)
            else:
                result = "Not a positive number"
            memo[n - 1] = result
            #print(result)
            return(result)
        result = fib(n, memo)
    else:
        result = -2
    return(result)


def json_to_dict(json_string):
    """
    Converts a JSON string to a Python Dictionnary. (> dict)
    """
    try:
        return json.loads(json_string)
    except:
        return {'error': 'An error occured while converting your json string.'}

def dict_to_json_string(dict):
    """
    Converts a Python Dictionnary to a JSON string. (> str)
    """
    try:
        return json.dumps(dict)
    except:
        return 'An error occured while converting your dict.'

def hash_image(image, algorithm='aHash', raw=False):
    """
    Hashes the given image with the chosen algorithm (average hash by default) (> str or ImageHash if raw)\n

    > the image needs to be a PIL (Pillow) instance.
    © Anime no Sekai - 2020
    Project Erina
    """
    image_hash = ''
    if algorithm == 'aHash':
        image_hash = imagehash.average_hash(image) # Needs to be a PIL instance
    elif algorithm == 'cHash':
        image_hash = imagehash.colorhash(image)
    elif algorithm == 'dHash':
        image_hash = imagehash.dhash(image)
    elif algorithm == 'dHash_vertical':
        image_hash = imagehash.dhash_vertical(image)
    elif algorithm == 'pHash':
        image_hash = imagehash.phash(image)
    elif algorithm == 'pHash_simple':
        image_hash = imagehash.phash_simple(image)
    elif algorithm == 'wHash':
        image_hash = imagehash.whash(image)
    if raw:
        return(image_hash)
    else:
        return(str(image_hash))

def hash_image_from_url(image_url, algorithm='aHash', raw=False):
    """
    Hashes the given image from the image url with the chosen algorithm (average hash by default) (> str or ImageHash if raw)\n
    © Anime no Sekai - 2020
    Project Erina
    """
    image_request = request(image_url, 'get')
    downloaded_image = Image.open(BytesIO(image_request.content)) # Open the downloaded image as a PIL Image instance
    return(hash_image(image=downloaded_image, algorithm=algorithm, raw=raw))
    
def hash_image_from_path(image_path, algorithm='aHash', raw=False):
    """
    Hashes the given image from his path with the chosen algorithm (average hash by default) (> str or ImageHash if raw)\n
    © Anime no Sekai - 2020
    Project Erina
    """
    image = Image.open(image_path)
    return(hash_image(image=image, algorithm=algorithm, raw=raw))
    
def hash_string_to_raw_hash(hash_string):
    """
    Converts a Hash String to a raw hash instance (ImageHash Class)

    Useful to make the hamming distance of two hashes for example (HASH1 - HASH2 = Hamming Distance of those two hashes).
    """
    result_hash = imagehash.hex_to_hash(hash_string)
    return result_hash

def base64_from_image(image_path):
    """
    Encodes an image in base64 (> str)
    """
    image = open(image_path, 'rb')
    image_content = image.read()
    image.close()
    return(base64.b64encode(image_content).decode('ascii'))

def string_to_base64(string):
    """
    Encodes a string in base64 (> str)
    """
    string_bytes = string.encode('ascii')
    base64_encoded = base64.b64encode(string_bytes)
    base64string = base64_encoded.decode('ascii')
    return base64string

def string_to_ascii(string):
    """
    Encodes a string in ascii (bytes) (> bytes/ascii)
    """
    string_bytes = string.encode('ascii')
    return string_bytes

def ascii_to_string(ascii_element):
    """
    Encodes an ascii string in string (> str)
    """
    string_decoded = ascii_element.decode('ascii')
    return string_decoded


### IMAGE ENHANCEMENT
def image_brightness_enhancement(image_path, output_name, enhancement_factor=1):
    """
    Enhance the image's brightness by the given factor.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        enhancer = ImageEnhance.Brightness(original_image)
        enhanced = enhancer.enhance(enhancement_factor)
        enhanced.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

def image_contrast_enhancement(image_path, output_name, enhancement_factor=1):
    """
    Enhance the image's contrast by the given factor.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        enhancer = ImageEnhance.Contrast(original_image)
        enhanced = enhancer.enhance(enhancement_factor)
        enhanced.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

def image_color_enhancement(image_path, output_name, enhancement_factor=1):
    """
    Enhance the image's color by the given factor.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        enhancer = ImageEnhance.Color(original_image)
        enhanced = enhancer.enhance(enhancement_factor)
        enhanced.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1
def image_grasyscale(image_path, output_name):
    """
    Turns the image in a grayscale (no color) image.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        image_grayscale_var = original_image.convert('L')
        image_grayscale_var.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

def image_rgb(image_path, output_name):
    """
    Converts the image in an RGB (color profile) image.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        image_rgb_var = original_image.convert('RGB')
        image_rgb_var.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

def image_cmyk(image_path, output_name):
    """
    Converts the image in an CMYK (color profile) image.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        image_cmyk_var = original_image.convert('CMYK')
        image_cmyk_var.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

def image_resize(image_path, output_name, new_size):
    """
    Resizes the image with the given size.
    > new_size needs to be a tuple of 2 values.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        image_resized = original_image.resize(new_size)
        image_resized.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

def image_resize_with_same_aspect_ratio(image_path, output_name, new_size):
    """
    Resizes the images while keeping the same aspect ratio (the image won't be strectched).
    > new_size needs to be a tuple of 2 values.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        image_thumbnail = original_image.copy()
        image_thumbnail.thumbnail(new_size)
        image_thumbnail.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

def image_crop(image_path, output_name, crop_size):
    """
    Crops the image with the given size.
    > crop_size needs to be a tuple of 4 values.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        image_cropped = original_image.crop(crop_size)
        image_cropped.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

def image_to_jpeg(image_path, output_name, jpeg_quality=100):
    """
    Saves the image as jpeg, with the given quality (compression quality).

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        original_image.save(destination_path + output_name, quality=jpeg_quality)
        return destination_path + output_name
    except:
        return 1

def image_watermark(image_path, output_name, watermark_path):
    """
    Adds a watermark at the bottom right of the image.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        watermark = Image.open(watermark_path)
        watermarked = original_image.copy()
        position = ((watermarked.width - watermark.width), (watermarked.height - watermark.height))
        watermarked.paste(watermark, position, watermark)
        watermarked.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

def image_invert(image_path, output_name):
    """
    Inverts the image colors.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        image_inverted = ImageOps.invert(original_image)
        image_inverted.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

def _givenoisy(noise_typ, image):
    '''
    ** INTERNAL FUNCTION **
    
    Parameters
    ----------
    image : ndarray
        Input image data. Will be converted to float.
    mode : str
        One of the following strings, selecting the type of noise to add:

        'gauss'     Gaussian-distributed additive noise.
        'poisson'   Poisson-distributed noise generated from the data.
        's&p'       Replaces random pixels with 0 or 1.
        'speckle'   Multiplicative noise using out = image + n*image,where
                    n is uniform noise with specified mean & variance.

    By Shubham Pachori\n
    > https://stackoverflow.com/questions/22937589/how-to-add-noise-gaussian-salt-and-pepper-etc-to-image-in-python-with-opencv
    '''
    if noise_typ == "gauss":
        row,col,ch= image.shape
        mean = 0
        var = 0.1
        sigma = var**0.5
        gauss = np.random.normal(mean,sigma,(row,col,ch))
        gauss = gauss.reshape(row,col,ch)
        noisy = image + gauss
        return noisy
    elif noise_typ == "s&p":
        row,col,ch = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
                for i in image.shape]
        out[coords] = 1

        # Pepper mode
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                for i in image.shape]
        out[coords] = 0
        return out
    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy
    elif noise_typ =="speckle":
        row,col,ch = image.shape
        gauss = np.random.randn(row,col,ch)
        gauss = gauss.reshape(row,col,ch)        
        noisy = image + image * gauss
        return noisy

def image_gaussian_noise(image_path, output_name):
    """
    Adds gaussian noise to the image.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        numpy_array_image = np.asarray(original_image)
        gaussian_array = _givenoisy('gauss', numpy_array_image)
        gaussian = Image.fromarray((gaussian_array * 255).astype(np.uint8))
        gaussian.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

def image_salt_and_pepper_noise(image_path, output_name):
    """
    Adds salt and pepper noise the image.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        numpy_array_image = np.asarray(original_image)
        salt_and_pepper_array = _givenoisy('s&p', numpy_array_image)
        salt_and_pepper = Image.fromarray((salt_and_pepper_array * 255).astype(np.uint8))
        salt_and_pepper.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

def image_poisson_noise(image_path, output_name):
    """
    Adds poisson noise to the image.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        numpy_array_image = np.asarray(original_image)
        poisson_array = _givenoisy('poisson', numpy_array_image)
        poisson = Image.fromarray((poisson_array * 255).astype(np.uint8))
        poisson.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

def image_speckle_noise(image_path, output_name):
    """
    Adds speckle noise to the image.

    Returns the path of the new file if success, 1 if error (> str/int)
    """
    try:
        filename = os.path.basename(image_path)
        destination_path = image_path[:-len(filename)]
        original_image = Image.open(image_path)
        numpy_array_image = np.asarray(original_image)
        speckle_array = _givenoisy('speckle', numpy_array_image)
        speckle = Image.fromarray((speckle_array * 255).astype(np.uint8))
        speckle.save(destination_path + output_name)
        return destination_path + output_name
    except:
        return 1

## SYSTEM AND HARDWARE INFO

def system():
    """
    Returns the system name (> string)
    """
    return platform.uname().system

def system_name():
    """
    Returns the system name from os.name, generally 'nt' is Windows, 'Darwin' is macOS (> string)
    """
    return os.name

def node():
    """
    Returns the node name (> string)
    """
    return platform.uname().node

def release():
    """
    Returns the system release name (> string)
    """
    return platform.uname().release

def version():
    """
    Returns the system version (> string)
    """
    return platform.uname().version

def machine():
    """
    Returns the machine name (> string)
    """
    return platform.uname().machine

def processor():
    """
    Returns the processor (CPU) name (> string)
    """
    return platform.uname().processor

def boot_time():
    """
    Returns the boot time with the format YEAR/MONTH/DAY HOUR:MIN:SECOND (> string)
    """
    boot_time_timestamp_var = psutil.boot_time()
    bt = datetime.datetime.fromtimestamp(boot_time_timestamp_var)
    return f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"

def boot_time_timestamp():
    """
    Returns the boot time expressed in seconds (> int)
    """
    return psutil.boot_time()

def number_of_physical_cores():
    """
    Returns the number of physical CPU cores (> int)
    """
    return psutil.cpu_count(logical=False)

def number_of_cores():
    """
    Returns the total number of CPU cores (> int)
    """
    return psutil.cpu_count(logical=True)

def cpu_max_frequency():
    """
    Returns the processor maximum frequency, in Mhz (> int)
    """
    return psutil.cpu_freq().max

def cpu_min_frequency():
    """
    Returns the processor minimum frequency, in Mhz (> int)
    """
    return psutil.cpu_freq().min

def cpu_current_frequency():
    """
    Returns the current processor frequency, in Mhz (> int)
    """
    return psutil.cpu_freq().current

def cpu_usage_per_core():
    """
    Returns the dict of the percent of processor usage for each core (> dict) 
    """
    usage = {}
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        usage["Core " + str(i)] = percentage
    return usage

def cpu_usage():
    """
    Returns the processor usage in percentage (> int)
    """
    return psutil.cpu_percent()

def total_ram():
    """
    Returns the total RAM installed, in a readeable way (> string)
    """
    return get_scaled_size(psutil.virtual_memory().total)

def available_ram():
    """
    Returns the available RAM, in a readeable way (> string)
    """
    return get_scaled_size(psutil.virtual_memory().available)

def used_ram():
    """
    Returns the used RAM, in a readeable way (> string)
    """
    return get_scaled_size(psutil.virtual_memory().used)

def used_ram_percentage():
    """
    Returns the used RAM in percentage (> int)
    """
    return psutil.virtual_memory().percent

def available_ram_raw():
    """
    Returns the available RAM (> int)
    """
    return psutil.swap_memory().free

def total_ram_raw():
    """
    Returns the total RAM installed (> int)
    """
    return psutil.swap_memory().total

def used_ram_raw():
    """
    Returns the used RAM (> int)
    """
    return psutil.swap_memory().used


def total_swap_memory():
    """
    Returns the SWAP memory if available, in a readeabl way (> string)
    """
    return get_scaled_size(psutil.swap_memory().total)

def free_swap_memory():
    """
    Returns the free SWAP memory if available, in a readeable way (> string)
    """
    return get_scaled_size(psutil.swap_memory().free)

def used_swap_memory():
    """
    Returns the used SWAP memory if available, in a readeable way (> string)
    """
    return get_scaled_size(psutil.swap_memory().used)

def used_swap_memory_percentage():
    """
    Returns the used SWAP memory in percentage if available (> int)
    """
    return psutil.swap_memory().percent

def free_swap_memory_raw():
    """
    Returns the free SWAP memory if available (> int)
    """
    return psutil.swap_memory().free

def total_swap_memory_raw():
    """
    Returns the total SWAP memory if available (> int)
    """
    return psutil.swap_memory().total

def used_swap_memory_raw():
    """
    Returns the used SWAP memory if available (> int)
    """
    return psutil.swap_memory().used


def disks_info():
    """
    Returns a dict of infos for each disks (> dict)
    """
    partition_infos = {}
    results = {}
    partitions = psutil.disk_partitions()
    for partition in partitions: 
        partition_infos["mountpoint"] = partition.mountpoint 
        partition_infos["filesystem_type"] = partition.fstype 
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            results[partition.device] = partition_infos
            continue
        partition_infos["total_size"] = get_scaled_size(partition_usage.total)
        partition_infos['total_size_raw'] = partition_usage.total
        partition_infos["used_space"] = get_scaled_size(partition_usage.used)
        partition_infos['used_space_raw'] = partition_usage.used
        partition_infos["free_space"] = get_scaled_size(partition_usage.free)
        partition_infos['free_space_raw'] = partition_usage.free
        partition_infos["space_percentage"] = partition_usage.percent
        
        results[partition.device] = partition_infos
    return results

def disk_info():
    """
    Same as disks_info()
    """
    return disks_info()

def disks_infos():
    """
    Same as disks_info()
    """
    return disks_info()

def disk_infos():
    """
    Same as disks_info()
    """
    return disks_info()

def disk_total_read_raw():
    """
    Returns the total amount of data read for the startup disk in bytes (> int)
    """
    return psutil.disk_io_counters().read_bytes

def disk_total_write_raw():
    """
    Returns the total amount of data written for the startup disk in bytes (> int)
    """
    return psutil.disk_io_counters().write_bytes

def disk_total_read():
    """
    Returns the total amount of data read for the startup disk in a readeable format (> string)
    """
    return get_scaled_size(psutil.disk_io_counters().read_bytes)

def disk_total_write():
    """
    Returns the total amount of data written for the startup disk in a readeable format (> string)
    """
    return get_scaled_size(psutil.disk_io_counters().write_bytes)

def ip_address():
    """
    Returns the IP Address (> string)
    """
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for _, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                if f"{address.broadcast}" != "None":
                    return(f"{address.address}")

def number_of_network_interfaces():
    """
    Returns the number of network interfaces (> int)
    """
    number = 0
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for _, interface_addresses in if_addrs.items():
        for _ in interface_addresses:
            number += 1
    return number

def net_total_sent():
    """
    Returns the total amount of data sent over the network (> string)
    """
    return get_scaled_size(psutil.net_io_counters().bytes_sent)
                
def net_total_received():
    """
    Returns the total amount of data received over the network (> string)
    """
    return get_scaled_size(psutil.net_io_counters().bytes_recv)

def net_total_sent_raw():
    """
    Returns the total amount of data sent over the network (in bytes) (> int)
    """
    return psutil.net_io_counters().bytes_sent
                
def net_total_received_raw():
    """
    Returns the total amount of data received over the network (in bytes) (> int)
    """
    return psutil.net_io_counters().bytes_recv

def network_interfaces():
    """
    Returns the IP Addresss/MAC address, Netmask and Brodcast IP/MAC for each network interfaces. (> dict)
    """
    # NETWORK INTERFACES DETAILS
    network_interfaces_var = {}
    try:
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                if str(address.family) == 'AddressFamily.AF_INET':
                    network_interfaces_var[interface_name] = {
                        'ip': address.address,
                        'netmask': address.netmask,
                        'broadcast_ip': address.broadcast
                    }
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    network_interfaces_var[interface_name] = {
                        'mac': address.address,
                        'netmask': address.nNetmask,
                        'broadcast_mac': address.broadcast
                    }
    except:
        network_interfaces_var = {'status': 'error'}
    return network_interfaces_var