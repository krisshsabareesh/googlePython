
list = ['aa', 'BB', 'zz', 'CC']
print 'Direct Sorted', sorted(list) #case sensitive
print list

print 'reverse sorted :', sorted(list, reverse=True)

strs = ['ccc', 'aabc', 'aaaa', 'd', 'bb']
print sorted(strs,key=len)


def myFn(s):
	return s[-1]

strs = ['xc', 'zb', 'yd', 'wa']
print sorted(strs, key=myFn)
btrs = strs.sort()
print btrs
print strs

tuple = (1, 2, 'hi')
print len(tuple)  ## 3
print tuple[2]    ## hi
####  tuple[2] = 'bye'  ### NO, tuples cannot be changed

tuple = ('Hi',)   #To create a size 1, tuple the lone element must be followed by comma

(x, y, z) = ( 33, 24, 'Hike')
print x, y, z

nums = [1, 2, 3, 4]
squares = [n * n for n in nums]
print squares 

strs = ['hello', 'and', 'good bye']
shouting = [s.upper() + '!!!' for s in strs]
print shouting

fruits = ['Apple', 'Banana', 'Cherry', 'Lemon', 'Goa']
#efruits = [for s in fruits if 'e' in s]  This is invalid
efruits = [s.upper() for s in fruits if 'e' in s]

print efruits
