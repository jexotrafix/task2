from model.expr import Binop
from model.instr import Save, Eval
from model.ssc import SSC

if __name__ == '__main__':
    # case where everything works fine
    ssc = SSC()
    program = [Save(2), Save(5), Eval("Int Div"), Save(7), Eval("Plus"), Save(2), Eval('Modulo')]
    ssc.load(program)
    stack = ssc.run()
    print(stack)

    # case where the correct assertion is thrown whlie executing integer div
    # ssc = SSC()
    # program = [Save(0), Save(5), Eval("Int Div")]
    # ssc.load(program)
    # stack = ssc.run()
    # print(stack)

    # case where the correct assertion is thrown whlie executing modulo
    # ssc = SSC()
    # program = [Save(0), Save(5), Eval("Modulo")]
    # ssc.load(program)
    # stack = ssc.run()
    # print(stack)

    # case where the correct assertion is thrown whlie calculating value of binary expression
    # binop = Binop("Int Div", 5, Binop("Modulo", 4, 2))
    # binop.value()
