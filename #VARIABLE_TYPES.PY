variable=input("enter something")
print(type(variable))
print(id(variable))
del variable
print(variable)
  
  
output:
enter some thingsri
<class 'str'>
140315802844336
#here as the variable already deleted it is showing an error
Traceback (most recent call last):
  File "/home/o/variable.py", line 5, in <module>
    print(variable)
NameError: name 'variable' is not defined
