class KSEC:
    X = 10 #Global Varaible
    def Name(self):
        Y = 100   #Local Varaible
        print("Value of X:",self.X+Y)
    
    
    def Proj(self):
        Y = 200
        print(self.X+Y)
        
    def Proj1(self):
        Y = 300
        print("Showing multiplication",self.X * Y)


Shu = KSEC()
Shu.Name()
Shu.Proj()
Shu.Proj1()
        

