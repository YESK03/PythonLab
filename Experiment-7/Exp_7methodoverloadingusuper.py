class Base:
    def method1(self):
        print("Statement from Base Class")
        
        
class Derived(Base):
    def method1(self):
        super().method1()
        print("Statement from derived class")
        
        
obj = Derived()
obj.method1()
obj.method1()