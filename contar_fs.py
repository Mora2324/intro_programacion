def contar_fs(input_string):
    return input_string.count("F")

string = input("Ingrese texto: ")
count = contar_fs(string)
print(f"El número de Fs en el texto es de: {count}")


string = input("Ingrese texto: ")
count = contar_fs(string)
print(f"El número de Fs en el texto es de: {count}")


#def contar_caracteres(input_string):
    #return input_string.count(input("Qué caracter desea contar: "))

#string2 = input("Ingrese texto: ")
#contar = contar_caracteres(string2)
#print(f"El número de caracteres es {contar}")

def contar_caracteres(input_string, caracter):
    return input_string.count(caracter)
