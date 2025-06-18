class class_sum:
    math=0
    eng=0
     
    def set_score(self, math, eng):
        self.math = math
        self.eng = eng
        return
    
    def do_sum(self):
        return(self.math+self.eng)