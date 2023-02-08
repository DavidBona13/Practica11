def exercici2 (num):
    #.format
    #Aquest codi et diu si un número és parell o cenar.
    #La funció és cridada al "main" on s'executarà, posant un número que s'et demanarà per l'input.
    if (num % 2 == 0):
        print('El número {num} és parell '.format(num=num))
    elif (num % 2 != 0):
        print('El número {num} és cenar '.format(num=num))