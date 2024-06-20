# We will use decorators to give our Fibaonnaci function more resources
import time, asyncio, functools
# A Basic "Decorator"
def functionA(n):
    print("Here is n:", n)

functionA(4)
# A decorator writes an inner wrapping function which takes any number of arguments, using this to call the given function
# The inner wrapping function is the return value of our decorator.
def decorator(function):
    def wrapper(arg1):
        print("wrapping:", function)
        print(function(arg1))
    return wrapper

def fn(n):
    num=(n*(n+1))/2
    return num

decorate=decorator(fn)
decorate(10)

#Wrapper is compatible with any function, it prints a log and calls the original function with arguments passed to it
#the decorator function returns wrap and then uses wrap in place of fn


#We can measure how long a function takes with the timeIt decorator
def timeIt(function):
    def timed(*args):
        start=time.time()
        for i in args:
            print(function(i))
        end=time.time()
        print("Ran in", end-start, "ms")
    return timed



#As an example, here's a function that adds the numbers 1 to n naively

def naive(n):
    total=0
    for i in range(n):
        total+=i
    return total

#The naive function gets slower and eventually stops working when you use large enough integers
#Use the timeIt decorator to measure this effect
timeNaive=timeIt(naive)
timeNaive(10000000)
timeNaive(int(1e9))
#timeNaive(int(1e9)) ran in 41.76961064338684 ms

async def timeAsync(function):
    async def timed(*args):
        start=time.time()
        for i in args:
           out= await function(i)
        end=time.time()
        print(out)
        print("Ran in", end-start, "ms")
        return out
    return timed

async def naive_async(n):
    total=0
    for i in range(0, n):
        total+=i
    return total

async def main(n):
    timer_async_naive=await timeAsync(naive_async)
    await timer_async_naive(int(n))

asyncio.run(main(1e9))

# Let's use an improved timing decorator
from datetime import datetime

def timed(func):
    """
    Wrap a function in a timer.
    """
    def timed_func(*args, **kwargs):
        now = datetime.now
        s_0 = now()
        value = func(*args, **kwargs)
        s_1 = now()
        print(value)
        print('%s' % (s_1 - s_0))
        return value
    return timed_func




#Memoization can allow us to cache function calls according to their arguments
#The technique trades space for time, and can make code run faster

memory={}
def memoize(f):
    def lookup(*num):
        for i in num:
            if i not in memory:
                memory[i]=f(i)
        return memory[i]
    return lookup

#Let's make a new fibonacci method to test this decorator
@functools.cache
def fibonacci(num):
    if num==1 or num==2: #these are our base cases
        return 1
    else: #to compute Fn, you add Fn-1 and Fn-2
        fn1= fibonacci(num-1) #use a recursive algorithm to get Fn-1 and Fn-2
        fn2=fibonacci(num-2)
        Fn=fn1+fn2 #add the resulting values together and return the result
        return Fn
    
    
    
#timeMemFib=timeIt(memoize(fibonacci))
timeMemFib=timed(fibonacci)
timeMemFib(40)
timeMemFib(40)

#We can see a stark difference:
# The first timeMemFib ran in 13.217664003372192 ms
# The second timeMemFib ran in 0.00038051605224609375 ms

#Unfortunately, this only memoizes the final answer, so computing fibonacci(39) would still take a while

#Once Decorator: Runs a function exactly once

def once(fn):
    def wrap(args):
        if wrap.has_run==False:
            wrap.has_run=True
            return fn(args)
        wrap.has_run=False
    return wrap
            

#Throttle Decorator: Calls a function only so often

def throttle(fn, interval):
    timeSinceLastExecution=time.time()-lastTime
    def wrap(args):
        if(lastTime or timeSinceLastExecution<=interval):
            fn(args)
            lastTime=time.time()
    return wrap



#Let's try some Fast Functional Faultless Fibonacci

#This uses parameterization since the function itself is now a parameter
#Once the function is memoized, each recursive call takes advantage of the memo table
#This approach is VERY fast
@functools.cache
def fibonacciParam(fibonacci, num):
    if num==1 or num ==2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)



timeMemoizedFibonacci=timed(fibonacciParam)
timeMemoizedFibonacci(fibonacci, 78)
timeMemoizedFibonacci(fibonacci, 100)
timeMemoizedFibonacci(fibonacci, 1000)

#timeMemoizedFibonacci=timeIt(fibonacciParam(78))
