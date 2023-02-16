# Math Evaluator
A package that evaluates a mathematical expression given as a string.

By default it accepts
- operands
    - `int`s and 
    - `float`s
- operators
    - unary `+-`, 
    - binary `+-*/` and
    - parantheses `()`


# Getting Started
Getting your first application running is super easy.

```shell
pip install math_evaluator
```

```py
"""
A small CLI application that endlessly takes user input and evaluates it as a mathematical expression
"""
from math_evaluator import calc 

while True:
    # this will raise a SyntaxError if the expression is syntactically incorrect
    # normally you should always catch that Exception
    expression = input(">>> ")
    print(calc(expression))
```

# Customization
The above usage is the simplest and suffices most of the time. Anyways, Math Evaluator is built to be customized by you. It internally uses the Python parser however, so it's abilities cannot be changed fundamentally. For example operator assoziativity or how parentheses work cannot be altered.  

This package consists of two main modules `.implicit` and `.explicit`. However, most applications will only need to use one of them.

## `.implicit`
Checks if the expression is a valid mathematical expression and then `eval`s it. This makes it totally safe to use - even when exposed to potencially malicious users.

### `.implicit` example 

We might want to extend the calculator to allow powers (`**` is the corresponding operator). To do that we can reach into `math_evaluator.implicit` and add `ast` operations to the valid operations

```py
import ast
from math_evaluator.implicit import calc, valid_ops

valid_ops.add(ast.Pow)

assert calc("4**3") == 4**3
```

You can not only change the valid operations but also the allowed operands. We could for example add `complex` numbers

```py
from math_evaluator.implicit import calc, allowed_types

allowed_types.add(complex)

assert calc("3*5j") == 15j
```

## `.explicit`

Explicitly evaluates the expression. This allows you to modify the semantics.

### `.explicit` example 

In many other programming languages `5 ^ 4` is the same as `5*5*5*5 = 625`. In Python however, `^` is the bitwise xor operator and `5 ^ 4` evaluates to `1`. Now we will redefine `^` to mean the same as `**` by reaching into the `.explicit` module:

```py
import ast
import operator
from math_evaluator.explicit import calc, op_map

op_map[ast.BitXor] = operator.__pow__

assert calc("5^4") == 625
```

`math_parser` exports `.explicit.calc` by default. 

## Further customization

If you want to change the fundamental syntax or semantics, you can file an issue. Then I will try my best at weighing `cost vs gain`. If I deem your feature request as "unworthy", that should not stop you from forking this project and extending it on your own. I am available for any questions you might have. 