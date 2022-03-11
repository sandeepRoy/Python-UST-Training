import zope.interface

class MyInterface(zope.interface.Interface):
    x = ''
    def method1(self, x):
        pass
    def method2(self):
        pass

@zope.interface.implementer(MyInterface)
class MyClass:
    def method1(self, x):
        return 'Sandeep Roy'
    def method2(self):
        return 'Nothing'
