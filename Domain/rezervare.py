def creeaza_rezervare(id, nume, clasa, pret, checkin):
    # creeaza o rezervare si returneaza o lista ce retine rezervarea facuta
    lst = []
    lst.append(("id: ", id))
    lst.append(("nume: ", nume))
    lst.append(("clasa: ", clasa))
    lst.append(("pret: ", pret))
    lst.append(("checkin: ", checkin))
    return lst


def getId(rezervare):
    id = rezervare[0][1]
    return id


def getNume(rezervare):
    return rezervare[1][1]


def getClasa(rezervare):
    return rezervare[2][1]


def getPret(rezervare):
    return rezervare[3][1]


def getCheckin(rezervare):
    return rezervare[4][1]

def toString(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare),
    )