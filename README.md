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
   - [Image Enhancement and Editing](#images)
   - [Hashing and Encoding](#hashing)
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

> Returns the number of seconds it slept if success, 1 if failed (> float/integer)

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

> Returns the new working directory if success, 1 if failed (> str/integer)

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

    commands: a string of command to be executed.
    capture_errors (optional, default:True): a boolean value which determines if the program should also capture and return console errors (stderr).
    hide_error (optional, default:False): a boolean value which determines if stderr errors should be shown if capture_errors is False.
    shell (optional, default:False): a boolean value which specifies if it is a shell command (I guess for Windows users?) (But it is kind of weird because commands on macOS with shell=True do not work).
    universal_newlines (opetional, default:True): Wether the returned value should have universal newlines.

> Returns the command output/result (> mostly string)

---
- **`command(command)`**

**Executes a command and returns the response code.**

Arguments:

    command: a string of command to be executed.
    hide_output (optional, default:False): a boolean which tells if outputs (stdout) should be shown on the console.
    hide_error (optional, default:False): a boolean which tells if errors (stderr) should be shown on the console.
    shell (optional, default:False): a boolean value which specifies if it is a shell command (I guess for Windows users?) (But it is kind of weird because commands on macOS with shell=True do not work).

> Returns the command response code (generally 0 if success) (> integer)

---
- **`request(url, method, parameters, data, headers, json_body)`**

**Makes an HTTP request with the given arguments.**

#### INFORMATION: Here are the available HTTP methods:

- GET
- POST
- DELETE
- PATCH
- PUT
- HEAD
- OPTIONS


Arguments:

    url: a string with the url of the request.
    
    method (optional, default: "GET"): a string with the http method to use with the request.
    
    parameters (optional): parameters to be sent with a GET request.
    
    data (optional): the data to be sent with the POST, PATCH and PUT request
    
    headers (optional): the headers to be sent with the GET, POST, PATCH, DELETE and PUT request (i.e. the API Key).
    
    json_body (optional): the json body of the request for POST, PATCH and PUT requests.

> Returns a <Response> type value (see the [Requests module documentation]
(https://requests.readthedocs.io/en/master/user/quickstart/#response-content) to learn more about this response type).
 
> Example: `response.text` is the content of the response.
 
> Returns 'Sorry but this HTTP Request Method is not available yet.' if the method isn't available.

---
- **`request_statuscode(url, method, parameters, data, headers, json_body)`**

**Makes an HTTP request with the given arguments and returns the status code.**

#### INFORMATION: Here are the available HTTP methods:

- GET
- POST
- DELETE
- PATCH
- PUT
- HEAD
- OPTIONS

Arguments:

    url: a string with the url of the request.
    
    method (optional, default: "GET"): a string with the http method to use with the request.
    
    parameters (optional): parameters to be sent with a GET request.
    
    data (optional): the data to be sent with the POST, PATCH and PUT request
    
    headers (optional): the headers to be sent with the GET, POST, PATCH, DELETE and PUT request (i.e. the API Key).
    
    json_body (optional): the json body of the request for POST, PATCH and PUT requests.

> Returns an integer representing the status code.
 
> Returns 'Sorry but this HTTP Request Method is not available yet.' if the method isn't available.

---

- **`pip_install(packages_to_install, upgrade, hide_output, hide_error)`**

**Installs the given PyPI (pip) packages.**

Arguments:

    packages_to_install: a list of packages to install.

    upgrade (optional, default: False): Wether you want to update your already installed package.

    hide_output (optional, default: False): Wether you want to hide the outputs from PIP.

    hide_error (optional, default: False): Wether you want to hide the possible errors (stderr) from PIP.

> Returns -1 if the packages_to_install argument isn't the right type, -2 if there is no life of packages and the install output (results from the console) if succeeded to try installing the packages. (> int)

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

- **`timing()`**

**Returns the current time in seconds since Epoch (1970 for UNIX-based systems like macOS and Linux).**

Arguments:

    there is no argument.

> Returns a float which represents the seconds since Epoch (> string)


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

> Returns 0 when done.

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

> Returns the given title or an error string if title_string type not supported (> string)

---

- **`display_body(body)`**

**Sets the body for display().**

Arguments:

    body_list: a list of string to be displayed as the body for display(). Each new element in the list means a line break.

> Returns the given body or an error string if body_list type not supported (> list)

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

> Returns the new filepath if success, 1 if failed (> str/integer)

---

- **`delete_file(filepath)`**

**Deletes the given file.**

Also available in my file management/info center library for python: `filecenter`

Arguments:

     file: the path of the file

> Returns 0 if success, 1 if failed at getting the file, 2 if failed at deleting a file and 3 if failed at deleting a directory (> integer)


---

- **`make_dir(path_of_new_dir)`**

**Makes a directory at the given path.**

Arguments:

    path_of_new_dir: the path to the directory (string).
    
> Returns the path of the new directory if success, 1 if failed (> str/integer)

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

    append (default: False, optional): Wether the text should be appended to a already existent file.
    
> Returns 0 if success and 1 if the text argument isn't in the right format (not a list or a string) (> integer)

---

- **`read_file(file_path)`**

**Returns the content of a text file.**

Arguments:

    file_path: the path to the text file

> Returns the content of the file (> string)

---

- **`read_file_line(file_path, lines_to_read)`**

**Returns the given line of a text file.**

Arguments:

    file_path: the path to the text file.

    lines_to_read (optional, default: 1): the line (if integer) or lines (if list of integers) to read and return

> Returns the given line of the text file or a list of strings. (> string)

---

- **`file_inside_file(file_path, search_query, whole_document)`**

**Returns the given line of a text file.**

Arguments:

    file_path: the path to the text file.

    search_query: the searching term(s).

    whole_document (optional, default: False): the search stops at the first result if whole_document is False and continues searching the whole document if True.

> Returns a dictionnary or a list of dictionnary. (> dict)

---

<a name="images"/>

### Image Enhancement and Editing

- **`image_brightness_enhancement(image_path, output_name, enhancement_factor)`**

**Enhances the image's brightness by the given factor and saves it to a file.**

Arguments:

    image_path: the path to the image you want to enhance.
    
    output_name: the name of the output file.

    enhancement_factor (default: 1): the factor of brightness enhancement.
    If set to 1, no visible changes in brightness are made.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---

- **`image_contrast_enhancement(image_path, output_name, enhancement_factor)`**

**Enhances the image's contrast by the given factor and saves it to a file.**

Arguments:

    image_path: the path to the image you want to enhance.
    
    output_name: the name of the output file.

    enhancement_factor (default: 1): the factor of brightness enhancement.
    If set to 1, no visible changes in contrast are made.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---

- **`image_color_enhancement(image_path, output_name, enhancement_factor)`**

**Enhances the image's colors by the given factor and saves it to a file.**

Arguments:

    image_path: the path to the image you want to enhance.
    
    output_name: the name of the output file.

    enhancement_factor (default: 1): the factor of brightness enhancement.
    If set to 1, no visible changes in color are made.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---


- **`image_grayscale(image_path, output_name)`**

**Turns the image in a grayscale (no color) image and saves it to a file.**

Arguments:

    image_path: the path to the image you want to enhance.
    
    output_name: the name of the output file.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---


- **`image_rgb(image_path, output_name)`**

**Converts the image in an RGB (color profile) image and saves it to a file.**

Arguments:

    image_path: the path to the image you want to enhance.
    
    output_name: the name of the output file.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---


- **`image_cmyk(image_path, output_name)`**

**Converts the image in an CMYK (color profile) image and saves it to a file.**

##### WARNING: This function fails more often that the others, especially with PNG files. (I don't know why)

Arguments:

    image_path: the path to the image you want to enhance.
    
    output_name: the name of the output file.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---


- **`image_resize(image_path, output_name, new_size)`**

**Resizes the image with the given size and saves it to a file.**

Arguments:

    image_path: the path to the image you want to enhance.
    
    output_name: the name of the output file.
    
    new_size: a tuple of two values corresponding to the new size.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---


- **`image_resize_with_same_aspect_ratio(image_path, output_name, new_size)`**

**Resizes the images while keeping the same aspect ratio (the image won't be strectched) and saves it to a file.**

Arguments:

    image_path: the path to the image you want to enhance.
    
    output_name: the name of the output file.
    
    new_size: a tuple of two values corresponding to the new size.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---


- **`image_crop(image_path, output_name, crop_size)`**

**Crops the image with the given size and saves it to a file.**

Arguments:

    image_path: the path to the image you want to enhance.
    
    output_name: the name of the output file.
    
    crop_size: a tuple of four values corresponding to the cropping size.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---


- **`image_to_jpeg(image_path, output_name, jpeg_quality)`**

**Saves the image as jpeg, with the given quality (compression quality) and saves it to a file.**

Arguments:

    image_path: the path to the image you want to enhance.
    
    output_name: the name of the output file.
    
    jpeg_quality: an integer which represents the jpeg compression quality from 0 to 100 (100 being best quality).

> Returns a string with the path of the output file or 1 if failed (> string/int)

---


- **`image_watermark(image_path, output_name, watermark_path)`**

**Adds a watermark at the bottom right of the image and saves it to a file.**

Arguments:

    image_path: the path to the image you want to enhance.
    
    output_name: the name of the output file.
    
    watermark_path: the path to the watermark image.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---


- **`image_invert(image_path, output_name)`**

**Inverts the image colors and saves it to a file.**

Arguments:

    image_path: the path to the image you want invert the colors.
    
    output_name: the name of the output file.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---


- **`image_gaussian_noise(image_path, output_name)`**

**Adds gaussian noise to the image and saves it to a file.**

Arguments:

    image_path: the path to the image you want invert the colors.
    
    output_name: the name of the output file.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---


- **`image_salt_and_pepper_noise(image_path, output_name)`**

**Adds salt and pepper noise the image and saves it to a file.**

Arguments:

    image_path: the path to the image you want invert the colors.
    
    output_name: the name of the output file.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---


- **`image_poisson_noise(image_path, output_name)`**

**Adds poisson noise to the image and saves it to a file.**

Arguments:

    image_path: the path to the image you want invert the colors.
    
    output_name: the name of the output file.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---


- **`image_speckle_noise(image_path, output_name)`**

**Adds speckle noise to the image and saves it to a file.**

Arguments:

    image_path: the path to the image you want invert the colors.
    
    output_name: the name of the output file.

> Returns a string with the path of the output file or 1 if failed (> string/int)

---

<a name="hashing"/>

### Hashing and Encoding/Decoding


- **`hash_image(image, algorithm, raw)`**

**Hashes the given image with the chosen algorithm (average hash by default)**

#### INFORMATION: Here is a list of the available hashing functions:

Hashing Function | Argument to pass
------------ | -------------
Average Hash | aHash
Color Hash | cHash
Difference Hash | dHash
Difference Hash Vertical | dHash_vertical
Perceptual Hash | pHash
Perceptual Hash (simple) | pHash_simple
Wavelet Hash | wHash

Arguments:

    image: A PIL (Pillow) instance of the image.
    
    algorithm (default: 'aHash'): the used algorithm.
    
    raw (optional, default: False): if it returns a raw ImageHash instance (to make, for example hamming distances between two hashes), or if it returns the hash as a string.

> Returns the hash as a string if raw=False, an ImageHash class if raw=True (> string/ImageHash)

---

- **`hash_image_from_url(image_url, algorithm, raw)`**

**Hashes the given image from the image url with the chosen algorithm (average hash by default)**

#### INFORMATION: Here is a list of the available hashing functions:

Hashing Function | Argument to pass
------------ | -------------
Average Hash | aHash
Color Hash | cHash
Difference Hash | dHash
Difference Hash Vertical | dHash_vertical
Perceptual Hash | pHash
Perceptual Hash (simple) | pHash_simple
Wavelet Hash | wHash


Arguments:

    image_url: the URL of the image.
    
    algorithm (default: 'aHash'): the used algorithm.
    
    raw (optional, default: False): if it returns a raw ImageHash instance (to make, for example hamming distances between two hashes), or if it returns the hash as a string.

> Returns the hash as a string if raw=False, an ImageHash class if raw=True (> string/ImageHash)

---

- **`hash_image_from_path(image_path, algorithm, raw)`**

**Hashes the given image from his path with the chosen algorithm (average hash by default)**

#### INFORMATION: Here is a list of the available hashing functions:

Hashing Function | Argument to pass
------------ | -------------
Average Hash | aHash
Color Hash | cHash
Difference Hash | dHash
Difference Hash Vertical | dHash_vertical
Perceptual Hash | pHash
Perceptual Hash (simple) | pHash_simple
Wavelet Hash | wHash


Arguments:

    image_path: the path to the hashing image.
    
    algorithm (default: 'aHash'): the used algorithm.
    
    raw (optional, default: False): if it returns a raw ImageHash instance (to make, for example hamming distances between two hashes), or if it returns the hash as a string.

> Returns the hash as a string if raw=False, an ImageHash class if raw=True (> string/ImageHash)

---

- **`hash_string_to_raw_hash(hash_string)`**

**Converts a Hash String to raw, ImageHash hash instance**

Arguments:

    hash_string: the hash string to convert.

> Returns an ImageHash Class object.

---

- **`base64_from_image(image_path)`**

**Encodes an image in base64**

Arguments:

    image_path: the path to the image.

> Returns the base64 string of the image.

---

- **`string_to_base64(string)`**

**Encodes a string in base64.**

Arguments:

    string: the string to encode.
    
> Returns the base64 encoded string.

---

- **`string_to_ascii(string)`**

**Encodes a string in ASCII (bytes).**

Arguments:

    string: the string to encode.
    
> Returns a bytes type ascii string.

---

- **`ascii_to_string(ascii_element)`**

**Encodes an ASCII string (bytes) into a regular string.**

Arguments:

    ascii_element: the ascii string to decode.
    
> Returns a string.

---

- **`json_to_dict(json_string)`**

**Turns a JSON string as a Python Dictionnary.**

Arguments:

    json_string: the json string to turn into a dictionnary.
    
> Returns a python dictionnary.

---

- **`dict_to_json_string(dict)`**

**Turns a Python Dictionnary into a JSON string.**

Arguments:

    dict: the python dictionnary to turn into json.
    
> Returns a string.


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

---

- **`process_time()`**

**Gives the process time.**

Arguments:

    there is no argument.

> Returns a float in seconds (> float)

---

- **`pid()`**

**Returns the Process ID of the current process (Python Process).**

Arguments:

    there is no argument.

> Returns the PID (> int)

---

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
The LifeEasy Library has five third-party dependencies.

- `requests`
- `psutil`
- `imagehash`
- `Pillow`
- `numpy`

Requests is used to make requests

Psutil is used for system information.

<a name="legals"/>

## Copyrights and Legals

**If you think that there is any kind of copyright infrigements, feel free to ask me to remove it and I will try to do so as soon as possible**

**GitHub** is a brand which belongs to GitHub, Inc. (Microsoft)

**Python** belongs to the Python Software Foundation


> ©Anime no Sekai - 2020 ✨
