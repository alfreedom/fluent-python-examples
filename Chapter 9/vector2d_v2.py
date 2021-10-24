"""
Example 9-6: Vector2d.format method, take #2, now with polar coordniates
"""

from __future__ import annotations
from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)
        self.y = float(y)

    def __iter__(self) -> tuple:
        return (i for i in (self.x, self.y))

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self) -> str:
        return str(tuple(self))

    def __bytes__(self) -> bytes:
        return (bytes([ord(self.typecode)]) +
               bytes(array(self.typecode, self)))

    def __eq__(self, other: Vector2d) -> bool:
        return tuple(self) == tuple(other)

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __bool__(self) -> bool:
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'

        components =  (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)