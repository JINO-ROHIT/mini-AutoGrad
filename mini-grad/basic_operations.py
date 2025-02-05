class Tensor:

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return f"Tensor({self.data})"
    
    def _add(self, other):
        return self.data + other.data
    
    def _sub(self, other):
        return self.data - other.data
    
    def _mul(self, other):
        return self.data * other.data
    
    def _div(self, other):
        return self.data / other.data
    
    def __add__(self, other):
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._add(other)
    
    def __radd__(self, other):
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._add(other)
    
    def __sub__(self, other):
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._sub(other)
    
    def __rsub__(self, other):
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._sub(other)
    
    def __mul__(self, other):
        if not isinstance(other, Tensor):
            other = Tensor(other)

        return self._mul(other)
    
    def __rmul__(self, other):  # Handles `3 * x`
        if not isinstance(other, Tensor):
            other = Tensor(other)

        return self._mul(other)
    
    def __truediv__(self, other):
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._div(other)
    
    def __rtruediv__(self, other):
        if not isinstance(other, Tensor):
            other = Tensor(other)
        return self._div(other)
    
    def backward(self):
        raise NotImplementedError("Subclass must implement backward method")



if __name__ == '__main__':
    t1 = Tensor(3)
    t2 = Tensor(5)

    print(t1, t2)
    print(t1._add(t2))
    print( t1 + t2 )
