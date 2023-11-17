def cifrado_atbash(mensaje):
    """
    >>> cifrado_atbash("Hola Mundo")
    SLOZ ÑFNWL
    >>> cifrado_atbash("Argentina Programa")
    ZITVNGRNZ KILTIZÑZ
    """
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
            
    print(mensaje_cifrado)

import doctest
print(doctest.testmod())