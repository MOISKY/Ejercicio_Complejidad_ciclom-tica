#Un negocio vende productos y realiza envíos por mensajeria. El producto tiene un
#precio base de $125. Sin embargo:
#Si se adquieren más de 100 unidades se ofrece un descuento del 5%
#Si se adquieren más de 1000 unidades el descuento será de 10%.
#Sobre el precio, agregue el transporte que depende de cuántas cajas se requieran. Cada caja puede almacenar hasta 4 unidades
#y tiene un costo de 50 pesos. 
#El programa lee la cantidad de productos, calcula el precio total, el número de cajas y el descuento que se aplicó.
unidades = int(input("Ingrese numero de unidades"))
precio = 125 * unidades
descuento = 0
tipo_descuento = 0
precio_auxiliar = 0
precio_total = 0

numero_cajas,residuo_cajas = unidades // 4,unidades % 4
if residuo_cajas >= 1 and residuo_cajas <= 3:
    numero_cajas +=1


if unidades > 100:
    tipo_descuento = 0.05
    descuento = precio * tipo_descuento
elif unidades > 1000:
    tipo_descuento = 0.10
    descuento = precio * tipo_descuento


precio_total = precio - descuento + (numero_cajas * 50)
print("Precio total: ",precio_total)
print("Numero cajas: ",numero_cajas)
print("Descuento aplicado",tipo_descuento)