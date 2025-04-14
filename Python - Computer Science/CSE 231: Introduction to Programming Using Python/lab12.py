#################################
# CSE 231
# Lab 12
#################################

import math 

class Vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '{:.2f} {:.2f}'.format(self.x, self.y)
    
    def __repr__(self):
        shell_str = str(self.x) + str(self.y)
        
        return shell_str
    
    def __add__(self, v2):
        if type(v2) != Vector:
            v2 = Vector(v2)
        
        c = self.x + v2.x
        d = self.y + v2.y
        
        new_v = Vector(c,d)
        return new_v
    
    def __sub__(self, v2):
        if type(v2) != Vector:
            v2 = Vector(v2)
        
        c = self.x - v2.x
        d = self.y - v2.y
        
        new_v = Vector(c,d)
        return new_v
    
    def __mul__(self, val):
        if type(val) == float or type(val) == int: # scalar product
            c = self.x * val
            d = self.y * val
            return Vector(c,d)
        else: # dot product
            if type(v2) != Vector:
                val = Vector(val)
            dot = (self.x * val.x) + (self.y * val.y)
            return dot
    
    def __rmul__(self, v2): ?
        if type(val) == float or type(val) == int: # scalar product
            c = self.x * val
            d = self.y * val
            return Vector(c,d)
        else: # dot product
            if type(v2) != Vector:
                val = Vector(val)
            dot = (val.x * self.x) + (val.y * self.y)
            return dot
        
    def __eq__(self, v2):
        # v1 == v2 ?
        if type(v2) != Vector:
            v2 = Vector(v2)
        if self == v2:
            return True
        else:
            return False
     
    def magnitude(self):
         return math.hypot(self.x,self.y)
     
    def unit(self):
        mag = self.magnitude()
        if mag != 0:
            1/(mag)
        else:
            print('Cannot convert zero vector to a unit vector')
    
# for testing purposes: 
    
a = Vector()
print(a)
print(a.unit())

b = Vector(2,1)
vect2 = Vector(1,3)
c = b + vect2
print(c)



        
        