import random

from tombola import Tombola


class LotteryBlower(Tombola):
    def __init__(self, iterable: iter) -> None:
        self._balls = list(iterable)

    def load(self, iterable: iter) -> None:
        self._balls.extend(iterable)

    def pick(self) -> None:
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty BingoCage')
        return self._balls.pop(position)

    def loaded(self) -> bool:
        return bool(self._balls)

    def inspect(self) -> tuple:
        return tuple(sorted(self._balls))