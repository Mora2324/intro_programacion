def contar_fs(input_string):
    return input_string.count("F")

string = input("Ingrese texto: ")
count = contar_fs(string)
print(f"El número de Fs en el texto es de: {count}")