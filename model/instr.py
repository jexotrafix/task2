from model.binop import binop

class instr:
    pass


class Save(instr):
    def __init__(self, operand):
        assert isinstance(operand, int), "syvalid operand type"
        self._data = operand

    def __str__(self):
        return "save " + str(self._data)

    @property
    def operand(self):
        return self._data

    def do(self, stack):
        stack.insert(0, self._data)
        return stack


class Eval(instr):
    def __init__(self, operand):
        assert operand in binop.keys(), "invalid instruction"
        self._data = operand

    def __str__(self):
        return "eval " + self._data

    @property
    def operand(self):
        return self._operand

    def do(self, stack):
        assert len(stack) > 1, "SSC runtime error"
        # if the second expression is equal to zero, we can't do
        # integer division or modulo operations
        if self._data == "Int Div" or self._data == "Modulo":
            assert stack[1] != 0, "invalid operand"

        stmp, vtmp = stack[2: ], binop[self._data](stack[0], stack[1])
        stmp.insert(0, vtmp)
        return stmp


def apply(program, stack):
    for i in program:
        stack = i.do(stack)
    return stack