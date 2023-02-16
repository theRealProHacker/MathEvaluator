from pytest import raises, main
import ast
import operator
from math_evaluator.explicit import calc as explicit_calc, op_map
from math_evaluator.implicit import calc as implicit_calc, valid_ops, allowed_types


def calc_test(calc):
    assert calc("1+4") == 5
    assert calc("-4-2") == -6
    assert calc("-3*-5") == 15
    assert calc("20/-4") == -5
    assert calc("2*3+5") == 11
    assert calc("2*(3+5)") == 16
    ...
    for error in [
        "not True",
        "2//3",
        "nonsense",
        "print('I\\'m a hacker')",
        "this is a syntax error",
    ]:
        with raises(SyntaxError):
            calc(error)

def test_implicit_example1():
    valid_ops.add(ast.Pow)

    assert implicit_calc("4**3") == 4**3

def test_implicit_example2():
    allowed_types.add(complex)

    assert implicit_calc("3*5j") == 15j

def test_explicit_example1():
    op_map[ast.BitXor] = operator.__pow__

    assert explicit_calc("5^4") == 625

def test():
    for calc in (explicit_calc, implicit_calc):
        calc_test(calc)


if __name__ == "__main__":
    main()
