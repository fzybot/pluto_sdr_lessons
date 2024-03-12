
from numpy import array


__all__ = [
    'convolution', 
    ]

def convolution(array_a, array_b):
    result = []
    
    a, v = array(a, copy=False, ndmin=1), array(v, copy=False, ndmin=1)
    if (len(v) > len(a)):
        a, v = v, a
    if len(a) == 0:
        raise ValueError('a cannot be empty')
    if len(v) == 0:
        raise ValueError('v cannot be empty')
    
    
    return result