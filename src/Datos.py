
def main():

    # Menú de restaurante 
    
    menu = {
        "comidas": [
            {"nombre": "Metallica Burger", "descripcion": "Pan brioche, doble carne de res, queso cheddar, tocino crujiente, cebolla caramelizada, salsa BBQ picante y jalapeños.", "valor": 30000},
            {"nombre": "Led Zeppelin Special", "descripcion": "Pan integral, carne de cordero, queso feta, espinacas, tomate, cebolla roja y salsa tzatziki.", "valor": 28000},
            {"nombre": "Guns N' Roses Burger", "descripcion": "Pan clásico, carne de res, queso suizo, champiñones salteados, lechuga, tomate y mayonesa de ajo.", "valor": 25000},
            {"nombre": "AC/DC Thunder Burger", "descripcion": "Pan de pretzel, carne de cerdo desmenuzada, queso pepper jack, cebolla frita, salsa de mostaza y miel, y pepinillos.", "valor": 27000},
            {"nombre": "Nirvana Veggie Burger", "descripcion": "Pan de centeno, hamburguesa de garbanzos, queso gouda, lechuga, tomate, cebolla roja y salsa de aguacate.", "valor": 28000},
            {"nombre": "Pink Floyd Psychedelic Burger", "descripcion": "Pan de ajonjolí, carne de res, queso azul, rúcula, cebolla morada, mermelada de higos y mayonesa trufada.", "valor": 32000},
            {"nombre": "Queen Royale Burger", "descripcion": "Pan brioche, carne de wagyu, queso brie, rúcula, champiñones portobello y salsa de vino tinto.", "valor": 25000},
            {"nombre": "Rolling Stones Spicy Burger", "descripcion": "Pan clásico, carne de res con chorizo, queso cheddar, jalapeños, lechuga, tomate, cebolla morada y salsa chipotle.", "valor": 29000}
        ],
        "bebidas": [
            {"nombre": "Iron Maiden Ale", "descripcion": "Cerveza rubia tipo ale, con notas a malta y un suave toque a cítricos, final ligeramente amargo. Graduación alcohólica: 4.7%.", "valor": 8000},
            {"nombre": "Black Sabbath Stout", "descripcion": "Cerveza negra tipo stout, con sabores intensos a café, chocolate amargo y un toque de vainilla. Graduación alcohólica: 6.5%.", "valor": 8000},
            {"nombre": "The Doors IPA", "descripcion": "Cerveza tipo IPA, con un amargor marcado, aroma a lúpulo fresco, notas de pino y frutas tropicales. Graduación alcohólica: 7.2%.", "valor": 8000},
            {"nombre": "Deep Purple Lager", "descripcion": "Cerveza lager clara, de cuerpo ligero y refrescante, con notas sutiles de malta y un final ligeramente dulce. Graduación alcohólica: 5.0%.", "valor": 8000},
            {"nombre": "Red Hot Chili Peppers Spicy Beer", "descripcion": "Cerveza especial con infusión de chile, un toque picante equilibrado con malta tostada y un suave amargor. Graduación alcohólica: 5.8%.", "valor": 8000}
        ]
    }
    
    def mostrar_menu():
        print("Menú de Comidas:")
        for i, comida in enumerate(menu["comidas"], start=1):
            print(f"{i}. {comida['nombre']} - {comida['valor']} COP")
        
        print("\nMenú de Bebidas:")
        for i, bebida in enumerate(menu["bebidas"], start=1):
            print(f"{i}. {bebida['nombre']} - {bebida['valor']} COP")
    
    def realizar_pedido():
        mostrar_menu()
        
        # Aqui se le pide al usuario escoger la comida
        comida_idx = int(input("Selecciona el número de la comida que deseas: ")) - 1
        comida_elegida = menu["comidas"][comida_idx]
        
        # Aqui la bevida que desea
        bebida_idx = int(input("Selecciona el número de la bebida que deseas: ")) - 1
        bebida_elegida = menu["bebidas"][bebida_idx]
        
        # Esta hecho para pedirle los datos al usuario, en este caso el nombre
        nombre_cliente = input("Ingresa tu nombre: ")
        
        # Aqui se le da la opcion de escoger que tipo de pedido es, si es para recoger en tienda, domicilio o reclamo
        print("1. Domicilio\n2. Pedido para recoger en tienda\n3. Reclamo")
        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 1:
            direccion = input("Ingresa la dirección de domicilio: ")
            metodo_pago = input("Método de pago (Tarjeta, Transferencia, Efectivo): ")
            print(f"\nResumen del Pedido para {nombre_cliente}:")
            print(f"Comida: {comida_elegida['nombre']} - {comida_elegida['valor']} COP")
            print(f"Bebida: {bebida_elegida['nombre']} - {bebida_elegida['valor']} COP")
            total = comida_elegida['valor'] + bebida_elegida['valor'] + 5000  # Este es el costo del domicilio
            print(f"Valor Total: {total} COP (incluye domicilio)")
            print(f"Pago con: {metodo_pago}")
            print(f"Enviado a: {direccion}")
        elif opcion == 2:
            metodo_pago = input("Método de pago (Tarjeta, Transferencia, Efectivo): ")
            print(f"\nResumen del Pedido para {nombre_cliente}:")
            print(f"Comida: {comida_elegida['nombre']} - {comida_elegida['valor']} COP")
            print(f"Bebida: {bebida_elegida['nombre']} - {bebida_elegida['valor']} COP")
            total = comida_elegida['valor'] + bebida_elegida['valor']
            print(f"Valor Total: {total} COP")
            print("Recoger en tienda")
        elif opcion == 3:
            print("Por favor, comunícate con nuestro call center para resolver tu reclamo.")
    
    # Aquí se ejecuta el programa siendo lo siguiente lo primero que le aparece al usuario 
    print("Hola, bienvenido a Rock Burger!")
    realizar_pedido()
    
    
if __name__ == "__main__":
    main()
