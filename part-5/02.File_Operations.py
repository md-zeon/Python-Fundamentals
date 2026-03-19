'''
File Operations in Python
1. Opening a File
2. Reading from a File
3. Writing to a File
4. Closing a File
'''
'''
Opening a File
To open a file in Python, you can use the built-in `open()` function. The syntax is as follows:
file_object = open(file_name, mode)
Where:
- `file_name` is the name of the file you want to open (including the path if it's not in the current directory).
- `mode` is the mode in which you want to open the file. Common modes include
    - 'r' for reading (default)
    - 'w' for writing (creates a new file or truncates an existing file)
    - 'a' for appending (adds to the end of the file)
    - 'b' for binary mode (used for non-text files)
    - 't' for text mode (default)

if the file does not exist and you try to open it in 'r' mode, it will raise a `FileNotFoundError`. If you open a file in 'w' mode and the file already exists, it will be truncated (i.e., all existing content will be deleted). Always remember to close the file after you're done with it to free up system resources.
'''
# Example of opening a file for reading
file_read = open('example.txt', 'r')
# Example of opening a file for writing
# file_write = open('example.txt', 'w')
'''
Reading from a File
Once you have opened a file for reading, you can read its contents using various methods. Some common methods include:
- `read()` - reads the entire file
- `readline()` - reads a single line from the file
- `readlines()` - reads all lines from the file and returns a list
'''
# Example of reading from a file
data = file_read.read()  # Reads the entire file
print(type(data))  # Output: <class 'str'>
file_read.seek(0)  # Move the file pointer back to the beginning of the file
print(data)  # Output: Contents of the file as a string
line = file_read.readline()  # Reads the next line from the file
print(line)
lines = file_read.readlines()  # Reads all lines and returns a list
print(lines)
'''
Writing to a File
To write to a file, you can use the `write()` method. When you open a file in 'w' mode, it will create a new file or overwrite an existing file. When you open a file in 'a' mode, it will append to the end of the file instead of overwriting it.
'''
# Example of writing to a file
# file_write.write("Hello, World!\n")  # Writes a string to the file
# file_write.write("This is a new line.\n")  # Writes another line to the file
'''Closing a File
After you have finished working with a file, it's important to close it using the `close()` method. This ensures that all resources associated with the file are released and that any changes are saved properly.
'''
# Example of closing a file
file_read.close()  # Closes the file opened for reading
# file_write.close()  # Closes the file opened for writing