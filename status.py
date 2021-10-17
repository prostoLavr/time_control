from enum import Enum


class Status(Enum):
    run = 1
    notdone = 0
    done = 2

    @classmethod
    def from_checkbox(cls, value):
        if value == 0:
            return cls.notdone
        if value == 1:
            return cls.run
        if value == 2:
            return cls.done

    @classmethod
    def from_value(cls, value):
        if value == 0:
            return cls.notdone
        if value == 1:
            return cls.run
        if value == 2:
            return cls.done
