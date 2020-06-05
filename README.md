# LifeEasy
 
 ### **A quick python toolbox that will let you access various multi-line and multi-imports function with just a single line of code!**
 
[![PyPI version](https://badge.fury.io/py/lifeeasy.svg)](https://pypi.org/project/lifeeasy)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/lifeeasy)](https://pypistats.org/packages/lifeeasy)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/lifeeasy)](https://pypi.org/project/lifeeasy/)
[![PyPI - Status](https://img.shields.io/pypi/status/lifeeasy)](https://pypi.org/project/lifeeasy/)
[![GitHub - License](https://img.shields.io/github/license/Animenosekai/lifeeasy)](https://github.com/Animenosekai/lifeeasy/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues-raw/Animenosekai/lifeeasy)](https://github.com/Animenosekai/lifeeasy/issues)
[![GitHub top language](https://img.shields.io/github/languages/top/Animenosekai/lifeeasy)](https://github.com/Animenosekai/lifeeasy)

## Table of Content
- [Installation](#installation)  
- [What is LifeEasy?](#whatis)
- [Usage](#usage)
   - [Basic](#basic)  
   - [Time Info](#time)
   - [Display Actions](#display)
   - [File Actions](#file)
   - [Calculations](#calculations)
   - [System Info](#system)
   - [Advanced](#advanced)
- [Development](#development) 
- [Legals](#legals)
 
 
<a name="installation"/>

## Installation
You can install this library with **`PIP`**, the Python Package Manager

Simply type `pip install lifeeasy` in your terminal/command-line prompt.

> This library has two third-pary dependencies installed automatically with `pip install lifeeasy`.

<a name="whatis"/>

## What is LifeEasy?
File Center is a simple library to make developers life easier with various of common, everyday functions callable with just one single line of code!.
> You just have to import it to your project! `import filecenter`


<a name="usage"/>

## Usage

<a name="fileactions"/>

### Basic
- **`sleep(time)`**

**Blocks the execution of the program for a certain amount of time**

Arguments:

    seconds: the amount of time to wait (in seconds).

> Returns 0 if success 1 if failed (> integer)

---
- **`clear()`**

**Clears the console.**

Arguments:

    there is no argument to pass.
    
> Returns 0 if success 1 if failed (> integer)

---
- **`change_working_dir(path)`**

**Changes the current working directory/folder.**

Arguments:

    new_dir: the path of the new working directory.

> Returns 0 if success, 1 if failed (> integer)

---
- **`working_dir()`**

**Returns the current working directory/folder.**

Arguments:

    there is no argument.

> Returns the path of the working directory (> string)

---
- **`command_output(command)`**

**Executes a command and returns the output of the command.**

Arguments:

    command: a string of command to be executed.

> Returns the command output/result (> mostly string)

---
- **`command(command)`**

**Executes a command and returns the response code.**

Arguments:

    command: a string of command to be executed.

> Returns the command response code (generally 0 if success) (> integer)

---
- **`request(url, method, parameters, data, headers, json_body)`**

**Makes an HTTP request with the given arguments.**

Arguments:

    url: a string with the url of the request.
    
    method: a string with the http method to use with the request (see below for a list of compatible methods)
    
    parameters (optional): parameters to be sent with a GET request.
    
    data (optional): the data to be sent with the POST, PATCH and PUT request
    
    headers (optional): the headers to be sent with the GET, POST, PATCH, DELETE and PUT request (i.e. the API Key).
    
    json_body (optional): the json body of the request for POST, PATCH and PUT requests.

> Returns a <Response> type value (see the [Requests module documentation]
(https://requests.readthedocs.io/en/master/user/quickstart/#response-content) to learn more about this response type).
 
> Example: `response.text` is the content of the response.
 
> Returns 'Sorry but this HTTP Request Method is not available yet.' if the method isn't available.

---

<a name="time"/>

### Time Information

- **`today()`**

**Gives today's date.**

Arguments:

    there is no argument.

> Returns a string with today's date (> string)

---

- **`current_time()`**

**Gives the current time with the format HH:MM:SS.**

Arguments:

    there is no argument.

> Returns a string with the current time (> string)
---

- **`timezone()`**

**Gives the system timezone.**

Arguments:

    there is no argument.

> Returns a string with the system timezone (> string)

---

- **`hours_from_greenwich()`**

**Gives the number of hours between greenwhich and the system timezone.**

Arguments:

    there is no argument.

> Returns a string with the number of hours from greenwhich (> string)

<a name="display"/>

### Display Actions

- **`display_action(action to display, times, delay)`**

**Shows the string passed with 3 dots animated at the end of it.**

    Warning: this is a blocking function, which means the program will only continue when the message disappear.
    To display a message with a non-blocking function, try display().

Arguments:

    action_to_display: the string to be displayed.

    times (optional, default: 3): the number of times the 3 dots need to be shown.

    delay (optional, default: 0.2): the number of seconds between each dot appearance. 

> Returns nothing.

---

- **`display(wait, delay)`**

**Displays a message in another thread.**

Displays a message with his title (set with the display_title() function) and his body (set with the display_body() function)

This message will be displayed in another thread and therefore will be non-blocking (code after this function will continue running normally)

Ideal for loading screens.

    Warning: print() won't work while this is running as it will constantly clear the console.

Arguments:

    wait (optional, default: 2): the number of times before the console gets cleared (after the message is fully shown).

    delay (optional, default: 0.1): the delay between each character appearance.
    
> Returns nothing or "Another instance is already running." if you already launched another instance of display() without stopping it.


---

- **`display_title(title)`**

**Sets the title for display().**

You should set the title before running display()

Arguments:

    title_string: the string to be displayed as the title for display()

> Returns the given title (> string)

---

- **`display_body(body)`**

**Sets the body for display().**

Arguments:

    body_list: a list of string to be displayed as the body for display(). Each new element in the list means a line break.

> Returns the given body (> list)

---

- **`stop_display()`**

**Stops the display() instance running.**

Arguments:

    there is no argument.

> Returns nothing.
---

<a name="file"/>

### File Actions

- **`move_file(filepath, new_path)`**

**Moves the given file to the provided new path..**

Also available in my file management/info center library for python: `filecenter`

Arguments:

    origin: the path to the file.

    destination: the new path

> Returns 0 if success and 1 if failed (> integer)

---

- **`delete_file(filepath)`**

**Deletes the given file.**

Also available in my file management/info center library for python: `filecenter`

Arguments:

     file: the path of the file

> Returns 0 if success, 1 if failed at getting the file, 2 if failed at deleting a file and 3 if failed at deleting a directory (> integer)


---

- **`open_file(filepath)`**

**Opens the given file in its default software.**

Arguments:

    file: the path to the file.
    
> Returns 0 if success and 1 if failed (> integer)

---

- **`write_file(title, text, destination)`**

**Writes a text file.**

Arguments:

    title: the title (with the extension) of the new text file.
    
    text: the body of the document, if this argument is a list, a line break will be made for each element of the list, if the argument is a string a line break '\n' will need to be written in the string itself.

    destination (default: working dir, optional): the destination of the file (the working directory by default)
    
> Returns 0 if success and 1 if the text argument isn't in the right format (not a list or a string) (> integer)

---

<a name="calculations"/>

### Calculations and Conversions

- **`get_scaled_size(bytes, suffix)`**

**To scale bytes to its proper format.**

Arguments:

    bytes: the number of bytes to convert.
    
    suffix: if you want to change the suffix of the given size.

> Returns a string with the correctly scaled size (> string)

---

- **`wavelength_to_rgb(wavelength)`**

**Converts a given wavelength of light to an RGB value.**

This converts a given wavelength of light to an approximate RGB color value. The wavelength must be given in nanometers in the range from 380 nm through 750 nm (789 THz through 400 THz).


Arguments:

    wavelength: the wavelength of light to convert.

> Returns a list of 3 values R, G and B (> list)

---

- **`sum(numbers)`**

**Makes the sum of the given numbers.**

Arguments:

    numbers: a list of numbers to make the sum of.

> Returns the result of the sum of numbers (> integer/float)

---

- **`substract(numbers)`**

**Makes the substraction of the provided numbers.**

Arguments:

    numbers: a list of numbers to make the substraction of.

> Returns the result of substraction of the provided list of numbers (> integer/float)

---

- **`multiply(numbers)`**

**Multiplies the given numbers.**

Arguments:

    numbers: a list of numbers to multiply.

> Returns the result of the multiplication of the provided list of numbers (> integer/float)

---

- **`division(numbers)`**

**Divide the given numbers between each other.**

Arguments:

    numbers: a list of numbers to divide.

> Returns the result of the division of the provided numbers or "Error: Division by zero" if a division by zero is made (> integer/float)

---

- **`fibonacci(n)`**

**Gives the n th number from the fibonacci sequence.**

*Uses dynamic programming techniques to optimize the calculation time.*

Arguments:

    n: the position of the number you want to get.

> Returns the n th number from the fibonacci sequence (> integer), -1 if you passed a 0, -2 if you passed a negative integer.

---



<a name="system"/>

### System Information

- **`system()`**

**Returns the system name.**

    Example:
    'nt': Windows
    'Darwin': macOS

Arguments:

    there is no argument.

> Returns the system name (> string)

---

- **`node()`**

**Returns the node name.**

Arguments:

    there is no argument.

> Returns the node name (> string)

---

- **`release()`**

**Returns the system release name.**

Arguments:

    there is no argument.

> Returns the system release name (> string)

---

- **`version()`**

**Returns the system version.**

Arguments:

    there is no argument.

> Returns the system version (> string)

---

- **`machine()`**

**Returns the machine name.**

Arguments:

    there is no argument.

> Returns the machine name (> string)

---

- **`processor()`**

**Returns the processor (CPU) name.**

Arguments:

    there is no argument.

> Returns the CPU name (> string)

---

- **`boot_time()`**

**Returns the boot time with the format YY/MM/DD HH:MM:SS.**

Arguments:

    there is no argument.

> Returns the boot time as a string (> string)

---

- **`number_of_physical_cores()`**

**Returns the number of physical CPU cores.**

Arguments:

    there is no argument.

> Returns the number of physical CPU Cores (> integer)

---

- **`number_of_cores()`**

**Returns the number of CPU cores.**

Arguments:

    there is no argument.

> Returns the number of CPU cores (> integer)

---

- **`cpu_max_frequency()`**

**Returns the CPU (processor) maximum frequency.**

Arguments:

    there is no argument.

> Returns the CPU maximum frequency in Mhz (> integer)

---

- **`cpu_min_frequency()`**

**Returns the CPU minimum frequency.**

Arguments:

    there is no argument.

> Returns the CPU minimum frequency in Mhz (> integer)

---

- **`cpu_current_frequency()`**

**Returns the current CPU frequency.**

Arguments:

    there is no argument.

> Returns the current CPU (processor) frequency in Mhz (> integer)

---

- **`cpu_usage_per_core()`**

**Returns the CPU usage for each core.**

Arguments:

    there is no argument.

> Returns a dictionnary with the percentage of processor usage for each core (> dict)

> The dict is formatted following this schema: {'core1': 10, 'core2': 14} with a string as the key and an int/float as the value.

---

- **`cpu_usage()`**

**Returns the current CPU usage in percent.**

Arguments:

    there is no argument.

> Returns the CPU current usage in percent (> float)

---

- **`total_ram()`**

**Returns the total RAM installed.**

Arguments:

    there is no argument.

> Returns the total RAM installed scaled in its proper format (> string)

---

- **`available_ram()`**

**Returns the available RAM.**

Arguments:

    there is no argument.

> Returns the available RAM in its proper format (> string)

---

- **`used_ram()`**

**Returns the used RAM.**

Arguments:

    there is no argument.

> Returns the used RAM in its proper format  (> string)

---

- **`used_ram_percentage()`**

**Returns the used RAM in percent.**

Arguments:

    there is no argument.

> Returns the used RAM in percent (> float)

---

- **`total_swap_memory()`**

**Returns the total SWAP memory.**

Arguments:

    there is no argument.

> Returns the total SWAP memory (if available) in its proper format (> string)

---

- **`free_swap_memory()`**

**Returns the free SWAP memory.**

Arguments:

    there is no argument.

> Returns the free SWAP memory (if available) in its proper format (> string)

---

- **`used_swap_memory()`**

**Returns the used SWAP memory.**

Arguments:

    there is no argument.

> Returns the used SWAP memory (if available) in its proper format (> string)

---

- **`used_swap_memory_percentage()`**

**Returns the used SWAP memory in percent.**

Arguments:

    there is no argument.

> Returns the used SWAP memory in percent (if available) (> float).

---

- **`disks_info()`**

**Returns the installed disks information.**

Arguments:

    there is no argument.

> Returns a dictionnary of infos for each disks mounted (> dict)

> The returned dict is following this schema: {'/dev/disk1s1': {'mountpoint': '/Volumes/アニメの世界', 'filesystem_type': 'exfat', 'total_size': '931.48GB', 'total_size_raw': 1000169537536, 'used_space': '736.89GB', 'used_space_raw': 791230939136, 'free_space': '194.59GB', 'free_space_raw': 208938598400, 'space_percentage': 79.1}

---

- **`disk_total_read()`**

**Returns the startup disk total amount of data read.**

Arguments:

    there is no argument.

> Returns the startup disk total read in a human readeable format (> string)

---

- **`disk_total_write()`**

**Returns the startup disk total amount of data written.**

Arguments:

    there is no argument.

> Returns the startup disk total write in a human readeable format (> string)

---

- **`ip_address()`**

**Returns the current IP Address.**

Arguments:

    there is no argument.

> Returns the an IP address (> string)

---

- **`number_of_network_interfaces()`**

**Returns the number of network interfaces.**

Arguments:

    there is no argument.

> Returns the number of network interfaces (> integer)

---

- **`network_interfaces()`**

**Returns the IP Addresss/MAC address, Netmask and Brodcast IP/MAC for each network interfaces.**

Argument:

    there is no argument.

> Returns a dict with the IP Addresss/MAC address, Netmask and Brodcast IP/MAC for each network interfaces (> dict)

> The returned dict is following this schema: {'en1': {'ip': '0.0.0.0', 'netmask': '0.0.0.0', 'broadcast_ip': '0.0.0.0'}, 'eth0': {'mac': '00:00:00:00:00:00', 'netmask': None, 'broadcast_mac': 'ff:ff:ff:ff:ff:ff'}}

---

- **`net_total_sent()`**

**Returns the total amount of data sent over the network.**

Arguments:

    there is no argument.

> Returns the total amount of data sent over the network in its proper format (> string)

---

- **`net_total_received()`**

**Returns the total amount of data sent over the network.**

Arguments:

    there is no argument.

> Returns the total amount of data received from the network scaled in its proper format (> string)

---


<a name="advanced"/>

### Advanced

---

- **`today_raw()`**

**Returns the current date as a datetime object.**

Arguments:

    there is no argument.

> Returns the current date as a datetime object (> datetime)

---

- **`current_time_raw()`**

**Returns the current time as a datetime object.**

Arguments:

    there is no argument.

> Returns the current time as a datetime object (> datetime)

---

- **`boot_time_timestamp()`**

**Returns the boot time expressed in seconds.**

Arguments:

    there is no argument.

> Returns the boot time expressed in seconds (> integer/float)

---

- **`available_ram_raw()`**

**Returns the available RAM.**

Arguments:

    there is no argument.

> Returns the available RAM in bytes (> integer)

---

- **`total_ram_raw()`**

**Returns the total RAM installed.**

Arguments:

    there is no argument.

> Returns the total RAM installed in bytes (> integer)

---

- **`used_ram_raw()`**

**Returns the used RAM.**

Arguments:

    there is no argument.

> Returns the used RAM in bytes (> integer)

---

- **`free_swap_memory_raw()`**

**Returns the free SWAP memory if available.**

Arguments:

    there is no argument.

> Returns the free SWAP memory if available in bytes (> integer)

---

- **`total_swap_memory_raw()`**

**Returns the total SWAP memory if available.**

Arguments:

    there is no argument.

> Returns the total SWAP memory if available in bytes (> integer)

---

- **`used_swap_memory_raw()`**

**Returns the used SWAP memory if available.**

Arguments:

    there is no argument.

> Returns the used SWAP memory if available in bytes (> integer)

---

- **`disk_total_read_raw()`**

**Returns the total amount of data read for the startup disk in bytes.**

Arguments:

    there is no argument.

> Returns the total amount of data read for the startup disk in bytes (> integer)

---

- **`disk_total_write_raw()`**

**Returns the total amount of data written for the startup disk in bytes).**

Arguments:

    there is no argument.

> Returns the total amount of data written for the startup disk in bytes (> integer)

---

- **`net_total_sent_raw()`**

**Returns the total amount of data received over the network (in bytes).**

Arguments:

    there is no argument.

> Returns the total amount of data received over the network (in bytes) (> integer)

---

- **`net_total_received_raw()`**

**Returns the IP Addresss/MAC address, Netmask and Brodcast IP/MAC for each network interfaces.**

Arguments:

    there is no argument.

> Returns the IP Addresss/MAC address, Netmask and Brodcast IP/MAC for each network interfaces (> integer)


---

<a name="development"/>

## Development
File Center is in constant development and fixes are made on a regular basis (but I also try to add some new features ehe)

#### If you have any issues, questions, development problem: feel free to ask in the issues section.

If you want to help us and join me here is a quick guide.

### Files
`__init.py__` is the main module

`README.md` is the text file you're currently reading, with all the documentations and explanations.

`LICENSE` is a text file with File Center's license

#### Dependencies
The File Center Library has two third-party dependencies.

- `requests`
- `psutil

Requests is used to make requests

Psutil is used for system information.

<a name="legals"/>

## Copyrights and Legals

**If you think that there is any kind of copyright infrigements, feel free to ask me to remove it and I will try to do so as soon as possible**

**GitHub** is a brand which belongs to GitHub, Inc. (Microsoft)

**Python** belongs to the Python Software Foundation


> ©Anime no Sekai - 2020 ✨
