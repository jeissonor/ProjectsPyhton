class cuentasCorrientes():
    numeroDeCuenta=''
    titularDeLaCuenta=''
    saldoCuenta=0
    retiroCuenta=0
    ingresandoDinero=0

    def __init__(self,numeroDeCuenta,titularDeLaCuenta,saldoCuenta,retiroCuenta,ingresandoDinero):
        self.numeroDeCuenta=numeroDeCuenta
        self.titularDeLaCuenta=titularDeLaCuenta
        self.saldoCuenta=saldoCuenta
        self.retiroCuenta=retiroCuenta
        self.ingresandoDinero=ingresandoDinero

    def metodoGetter(self):
        return 'El titular de la cuenta es:' ,self.titularDeLaCuenta ,' y el saldo de la cuenta es ',\
            self.saldoCuenta,'El retiro de la cuenta es:',self.retiroCuenta, 'El ingreso de la cuenta es',self.ingresandoDinero,\
            self.numeroDeCuenta,'Su cuenta es corriente'
    
    def ingresoDinero(self):
        return self.ingresandoDinero
    def retiroDinero(self):
        return self.retiroCuenta   


Jeisson=cuentasCorrientes(6575674,'Jeisson Ortega Diaz',2000,30000,2000)
print(Jeisson.metodoGetter())
