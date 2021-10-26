import random

from tombola import Tombola


class BingoCage(Tombola):
    
    def __init__(self, items: iter):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items: iter) -> None:
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()