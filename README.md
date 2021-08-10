# Switch
Switch-Case class for Python (before 3.10)

Usage:

```python
from switch import Switch

def say(): # You can set function as key or value!
    print("Hello World")

cases = { # define dictionary (dict) outside or as inline
    0: "Hello",
    1: "World"
    "Full": say # or say() to run immediately
}

example = Switch(cases) # Assignment is optional, and second argument is optionally, which defines **Default** key (you can assign or change ot later)

example.case(True, "Lol") # you can set new cases always, just please don't use **None** as key **and if key exists this will override it's value**

example.default = "Full" # set/change **default** key

example.switch(0) # will return *"Hello"*

example.switch(3) # This key doesn't exists and Switch will return value of default key (**Full**, as defined before) and this will return **say** function object, which you can run later

example # this will return current cases as below comment

# Switch(key):
#     Case(0): # or **Empty** if there are no **cases**
#         "Hello"
#     Case(1):
#         "World"
#     Case(True):
#         "Lol"
#     Default("Full"):
#         # say's object
```

## TODO
 - [ ] Make second variant of usage with decorators
 - [ ] Think about other additions :)
