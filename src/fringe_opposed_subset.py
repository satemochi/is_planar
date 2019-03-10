from collections import deque


class fringe_opposed_subset:
    __slots__ = ('c')

    def __init__(self, h):
        self.c = [deque([h]), deque()]

    def __repr__(self):
        return ('\33[1m\33[90m(\33[0m' + str(list(self.c[0])) +
                ', ' + str(list(self.c[1])) + '\33[1m\33[90m)\33[0m')

    @property
    def left(self):
        return self.c[0]

    @property
    def right(self):
        return self.c[1]

    @property
    def l_lo(self):
        return self.c[0][-1]

    @property
    def l_hi(self):
        return self.c[0][0]

    @property
    def r_lo(self):
        return self.c[1][-1]

    @property
    def r_hi(self):
        return self.c[1][0]

    def last_of_left_is_lowest(self):
        return self.l_lo == min(self.left)

    def last_of_right_is_lowest(self):
        return self.r_lo == min(self.right) if self.right else True
