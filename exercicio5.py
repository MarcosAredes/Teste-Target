# Inverte Strings
def inverte_string(string):
    invertida = ""
    for char in string:
        invertida = char + invertida
    return invertida


string = input("Informe uma string: ")
print("String invertida:", inverte_string(string))
