class calcu:
    
    x = int(input("Enter Value of X"))  #Global Variable
    y = int(input("Enter Value of Y"))
    
    
    def Add(self):
        print("Addition",self.x + self.y)
        
        
    def Sub(self):
        print("Subtraction",self.x - self.y)
        
    def Mul(self):
        c = 2  # Local Variable
        print("Multiplication", (self.x * self.y) * c )
        
        
    def div(self):
        print("Division", self.x/self.y)
        
        
        
c = calcu()
c.Add()
c.Mul()
c.Sub()
c.div()
