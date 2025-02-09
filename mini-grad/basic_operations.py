from typing import Union

class Tensor:
    def __init__(self, data: Union[int, float]):
        self.data = data
    
    def __repr__(self) -> str:
        return f"Tensor({self.data})"
    
    def _add(self, other: 'Tensor') -> Union[int, float]:
        return self.data + other.data
    
    def _sub(self, other: 'Tensor') -> Union[int, float]:
        return self.data - other.data
    
    def _mul(self, other: 'Tensor') -> Union[int, float]:
        return self.data * other.data
    
    def _div(self, other: 'Tensor') -> Union[int, float]:
        return self.data / other.data
    
    def __add__(self, other: Union[int, float, 'Tensor']) -> Union[int, float]:
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._add(other)
    
    def __radd__(self, other: Union[int, float, 'Tensor']) -> Union[int, float]:
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._add(other)
    
    def __sub__(self, other: Union[int, float, 'Tensor']) -> Union[int, float]:
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._sub(other)
    
    def __rsub__(self, other: Union[int, float, 'Tensor']) -> Union[int, float]:
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._sub(other)
    
    def __mul__(self, other: Union[int, float, 'Tensor']) -> Union[int, float]:
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._mul(other)
    
    def __rmul__(self, other: Union[int, float, 'Tensor']) -> Union[int, float]:
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._mul(other)
    
    def __truediv__(self, other: Union[int, float, 'Tensor']) -> Union[int, float]:
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._div(other)
    
    def __rtruediv__(self, other: Union[int, float, 'Tensor']) -> Union[int, float]:
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._div(other)
    
    def backward(self) -> None:
        raise NotImplementedError("Subclass must implement backward method")

if __name__ == '__main__':
    t1 = Tensor(3)
    t2 = Tensor(5)

    print(t1, t2)
    print(t1._add(t2))
    print(t1 + t2)