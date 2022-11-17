class MyClass(object):
    def __init__(self):
        print ("never called in this case")
    def __new__(cls):
        return 42

obj = MyClass()
print (obj)