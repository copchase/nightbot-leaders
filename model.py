from typing import Any


class LeaderUserClass:
    """
    The values are treated as inverted in comparison operations to work with
    the built-in min heap provided in the standard library
    """

    def __init__(self, *, value: Any, last_modified: int, user_id: str) -> None:
        self.value = value
        self.last_modified = last_modified
        self.user_id = user_id

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, LeaderUserClass):
            return False

        out = True
        out &= self.value == __o.value
        out &= self.last_modified == __o.last_modified
        return out

    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __lt__(self, __o: object) -> bool:
        if not isinstance(__o, LeaderUserClass):
            return False

        out = False
        out |= self.value > __o.value
        out |= self.last_modified < __o.last_modified
        return out

    def __le__(self, __o: object) -> bool:
        return self.__lt__(__o) or self.__eq__(__o)

    def __gt__(self, __o: object) -> bool:
        return not self.__le__(__o)

    def __ge__(self, __o: object) -> bool:
        return not self.__lt__(__o)
