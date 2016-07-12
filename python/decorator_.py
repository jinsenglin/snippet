"""
simplest snippet
"""
import functools

def decorated(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kargs):
        print "wrapper"
        result = fn(*args, **kargs)
        return result
    return wrapper

@decorated
def f():
    print "f"

f()
