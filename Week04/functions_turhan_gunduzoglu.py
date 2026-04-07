import sys

custom_power = lambda x, /, e=1: x ** e

def custom_equation(x: int = 0, y: int = 0, /, a: int = 1, b: int = 1, *, c: int = 1) -> float:
    """
    Compute (x**a + y**b) / c.

    :param x: Base for the first term; positional-only; default 0.
    :type x: int
    :param y: Base for the second term; positional-only; default 0.
    :type y: int
    :param a: Exponent for x; positional-or-keyword; default 1.
    :type a: int
    :param b: Exponent for y; positional-or-keyword; default 1.
    :type b: int
    :param c: Divisor; keyword-only; default 1.
    :type c: int
    :return: (x**a + y**b) / c
    :rtype: float
    """
    return (x ** a + y ** b) / c

_counter_total = 0
_counter_callers = {}

def fn_w_counter() -> tuple:
    global _counter_total, _counter_callers
    caller = sys._getframe(1).f_globals.get("__name__", "<unknown>")
    _counter_total += 1
    _counter_callers[caller] = _counter_callers.get(caller, 0) + 1
    return (_counter_total, dict(_counter_callers))
