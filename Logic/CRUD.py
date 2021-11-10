from Domain.rezervare import creeaza_rezervare, getId

def adaugaRezervare(id, nume, clasa, pret, checkin, lista):

    if getbyID(id, lista) is not None:
        raise ValueError("Id-ul exista deja! ")
    rezervare = creeaza_rezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]
    #creeaza o noua rezervare si o adauga in lista cu rezervarile anterioare

def stergeRezervare(id, lista):
    #sterge rezervarea si returneaza lista fara aceasta rezervare
    if getbyID(id, lista) is  None:
        raise ValueError("Id-ul nu exista! ")
    return [rezervare for rezervare in lista if getId(rezervare) != id]

def modificaRezervare(id, nume, clasa, pret, checkin, lista):
    #modifica rezervarea curenta si returneaza lista in care apar rezervarile anterioare si
    # rezervarea curenta modificata
    if getbyID(id, lista) is  None:
        raise ValueError("Nu exista o rezervare cu Id-ul nu exista! ")
    lista_noua = []
    for rezervare in lista:
        if id == getId(rezervare):
            rezervareNoua = creeaza_rezervare(id, nume, clasa, pret, checkin)
            lista_noua.append(rezervareNoua)
        else:
            lista_noua.append(rezervare)
    return lista_noua


def getbyID(id, lista):
    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None