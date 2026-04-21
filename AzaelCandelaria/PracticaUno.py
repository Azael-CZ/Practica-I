class Hambuguesa:
    # Crear el init y la clase
    def __init__ (self, id, nombre, precio, stock, descuento, ingredientes=[]):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__descuento = descuento
        self.__ingredientes = ingredientes

    # Funcion Info(Imprimir la informacion de la hamburguesa)
    def info (self):
        print(f"--Detalles de la hamburguesa-- \nLa hamgurguesa {self.__nombre} tiene un precio de {self.__precio} \nSu ID es: {self.__id} y hay en el stock {self.__stock} piezas")
        if self.__descuento >= 1 and self.__descuento <=100:
            print(f"La hamburguesa tiene un descuento de {self.__descuento}%")
        else:
            print("No tiene un descuento actualmente")

    # Funcion Valor_inventario(Calcular el precio * el stock)
    
    # Funcion Precio_descuento(Calcular el precio si tiene descuento)

    # Funcion Ingredientes(Imprimir los ingredientes de la hamburguesa)


    # Gets y Sets

    # Menu breve