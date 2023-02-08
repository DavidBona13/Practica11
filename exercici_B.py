def exercici1(nGran, nPetit):
    #.format()
    #Aquest codi et diu quin número és més gran o si són iguals (2 números).
    #El "run" és fa en el main que és on estan els inputs.
    if (nGran > nPetit):
        print('El número gran és: {nGran} i el número petit és: {nPetit}'.format(nGran=nGran, nPetit=nPetit))
    elif (nGran < nPetit):
        print('El número gran és: {nPetit} i el número petit és: {nGran}'.format(nGran=nGran, nPetit=nPetit))
    else:
        print('Els números {nGran} i {nPetit} són exactament iguals. '.format(nGran=nGran, nPetit=nPetit))