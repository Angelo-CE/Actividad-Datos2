def romano(numero):
    """
    Convierte un número romano a número decimal.

    Entrada: cadena de caracteres con el número romano
    Salida: el número introducido, pero en decimal.
    """

    if isinstance(numero, str):
        romanChars = ["M", "D", "C", "L", "X", "V", "I"] # lista de caracteres romanos
        
        if not VerificaRomano(numero, romanChars):
        # si el número no es romano, retorna lo siguiente:
            return "La cadena debe ser un número romano (recuerde que el número romano se escribe en mayúscula)."
            
        romanCharsDic = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        # genera el diccionario para la traducción
        return TraduceRomano(numero, "", romanCharsDic)
        
    else:
        # especifica el error
        return "El dato introducido debe ser una cadena de caracteres."
        
        
def VerificaRomano(numero, romanChars):
    """
    Verifica que un número sea romano

    Entrada: el número romano y la lista de caracteres romanos.
    Salida: true si el número es romano, false si no lo es.
    """

    if numero == "":
    # si la cadena se revisó por completo, es romano.
        return True
        
    elif numero[0] in romanChars:
    # si el primero caracter es romano, continúa con el resto de la lista
        return VerificaRomano(numero[1:], romanChars)
        
    else:
    # en caso de no encontrar ningún caracter romano y todavía hay elementos en la lista,
    # significa que el número no es romano.
        return False
        
def TraduceRomano(numero, lastChar, romanCharsDic):
    """
    Convierte un número romano utilizando un diccionario que convierte de romano a decimal.

    Entrada: el número romano, el último caracter revisado y el diccionario de números romanos con su valor decimal respectivo.
    Salida: una suma recursiva de números en una pila.
    """

    if numero == "":    # si el número romano ya se recorrió por completo:
        return 0        # añade 0 a la suma, como valor neutro.
    elif lastChar == "" or romanCharsDic[numero[0]] <= romanCharsDic[lastChar]: 
    # si el último dígito está vacío, es porque se está revisando el primer caracter del 
    # número romano. O que si el número anterior (romanCharsDic[lastChar]) es mayor que el 
    # número actual (romanCharsDic[numero[0]]), entonces se haga una suma normal.
        return romanCharsDic[numero[0]] + TraduceRomano(numero[1:], numero[0], romanCharsDic) 
        # la suma recursiva. "romanCharsDic[numero[0]]" obtiene el número equivalente al caracter 
        # en revisión (numero[0]) y obtiene su valor en el diccionario 
        # ejemplo, si numero = "XII", numero[0] = "X", en el diccionario "X" retorna 10.
    else:
        # aquí entra cuando el número actual es mayor que el anterior, por lo tanto, significa 
        # que se debe hacer una resta (por ejemplo, el número IX significa 9 en romano
        # porque I resta 1 a X que es 10 y 10-1 es 9).
        return -(romanCharsDic[lastChar]*2) + romanCharsDic[numero[0]] + TraduceRomano(numero[1:], numero[0], romanCharsDic)
        # como el número anterior se sumó en la recursión anterior, debemos restarlo dos 
        # veces, pues no solo debe quitarse, sino que quitar su valor. Por tanto, lo hacemos 
        # negativo y multiplicamos por 2. Al final, sumamos el número actual y procedemos con 
        # la recursión.

# ejemplos de ejecución.


#Se agregan ejemplos de ejecucion

print("Romano XXXX: ")+str(romano("XXXX"))
print("Romano XIX: " + str(romano("XIX")))
print("Romano XX: " + str(romano("XX")))







