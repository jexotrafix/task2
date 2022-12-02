from model.expr import *
from model.instr import *

class SSC:
    def __init__(self):
        self._stack = []
        self._program = []

    def load(self, program):
        assert isinstance(program, list), "invalid program type"
        assert not program or all(map(isinstance,
                                      program,
                                      len(program) * [instr])), \
               "some program instruction is invalid"
        self._program = program

    def run(self):
        self._stack = []
        return apply(self._program, self._stack)


def compile(expression):
    assert isinstance(expression, expr), "invalid expression"
    if isinstance(expression, Const):
        return [Save(expression.value)]
    else:   # isinstance(expression, Binop)
        b = expression.operator
        e1, e2 = expression.operand1, expression.operand2
        return compile(e1) + compile(e2) + [Eval(b)]