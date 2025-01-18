var_global = 'This is a global variable'
def example():
    var_global = 'This is a local variable'
    return f'{var_global}'

def another_example():
    global var_global
    var_global = 'now var_global is me'
print(var_global)
print(f"The local variable don't change the global variable: {example()}")
another_example()
print(f"Unless we call the global variable inside the function: {var_global}")