from datetime import datetime


def fib(n):
    if n == 1:
        return 0
    first = 0
    second = 1
    for _ in range(2, n):
        first, second = second, first + second
    return second


def time_converter(time_string):
    datetime_obj = datetime.strptime(time_string, "%b %d, %Y %I:%M:%S %p")
    formatted_date = datetime_obj.strftime("%d %B %Y %H:%M:%S")
    return formatted_date
