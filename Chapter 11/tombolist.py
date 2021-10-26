from random import randrange

from tombola import Tombola

@Tombola.register
class TomboList(list):

    def pick(self) -> object:
        if self:
            position = randrange(self)
            return self.pop(position)
        else:
            raise LookupError('pick from empty Tobolist')
    
    load = list.extend

    def loaded(self) -> bool:
        return bool(self)

    def inspect(self) -> tuple:
        return tuple(sorted(self))