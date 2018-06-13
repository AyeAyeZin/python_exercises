class Other(object):
    def override(self):
        print("OTHER override()")
    def implicit(self):
        print("OTHER implicit()")
    def altered(self):
        print("OTHER altered()")
class Child(object):
    def _iit_(self):
        self.other=Other()
    def impliccit(self):
        self.other.iimplicit()
    def override(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")
son = Child()
