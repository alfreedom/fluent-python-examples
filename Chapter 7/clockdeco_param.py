
import functools
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate



def clock_v2(fmt= DEFAULT_FMT, enable=True):
    def decorate(func):
        @functools.wraps(func)
        def clocked(*_args, **_kwargs):
            t0 = time.time()
            _result = func(*_args, *_kwargs)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate