'''
`with` keyword in Python
`with` is a keyword in Python that is used to wrap the execution of a block of code within methods defined by a context manager. This allows for the setup and teardown of resources, such as file handling, to be managed automatically.
The `with` statement simplifies exception handling by encapsulating common preparation and cleanup tasks in a block of code. It ensures that resources are properly released after their use, even if an error occurs.
The syntax for using `with` is as follows:
with expression as variable:
    # code block
In this syntax, `expression` is evaluated to obtain a context manager, and `variable` is assigned the value returned by the context manager's `__enter__` method. The code block is executed within the context of the manager, and when the block is exited, the context manager's `__exit__` method is called to clean up resources.
A common use case for the `with` statement is file handling. For example:
'''
with open('example.txt', 'r') as file:
    data = file.read()
    print(data)
# The file is automatically closed after the block is exited, even if an error occurs.