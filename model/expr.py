from model.binop import binop

class expr:
    pass


class Const(expr):
    def __init__(self, n):
        assert isinstance(n, int), "invalid constant type"
        self._data = n

    def __str__(self):
        return "(Const " + str(self._data) + ")"

    @property
    def value(self):
        return self._data


class Binop(expr):
    def __init__(self, b, e1, e2):
        assert b in binop.keys(), "invalid binop type"
        assert isinstance(e1, expr) and isinstance(e2, expr), \
               "invalid operand"
        
        self._data = (b, e1, e2)

    def __str__(self):
        tmp = str(self._data[0]) + " "
        tmp += str(self._data[1]) + " "
        tmp += str(self._data[2])
        return "(" + tmp + ")"

    @property
    def operator(self):
        return self._data[0]

    @property
    def operand1(self):
        return self._data[1]

    @property
    def operand2(self):
        return self._data[2]

    @property
    def value(self):
        # if the second expression is equal to zero, we can't do
        # integer division or modulo operations
        if self._data[0] == "Int Div" or self._data[0] == "Modulo":
            assert self._data[2] != 0, "invalid operand"

        return binop[self._data[0]](self._data[1].value,
                                    self._data[2].value)