class Other(object):
    def override(self):
        print("OTHER override()")
    def implicit(self):
        print("OTHER implicit()")
    def altered(self):
        print("OTHER altered()")
class Child(object):
    def _init_(self):
        self.other=Other()
    def implicit(self):
        print("CHILD BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")
son=Child()
son.implicit()
so.override()
son.altered()
