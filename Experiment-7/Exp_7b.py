class base:
    def show(self):
        print("This is a base class method")
        
    def fint(self):
        print("Pyhton Programming for BCA 3rd sem")
        
    def wire(self):
        print("One type of snake is also called python")
        
class second(base):
    def disp(self):
        print("This is a second class method")
        

ob = second()
ob.wire()
ob.show()
ob.disp()
ob.fint()

