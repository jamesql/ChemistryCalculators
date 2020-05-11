
class Conversion:
    def __init__(self):
        self.atmconst = 1.01325
        self.mmhgconst =  0.0013332239
        self.kconst = 273.15
    
    def atm_to_bar(self, atm):
        nBar = atm * self.atmconst
        return nBar
    
    def mmhg_to_bar(self, mmhg):
        nBar = mmhg * self.mmhgconst
        return nBar
    
    def bar_to_atm(self, bar):
        nAtm = bar / self.atmconst
        return nAtm
        
    def bar_to_mmhg(self, bar):
        nMmhg = bar / self.mmhgconst
        return nMmhg
        
    def c_to_k(self, c):
        return (c + self.kconst)
        
    def k_to_c(self, k):
        return (k - self.kconst)

class Lussac:
    def __init__(self, temp, pressure):
        self.temp = temp
        self.pressure = pressure
        self.kval = (self.pressure / self.temp)
        self.tempType = "k"
        self.pType = "bar"
    
    def findNewPressure(self, newTemp):
        nPressure = ( (self.pressure * newTemp) / self.temp )
        self.pressure = nPressure
        return self
        
    def findNewTemp(self, newPressure):
        nTemp = ( (self.temp * newPressure) / self.pressure )
        self.temp = nTemp
        return self
    
def main():
    con = Conversion()
    
    problem_one = Lussac( con.c_to_k(22), con.atm_to_bar(135) ).findNewPressure(con.c_to_k(50))
    print(con.bar_to_atm(problem_one.pressure))
    
    problem_two = Lussac(  con.c_to_k(20), con.mmhg_to_bar(1900) ).findNewTemp(con.mmhg_to_bar(1750))
    print(con.k_to_c(problem_two.temp))
    
    problem_three = Lussac( 150, con.atm_to_bar(1) ).findNewPressure(300)
    print(con.bar_to_atm(problem_three.pressure))
    
main()
