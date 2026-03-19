'''
Delete Files in Python
In Python, you can delete files using the `os` module, which provides a method called `remove()`. This method takes the file path as an argument and deletes the specified file from the filesystem.
Here's how you can use the `os.remove()` method to delete a file:
import os
file_path = 'path/to/your/file.txt'
try:
    os.remove(file_path)
    print(f"{file_path} has been deleted successfully.")
except FileNotFoundError:
    print(f"{file_path} does not exist.")
except Exception as e:
    print(f"An error occurred while trying to delete {file_path}: {e}")
In this example, we first import the `os` module and define the path to the file we want to delete. We then use a `try-except` block to handle potential exceptions that may arise during the deletion process. If the file is successfully deleted, a confirmation message is printed. If the file does not exist, a `FileNotFoundError` is caught, and an appropriate message is displayed. Any other exceptions that may occur are also caught and printed for debugging purposes.
It's important to note that once a file is deleted using `os.remove()`, it cannot be recovered through Python, so use this method with caution. Always ensure that you have the correct file path and that you intend to delete the file before executing the code.
'''

# Example of deleting a file using os.remove()
import os
file_path = os.getcwd() + "/example2.txt"
try:
    os.remove(file_path)
    print(f"{file_path} has been deleted successfully.")
except FileNotFoundError:
    print(f"{file_path} does not exist.")
except Exception as e:
    print(f"An error occurred while trying to delete {file_path}: {e}")
