from abc import ABC, abstractmethod
from typing import Union, Any

class Expr(ABC):
    """Base class for symbolic expressions."""

    def __add__(self, other: Any) -> 'Add':
        return Add(self, other)

    def __sub__(self, other: Any) -> 'Sub':
        return Sub(self, other)

    def __mul__(self, other: Any) -> 'Mul':
        return Mul(self, other)

    def __truediv__(self, other: Any) -> 'Div':
        return Div(self, other)

    def __pow__(self, other: Any) -> 'Pow':
        return Pow(self, other)
    
    @abstractmethod
    def diff(self, var: 'Var') -> 'Expr':
        """Symbolic differentiation: implemented in subclasses."""
        pass


class Const(Expr):
    """Constant values (e.g., numbers like 3, 4, etc.)."""
    def __init__(self, value: Union[int, float]) -> None:
        self.value: Union[int, float] = value

    def diff(self, var: 'Var') -> 'Const':
        return Const(0)  # Derivative of a constant is 0

    def __repr__(self) -> str:
        return str(self.value)


class Var(Expr):
    """A variable (e.g., x, y)."""
    def __init__(self, name: str) -> None:
        self.name: str = name

    def diff(self, var: 'Var') -> 'Const':
        return Const(1) if self.name == var.name else Const(0)  # d(x)/dx = 1, d(y)/dx = 0

    def __repr__(self) -> str:
        return self.name


class Add(Expr):
    """Addition operation (a + b)."""
    def __init__(self, left: Expr, right: Expr) -> None:
        self.left: Expr = left
        self.right: Expr = right

    def diff(self, var: 'Var') -> 'Add':
        return Add(self.left.diff(var), self.right.diff(var))  # (f + g)' = f' + g'

    def __repr__(self) -> str:
        return f"({self.left} + {self.right})"


class Sub(Expr):
    """Subtraction operation (a - b)."""
    def __init__(self, left: Expr, right: Expr) -> None:
        self.left: Expr = left
        self.right: Expr = right

    def diff(self, var: 'Var') -> 'Sub':
        return Sub(self.left.diff(var), self.right.diff(var))  # (f - g)' = f' - g'

    def __repr__(self) -> str:
        return f"({self.left} - {self.right})"


class Mul(Expr):
    """Multiplication operation (a * b)."""
    def __init__(self, left: Expr, right: Expr) -> None:
        self.left: Expr = left
        self.right: Expr = right

    def diff(self, var: 'Var') -> 'Add':
        # Product rule: (f * g)' = f' * g + f * g'
        return Add(Mul(self.left.diff(var), self.right), Mul(self.left, self.right.diff(var)))

    def __repr__(self) -> str:
        return f"({self.left} * {self.right})"


class Div(Expr):
    """Division operation (a / b)."""
    def __init__(self, left: Expr, right: Expr) -> None:
        self.left: Expr = left
        self.right: Expr = right

    def diff(self, var: 'Var') -> 'Div':
        # Quotient rule: (f / g)' = (f' * g - f * g') / g²
        return Div(Sub(Mul(self.left.diff(var), self.right), Mul(self.left, self.right.diff(var))), Mul(self.right, self.right))

    def __repr__(self) -> str:
        return f"({self.left} / {self.right})"


class Pow(Expr):
    """Exponentiation operation (a ^ b)."""
    def __init__(self, base: Expr, exponent: Expr) -> None:
        self.base: Expr = base
        self.exponent: Expr = exponent

    def diff(self, var: 'Var') -> Union['Mul', 'Expr']:
        # Power rule: (x^n)' = n * x^(n-1)
        if isinstance(self.exponent, Const):  # Only handles constants as exponents
            return Mul(Mul(self.exponent, Pow(self.base, Const(self.exponent.value - 1))), self.base.diff(var))
        else:
            raise NotImplementedError("Only constant exponents are supported.")

    def __repr__(self) -> str:
        return f"({self.base} ^ {self.exponent})"


if __name__ == "__main__":
    x = Var("x")
    y = Var("y")  

    f = Add(Mul(Const(3), Pow(x, Const(2))), Mul(Const(2), x))  # f(x) = ( 3 * x * x ) + ( 2 * x )
    df_dx = f.diff(x)

    print(f"Function: {f}")
    print(f"Derivative df/dx: {df_dx}")