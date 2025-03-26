############################
# CSE 231
# Lab #11 - Part B
############################

# CLASS TIME DEFINITION (clock.py source code)

class Time(object):
    def __init__(self, hr=0, min=0, sec=0):
        ''' create time object with 3 integers '''
        self.__hour = hr
        self.__mins = min
        self.__secs = sec


    def __repr__(self):
        ''' return string with formal representation of a Time
            Formatted to be 2 digits wide and include leading zeroes if needed '''
            
        frml_str = 'Class Time: {:02d}:{:02d}:{:02d}' \
                .format(self.__hour,self.__mins,self.__secs)
        
        return frml_str
        
    def __str__(self):
        ''' Return a string with hh:mm:ss format '''
            
        out_str = '{:02d}:{:02d}:{:02d}'.format(self.__hour,self.__mins,self.__secs)
        
        return out_str
    
    def from_str(self, out_str):
        ''' Update a Time object after creation
            Takes a string and assigns string components to instance variables'''
        hms_list = out_str.split(':')
        #print(hms_list)
        self.__hour = int(hms_list[0])
        self.__mins = int(hms_list[1])
        self.__secs = int(hms_list[2])



# DEMONSTRATION PROGRAM (clockDemo.py source code)

A = Time( 12, 25, 30 )

print( A )
print( repr( A ) )
print( str( A ) )
print()

B = Time( 2, 25, 3 )

print( B )
print( repr( B ) )
print( str( B ) )
print()

C = Time( 2, 25 )

print( C )
print( repr( C ) )
print( str( C ) )
print()

D = Time()

print( D )
print( repr( D ) )
print( str( D ) )
print()

D.from_str( "03:09:19" )

print( D )
print( repr( D ) )
print( str( D ) )
