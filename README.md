[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MuElT52l)
# Unidad 3
---
## Documentación del proyecto
Nombre: Felipe Gomez P 
ID:  000511279
---


Evaluación Programación

La idea inicial es crear un código de asistencia virtual de un restaurante por donde tu puedas ordenar tu comida y pedir el domicilio, este código le mostraría al usuario el menú del restaurante con las opciones de precio y el valor del domicilio dependiendo de la dirección.
	mostrar "Hola, bienvenido a (nombre del restaurante)
	mostrar " Por favor ingreresa la opción con la que desees continuar"
	mostrar " 1. Domicilio"
	mostrar " 2. Pedido para recoger en tienda"
	mostrar "3. Reclamo"
Aquí pedimos al usuario ingresar una de las opciones dadas y dependiendo de su elección el código va correr por una de las ramas
	x = print(int(" Elige una de las opciones " ))
	if x == 1 entonces
1. Si x = 1 el código le va a mostrar el menú con los precios de cada comida y bebida
2. Se le da la opción al usuario de escoger qué cosas del menú desea 
3. se solicita al usuario la información necesaria para el domicilio ( dirección, nombre de la unidad, apto, edificio, etc)
4. se le va a dar al usuario la opción de pagar por tarjeta, transferencia o efectivo
5. Como resultado se le va a devolver al usuario un resumen de su pedido, el valor total, método de pago, la confirmación de los datos para el domicilio y un aproximado de tiempo que se demora. 
	if  x == 2  entonces 
1. Si x = 1 el código le va a mostrar el menú con los precios de cada comida y bebida
2. Se le da la opción al usuario de escoger qué cosas del menú desea 
3. se le va a dar al usuario la opción de pagar por tarjeta, transferencia o efectivo
5. Como resultado se le va a devolver al usuario un resumen de su pedido, el valor total, método de pago.
	if x == 3 entonces 
1. Se le otorga al usuario un número para que contacten al callcenter y le resulvan la inquietud.
