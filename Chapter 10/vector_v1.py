from __future__ import annotations
from array import array
import reprlib
import math

class Vector:

    typecode = 'd'

    def __init__(self, components: iter) -> None:
        self._components = array(self.typecode, components)

    def __iter__(self) -> iter:
        return iter(self._components)

    def __repr__(self) -> str:
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self) -> str:
        return str(tuple(self))

    def __bytes__(self) -> bytes:
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def eq(self, other: Vector) -> bool:
        return tuple(self) == tuple(other)

    def __abs__(self) -> float:
        return math.sqrt(sum(x + x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets: bytes) -> Vector:
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


