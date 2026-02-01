from array import array as _array

class Array:
    """A minimal fixed-size array wrapper.

    Provides __len__, __getitem__, and __setitem__ so it behaves like a simple array
    for the book's examples.
    """
    def __init__(self, max_size, typecode='l'):
        if max_size < 0:
            raise ValueError("max_size must be >= 0")
        self._size = max_size
        self._typecode = typecode
        # initialize with zeros
        self._elements = _array(typecode, [0] * max_size)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError('Index out of range')
        return self._elements[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError('Index out of range')
        self._elements[index] = value

    def __repr__(self):
        return f"Array({list(self._elements)})\n"