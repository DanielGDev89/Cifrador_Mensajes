def cifrado_cesar(mensaje, clave):
    mensaje_mayus = mensaje.upper()
    mensaje_cifrado = ""

    for caracter in mensaje_mayus:
        if caracter == " " or caracter == "Ñ":
            mensaje_cifrado += caracter
        else:        
            caracter_unicode = ord(caracter)
            if caracter_unicode < 65 or caracter_unicode > 90:
                mensaje_cifrado += caracter
            elif caracter_unicode >= 65 and caracter_unicode <= 90:
                caracter_transformar = caracter_unicode + clave
                if caracter_transformar> 90:
                    caracter_transformar = caracter_transformar -26
                nueva_letra = chr(caracter_transformar)
                mensaje_cifrado += nueva_letra
    
    return mensaje_cifrado

print(cifrado_cesar('hola mundo', 3))