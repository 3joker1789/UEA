print("UNIVERSIDAD ESTATAL AMAZONICA")
str(input('Nombre Cliente:'))
str(input('Mes:'))
int(input('Año:'))
str(input('Institucion Bancaria: '))


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retiro(self, cantidad):
        self.__saldo -= cantidad

    def obtener_saldo(self):
        return self.__saldo


cuenta = CuentaBancaria("Juan", 15460)
cuenta.depositar(500)
cuenta.depositar(10000 * 12 / 100)
cuenta.retiro(1260)

print(cuenta.obtener_saldo())
print('ESTE ES SU SALDO ESTIMADO/A')
