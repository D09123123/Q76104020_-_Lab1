import random
class Nine_Coins:
    def __init__(self, decimal):
        self.decimal = decimal
        self.binary = str(bin(self.decimal))[2:].zfill(9)         #change decimal into binary, fill the digits to 9 
        self.HT = ""                                                  
        for i in range(9):                                        #change binary to Head or Tail (0=H, 1=T)
            if self.binary[i] == "0":
                self.HT += "H"
            elif self.binary[i] == "1": 
                self.HT += "T"
        
        
    def toss(self):
        self.HT = ""
        self.binary = ""
        self.decimal = 0
        for i in range(9):                                        #toss the coin 9 times. the result is random.
            self.HT += random.choice(["H","T"])                   #record the result
        for i in range(9):                                        #change Head or Tail into binary (H=0, T=1)
            if self.HT[i] == "H":
                self.binary += "0"
            elif self.HT[i] == "T":
                self.binary += "1"
        for i in range(9):                                        #change binary to decimal by mathematics
            self.decimal += 2**(8-i)*int(self.binary[i])
    def __str__(self):
        return f"binary: {self.binary} and decimal : {self.decimal}"
    def __repr__(self):
        return ('Nine_Coins :"'+ self.HT +'"')
    