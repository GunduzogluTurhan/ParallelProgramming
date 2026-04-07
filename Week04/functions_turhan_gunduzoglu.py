custom_power = lambda x, e=1: x ** e


def custom_equation(x, y=0, /, a=0, *, b=1, c=1) -> float:
    """
    Calculate the value of (x**a + y**b) / c.

    :param x: integer (positional-only)
    :param y: integer (positional-only, default=0)
    :param a: integer (positional or keyword, default=0)
    :param b: integer (keyword-only, default=1)
    :param c: integer (keyword-only, default=1)
    :return: float
    """
  return (x ** a + y ** b) / c

def fn_w_counter():
    calls = {}

    def inner(caller_name):
        calls[caller_name] = calls.get(caller_name, 0) + 1
        total_calls = sum(calls.values())
        return total_calls, calls

    return inner
