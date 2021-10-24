from __future__ import annotations
from array import array
import math
import numbers
import reprlib

class Vector:

    typecode = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components: iter) -> None:
        self._components = array(self.typecode, components)

    def __len__(self) -> int:
        return len(self._components)

    def __getitem__(self, index: int) -> object:
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name: str) -> object:
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos <= len(self._components):
                return self._components[pos]

        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name: str, value: object) -> None:
        cls = type(self)

        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'Read only attribute {attr_name!r}'
            elif name.islower():
                error = "Can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''

            if error:
                msg = error.format(cls_name= cls.__name__, attr_name=name)
                raise AttributeError(msg, value)
        super().__setattr__(name, value)

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


