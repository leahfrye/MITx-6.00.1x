class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self.dict = {}
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        self.dict[k] = v
        
    def getval(self, k):
        """ k, immutable object  """
        return self.dict[k]
        
    def delete(self, k):
        """ k, immutable object """   
        del self.dict[k]
    
sample = myDict()
print(sample.assign(1, 2))
print(sample.delete(1))