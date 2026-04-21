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
    def valor_inventario(self):
        inventario = self.__precio * self.__stock
        return inventario
    
    # Funcion Precio_descuento(Calcular el precio si tiene descuento)
    def precio_descuento(self):
         if self.__descuento >= 1 and self.__descuento <=100:
            precio_final = self.__precio - ((self.__descuento * self.__precio) / 100) 
            return precio_final
         else:
             print("No tiene descuento")

    # Funcion Ingredientes(Imprimir los ingredientes de la hamburguesa)
    def ingredientes(self):
        for ingredientes in self.__ingredientes:
            print(f"{ingredientes}", end="/ ")
        print("")

    # Gets y Sets
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_precio(self):
        return self.get_precio
    def set_precio(self, precio):
        self.__precio = precio

    def get_stock(self):
        return self.__stock
    def set_stock(self, stock):
        self.__stock = stock

    def get_descuento(self):
        if self.__descuento >= 1 and self.__descuento <=100:
            return self.__descuento
        else:
             print("Tiene un descuento invalido, ingrese otro")
    def set_descuento(self, descuento):
            self.__descuento = descuento

# Las hamburguesas hechas desde el programa
Sencilla = Hambuguesa(100, "Sencilla", 80, 20, 10, ['Pan', 'Carne', 'Queso amarillo', 'Lechuga', 'Catsup', 'Mostaza'])
Choriburguer = Hambuguesa(101, "Choriburguer", 100, 35, 0, ['Pan', 'Carne', 'Chorizo', 'Queso blanco', 'Jalapeño', 'Cebolla'])
Chikenburguer = Hambuguesa(102, "Chikenburguer", 120, 40, 20, ['Pan', 'Pechuga empanizada', 'Cebolla', 'Lechuga', 'Tocino'])

    # Menu breve
while True:
    print(f"\n\n\n\nBienvenido a WcDonal's, ¿Que desea hacer? \n1.- Ver el menu completo \n2.- Info de la hamburguesa sencilla \n3.- Info de la hamburguesa choriburguer \n4.- Info de la hamburguesa de pollo \n5.- Salir")
    opcion = int(input("Ingresa tu opcion: "))
    print("\n\n")
    match opcion:
        case 1:
            Sencilla.info_menu()
            Sencilla.ingredientes()            
            Choriburguer.info_menu()
            Choriburguer.ingredientes() 
            Chikenburguer.info_menu()
            Chikenburguer.ingredientes() 

        case 2:


        case 3:


        case 4:

        case 5:
            print("Tenga buen dia ☺")
            break