import barcode
from barcode.writer import ImageWriter

# Definir el contenido que va a tener el contenido de barras
number = input("Ingrese 12 dígitos para el código de barras:")

# Verificar si el número es de 12 caracteres
if len(number) == 12:
    print("Generando Codigo de barras...")

    # Definir el formato de código de barras
    FormatoBarCode = barcode.get_barcode_class("upc")

    # Generamos la imagen del código de barras
    MyBarcode = FormatoBarCode(number, writer=ImageWriter())

    # Guardar imagen del código de barras
    MyBarcode.save("Barcode.png")

    print("El código de barras se generó correctamente")
else:
    print("El número ingresado no es de 12 dígitos")
