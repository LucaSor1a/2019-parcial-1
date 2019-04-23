
equi = {
    10 : 'A',
    11 : 'B',
    12 : 'C',
    13 : 'D',
    14 : 'E',
    15 : 'F'
}


def hexa(nume):
    final = '' 

    #Repite el proceso hasta que no pueda dividirse el numero en mas partes enteras
    while True:

        #Toma el resto de la division
        result = nume % 16

        #Si el resto es alguno de los que esta en el diccionario definido  entonces lo reemplaza al numero por su letra correspondiente
        if result in equi:
            final += equi[result]
        else:
            final += str(result)

        #Toma la parte entera de la division
        nume = int(nume/16)

        #Si la parte entera llega a 0 entonces termina el bucle
        if nume == 0:
            break
    

    #Ordena el numero hexadecimal
    final = final[::-1]
    return final