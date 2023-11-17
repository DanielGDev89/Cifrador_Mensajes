import csv

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

def cifrado_atbash(mensaje):
    mensaje_mayus = mensaje.upper()
    mensaje_cifrado = ""
    letras_claves = {"A":"Z",
                     "B":"Y",
                     "C":"X",
                     "D":"W",
                     "E":"V",
                     "F":"U",
                     "G":"T",
                     "H":"S",
                     "I":"R",
                     "J":"Q",
                     "K":"P",
                     "L":"O",
                     "M":"Ñ",
                     "N":"N",
                     "Ñ":"M",
                     "O":"L",
                     "P":"K",
                     "Q":"J",
                     "R":"I",
                     "S":"H",
                     "T":"G",
                     "U":"F",
                     "V":"E",
                     "W":"D",
                     "X":"C",
                     "Y":"B",
                     "Z":"A"}

    for caracter in mensaje_mayus:
        if caracter not in letras_claves:
            mensaje_cifrado += caracter
        else:
            mensaje_cifrado += letras_claves[caracter]
            
    return mensaje_cifrado

def validar_espia(destinatario):
    if len(destinatario) >= 5 and len(destinatario) <= 15 and validar_caracteres(destinatario):
        return True
    else:
        return False

def validar_caracter(caracter):
    caracteres = '_-.'
    if caracter.isalnum(): 
        return True
    elif caracter in caracteres:
        return True
    else:
        return False

def validar_caracteres(destinatario):
    for caracter in destinatario:
        if not validar_caracter(caracter):
            return False
    return True

def datos_en_csv(destinatario, cifrado, mensaje_cifrado):
    datos = [destinatario, cifrado, mensaje_cifrado]
    
    myfile= open('mensajes.csv','a',newline="")
    csvWriter=csv.writer(myfile)

    csvWriter.writerow(datos)

    myfile.close()