class Parent(object):
    def overide(self):
        print("PARENT override()")
class Child(Parent):
    def override(self):
        print("CHILD override()")
dad=Parent()
son=Child()
dad.override()
son.override()
