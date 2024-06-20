//We will use decorators to give our Fibaonnaci function more resources

//A decorator writes an inner wrapping function which takes any number of arguments, using this to call the given function
//The inner wrapping function is the return value of our decorator.

const decorator=(fn) =>{
    let wrap =(...args) =>{
        console.log("wrapping:", fn)
        let out=fn.apply(this, args)
        return out
    }
    return wrap
}
const fn = (n) => (n*(n+1))/2
const wrapFn = decorator(fn)
wrapFn(10)

const time = (fn) => {
    let timed = (...args) => {
      let start = new Date()
      let out = fn.apply(this, args)
      let end = new Date()
      console.log("Ran in", end-start, "ms")
      return out
    }
    return timed
  }
  const naive = n => {
    let total = 0
    for(let i=0;i<=n;i++) {
      total += i
    }
    return total
  }
  timeNaive=time(naive)
  timeNaive(1e9)

  const timeAsync = (fn) => {
    let timed = async (...args) => {
      let start = new Date()
      let out = await fn.apply(this, args)
      let end = new Date()
      console.log("Ran in", end-start, "ms")
      return out
    }
    return timed
  }

  timeAsyncNaive=timeAsync(naive)
  timeAsyncNaive(1e9)

  const sleep = async (time) => {
    console.log(`Sleeping ${time} ms`)
    await new Promise((resolve) => setTimeout(resolve, time))
    console.log("Waking up!")
  }

const timeSleep = timeAsync(sleep)
timeSleep(1000)

const memoize = (fn, keymaker = JSON.stringify) => {
    const lookupTable = new Map()
  
    return (...args) => {
      const key = keymaker(args)
      return lookupTable[key] || (lookupTable[key] = fn(...args))
    }
  }

  const fibonacci = (n) => {
    if(n === 1 || n === 2) return 1
    return fibonacci(n-1) + fibonacci(n-2)
  }

timeMemFib(41)
timeMemFib(41)

//Fast Functional Faultless Fibonacci
const fibonacciParam = (fibonacci, n) => {
  if(n === 1 || n === 2) return 1
  return fibonacci(fibonacci, n-1) + fibonacci(fibonacci, n-2)
}

const bigIntFibonacciParam = (fibonacci, n) => {
  if(n === 1 || n === 2) return BigInt(1)
  return fibonacci(fibonacci, n-1) + fibonacci(fibonacci, n-2)
}
const memBigIntFibParam = memoize(bigIntFibonacciParam)
const memBigIntFibonacci = (n) => memBigIntFibParam(memBigIntFibParam, n)
const timeMemBigIntFibonacci = timeAsync(memBigIntFibonacci)


