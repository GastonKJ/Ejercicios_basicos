medida =float(input("""Seleccione el tipo de medición:
                     
1: Grados Celsius a grados Fahrenheit
2: Grados Fahrenheit a grados Celsius
"""))

if medida == 1:
        gradosC = float(input("ingrese los grados Celsius "))
        gradosF = float( gradosC * 1.8) + 32


        print(str(gradosC) + " grados celsius equivalen a " + str(gradosF) + " grados Fahrenheit")


if medida == 2: 
   gradosF = float(input("ingrese los grados Fahrenheit "))
   gradosC = float(gradosF - 32) * (5/9)
   print(str(gradosF) + " grados fahrenheit equivalen a " + str(gradosC) + " grados Celsius") 