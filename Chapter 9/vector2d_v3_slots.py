"""
Example 9-7: vector2d_v3: Make Vector2d objects immutables
"""

from array import array
import math

class Vector2d:
    __slots__ = ('__x', '__y')
    typecode = 'd'

    def __init__(self, x: float, y: float) -> None:
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self) -> str:
        return str(tuple(self))

    def __bytes__(self) -> bytes:
        return (bytes([ord(self.typecode)]) +
               bytes(array(self.typecode, self)))

    def __eq__(self, other) -> bool:
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

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

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def angle(self):
        return math.atan2(self.y, self.x)