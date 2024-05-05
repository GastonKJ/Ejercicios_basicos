frase = input("ingrese una frase: ")
con = 1
for palabra in frase: 
    if palabra == " ":
        con += 1

print("El total de palabras es de " + str(con))
