from hexa import hexa

class Not_in_range_exception(Exception):
    pass

class Not_a_number_exception(Exception):
    pass



#Sacar # del comentario para usarlo fuera de los test
#inp = input("Ingrese un numero entre 0 y 4095: ")




def interfaz_hexa(inp):

    #Controla que el numero sea un numero
    if inp.isdigit():

        #Controla que el numero sea menor a 4095
        if int(inp) > 4095:
            raise Not_in_range_exception("\n\n\n\n{} no esta entre 0 y 4095\n\n\n\n".format(inp))

        #Llama a la funcion que transforma el numero
        hola = hexa(int(inp))
    
    #Controla que el numero sea mayor a 0
    elif inp.replace("-","").isdigit():
        raise Not_in_range_exception("\n\n\n\n{} no esta entre 0 y 4095\n\n\n\n".format(inp))
    
    #Controla que sea un numero entero
    else:
        raise Not_a_number_exception("\n\n\n\n{} no es un numero entero\n\n\n\n".format(inp))
            

    return hola



#Sacar # del comentario para usarlo fuera de los test
#fin = interfaz_hexa(inp)
#print("El numero {} en hexadecimal es: {}".format(inp,fin))