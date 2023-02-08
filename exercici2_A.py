
#Lista en cuestion
NameList = ["Pablo", "Kevin", "Samanta", "Pepe"]

#esta funcion itera por la lista en cuestion para saber si el nombre que se pide, este dentro de la lista, mostrara si esta o no
def IsOnTheList():
    RetrievedName = input("Give me your name, you should be on the list below\n{}\n".format(NameList))
    In = False

    for Name in NameList:
        if RetrievedName == Name:
            In = True
            print("Hello {}!".format(Name))
    if not In: print("{} is not on the list!".format(RetrievedName))
