def decorator_function(original_function):
  def wrapper_function(*args,**kwargs):
    print('wrapper executed this before {}'.format(original_function.__name__))
    return original_function(*args,**kwargs)
  return wrapper_function

#This call 1
print("Decorator underlying form")
def display():
  print("Hello there this is dell")
dc=decorator_function(display)
dc()

#This is call2
print(" ")
print("Decorator Form")
@decorator_function
def display():
  print("Hello there this is dell")
display()

#this is call3 
print(" ")
print("Passing arguments into decorator function")
@decorator_function
def display_info(name,age):
  print(f"Display info ran with arg {name} {age}")

display_info("ganesh",22)