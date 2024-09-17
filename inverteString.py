def inverter_string(s):
    resultado = ''
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

# String a ser invertida
string = input("Informe a string: ")
print(f"String invertida: {inverter_string(string)}")
