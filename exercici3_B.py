def exercici3 (edat, ingressos):
    #.format()
    #En aquest exercici no és necessari el .format()
    #Aquest codi et diu si has de fer la declaració d'hisenda o no.
    if (edat >= 18 and ingressos > 1200):
        print("És necessari que facis la declaració d\'hisenda ")
    elif (edat < 18 or ingressos < 1200):
        print("Encara no pots fer la declaració ")