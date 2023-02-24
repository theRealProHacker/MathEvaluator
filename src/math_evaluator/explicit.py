"""
Explicitly calculates valid mathematical expressions (using "+-*/" and brackets)
"""

import ast
import operator


def calc(expr: str):
    return compute(ast.parse(expr, mode="eval").body)


op_map = {
    # binary
    ast.Add: operator.__add__,
    ast.Sub: operator.__sub__,
    ast.Div: operator.__truediv__,
    ast.Mult: operator.__mul__,
    # unary
    ast.UAdd: operator.__pos__,
    ast.USub: operator.__neg__,
}

allowed_types = {int, float}


def compute(expr):
    match expr:
        case ast.Constant(value=value):
            if type(value) not in allowed_types:
                raise SyntaxError(
                    f"Not a number {value!r}"
                )
            return value
        case ast.UnaryOp(op=op, operand=value):
            try:
                return op_map[type(op)](compute(value))  # type: ignore
            except KeyError:
                raise SyntaxError(f"Unknown operation {ast.unparse(expr)}")
        case ast.BinOp(op=op, left=left, right=right):
            try:
                return op_map[type(op)](compute(left), compute(right))  # type: ignore
            except KeyError:
                raise SyntaxError(f"Unknown operation {ast.unparse(expr)}")
        case x:
            raise SyntaxError(f"Invalid Node {ast.dump(x)}")
