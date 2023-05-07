from ClaseViajeroFrecuente import ViajeroFrecuente
import csv


class ManejadorViajero:
    __lista: list[ViajeroFrecuente]

    def __init__(self):
        self.__lista = []

    def cargar(self):
        archivo = open("Viajeros.csv")
        reader = csv.reader(archivo, delimiter=",")
        next(reader)
        for fila in reader:
            num = int(fila[0])
            dni = int(fila[1])
            nombre = fila[2]
            apellido = fila[3]
            millas = int(fila[4])
            viaj = ViajeroFrecuente(num, dni, nombre, apellido, millas)
            self.__lista.append(viaj)
        archivo.close()

    def funcion1(self):
        max = self.__lista[0]
        for obj in self.__lista:
            if obj > max:
                max = obj.cantidadTotaldeMillas
        print("Viajeros con Mayor Millas acumuladas \n")
        for obj in self.__lista:
            if obj.cantidadTotaldeMillas() == max:
                obj.mostrar()

    def funcion2_3(self):
        viajero = self.__lista[0]
        print("Instancia de la clase viajero: \n")
        viajero.mostrar()
        viajero += 1000
        print("\nSe acumularon nuevas millas, la nueva actualizacion es: \n")
        viajero.mostrar()
        print("\nA continuación se ha realizado el canje: \n")
        viajero -= 500
        viajero.mostrar()



