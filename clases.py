
class nuevas_var:
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self.var2=var2
        self.var3=var3
    def fit(self):
        diff=self.var1-self.var2
        suma=self.var1+self.var2
        mult=self.var1*self.var2
        imc=self.var1/(self.var2/100)**2
        div=self.var1/self.var2
        return [self.var1,self.var2,self.var3,diff,suma,mult,imc,div]
if __name__ == "__main__":
    print('ejecuta esto')
    nuevas_var

