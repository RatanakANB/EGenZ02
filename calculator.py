import math
from logger import log_action

def add(a, b):
    result = a + b
    log_action("add", result)
    return result

def subtract(a, b):
    result = a - b 
    log_action("subtract", result)
    return result

def multiply(a, b):
    # TODO: {#{5}} Member 02: Implement multiplication
    pass

def divide(a, b):
    if (b==0):
        raise ValueError ("Cannot divide by Zero")
    result = a/b
    log_action("divide", result)
    return result

def power(a, b):
    # TODO: {#{6}} Member 03: Implement power (a^b)
    pass

def sum_n(*args):
    result = sum(args)
    log_action("sum_n", result)
    return result

def logarithm(a, base=10):
    # TODO: {#{7}} Member 04: Implement logarithm
    pass

def modulo(a, b):
#{8}} Member 05: Implement modulo
    result = a % b
    log_action("modulo", result)
    return result    

def sq_root(a):
    # TODO: {#{10}} Member 05: Implement square root
    pass

def factorial(n):
    # TODO: {#{9}} Member 06: Implement factorial
    result = math.factorial(int(n))
    log_action("factorial", result)
    reaturn result
    
>>>>>>> 3d23a63 (feat: implement factorial() {#{9}})

def absolute(a):
    # TODO: {#{11}} Member 06: Implement absolute value
    pass
