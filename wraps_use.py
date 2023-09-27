def my_decorator_without_wraps(func):
    def wrapper(*args, **kwargs):
        print("Before function is called")
        result = func(*args, **kwargs)
        print("After function is called")
        return result

    return wrapper


@my_decorator_without_wraps
def my_function():
    """This is my function."""
    pass


print(my_function.__name__)  # Prints 'wrapper' instead of 'my_function'
print(my_function.__doc__)  # Prints the docstring of 'wrapper' instead of 'my_function'

from functools import wraps


def my_decorator(func):
    @wraps(func)  # Use wraps to preserve the original function's metadata
    def wrapper(*args, **kwargs):
        print("Before function is called")
        result = func(*args, **kwargs)
        print("After function is called")
        return result

    return wrapper


@my_decorator
def my_function_wraps():
    """This is my function."""
    pass


print(my_function_wraps.__name__)  # Prints 'wrapper' instead of 'my_function'
print(
    my_function_wraps.__doc__
)  # Prints the docstring of 'wrapper' instead of 'my_function'
