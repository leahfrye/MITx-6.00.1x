class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        commonVals = []
        print(other.vals)
        # for num in self.vals:
        #     if num not in other.vals:
        #         commonVals.append(c)
        
        return commonVals

values = intSet()
values.insert([-20,-17,-15,-12,-8,-3,3,12,13,16])

values2 = intSet()
values2.insert([-18,-9,-6,-4,-3,-2,0,5,8,18])

print(values.intersect(values2))        