# with decorator 

import time

def performance(f):
    t1=time.time()
    def fn(*args,**kw):
        # print 'call'+f.__name__+'()' if (args==None and kw==None) else 'call'+f.__name__+str(args)
        t2=time.time()
        t=t2-t1
        print 'call'+f.__name__+'() in'+str(t)
        return f(*args,**kw)
    return fn

@performance
def factorial(n,b):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10,2)


'''


import time

def performance(unit):
    t1=time.time()
    def per_decorator(f):
        def wrapper(*args,**kw):
            t2=time.time()
            t=t2-t1
            print "call %s()...  %f %s "%(f.__name__,t,unit)
            return f(*args,**kw)
        return wrapper
    return per_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)


'''
'''
import time, functools

def performance(unit):
    t1=time.time()
    def per_decorator(f):
        @functools.wraps(f)
        def wrapper(*argw,**kw):
            t2=time.time()
            t=t2-t1
            print f.__name__+'() calling  in  '+str(t)+unit
            return f(*argw,**kw)
        return wrapper
    return per_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
    
# factorial(5)

print factorial.__name__
'''
'''
################################################## with class #################################################

class Any(object):
    def __getattr__(self,name):
        def methods(*args):
            if args!=None:
                print(name+str(args))
            else:
                print(name)
        return methods

a=Any()
a.hello('goodbye')
a.goodbye()
a.goodbye('dead meat','you are dead meat')


#*******************************************

class Illusion(object):
    def __getattr__(self, method):
        def proc(*args):
            if args != None:
                print(method + str(args))
            else:
                print(method)
        return proc

if __name__ == '__main__':
    illusion = Illusion()
    illusion.foo()
    illusion.dream('land on Mars')
    illusion.foo('bar', 'buzz')
    illusion.memo_fib(10)

    # The following instance exposes the defficiency of our Illusion class,
    # that arguments of method should have their runtime value. Try a method
    # call with undefined arguments and see what would happen. e.g.
    #
    #     illusion.evaluate(undefined_exp, undefined_env)
    #
    # Do you know why it is that case?
    exp = 'exp'
    database = []
    illusion.query(exp, database)

#************************************


class Fuck():
	def __getattr__(self, name):
		def suck(*arguments):
			l = [name] if arguments is None else [name] + list(arguments)
			print l
	return suck



'''
