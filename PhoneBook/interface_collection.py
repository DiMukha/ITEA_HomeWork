class PhoneBookDictionary:

    def __init__(self, d={}):
        self._d = dict(d)

    def __repr__(self):
        return repr(self._d)

    def __setitem__(self, index, value):
        self._d[index] = value

    def __getitem__(self, index):
        return self._d[index]

    def __delitem__(self, index):
        del self._d[index]

    def __iter__(self):
        for i in self._d:
            yield i

    def items(self):
        return self._d.items()