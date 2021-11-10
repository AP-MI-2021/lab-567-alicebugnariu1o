from Domain.rezervare import getClasa, getCheckin, getPret, getNume, getId
from Logic.CRUD import modificaRezervare


def trecereRezervareLaClasaSuperioara(nume, lista):
    for rezervare in lista:
        if getNume(rezervare) == nume:
            if getClasa(rezervare) == "economy":
                 lista = modificaRezervare(getId(rezervare), getNume(rezervare), "economy plus", getPret(rezervare), getCheckin(rezervare), lista)
            elif getClasa(rezervare) == "economy plus":
                lista = modificaRezervare(getId(rezervare), getNume(rezervare), "business", getPret(rezervare), getCheckin(rezervare), lista)
    return lista

def ieftinireRezervari(lista, procent):

    for rezervare in lista:
        if getCheckin(rezervare) == "da":
            pretcurent = getPret(rezervare)
            noulpret = float(pretcurent) * float(1.0-float(procent/100))
            lista = modificaRezervare(getId(rezervare), getNume(rezervare), getClasa(rezervare), noulpret, "da", lista)
    return lista

def pretMaximPentruFiecareClasa(lista):
    maximEconomy = 0
    maximEconomyPlus = 0
    maximBusiness = 0
    for rezervare in lista:
        pret = getPret(rezervare)
        if getClasa(rezervare) == "economy":
            if int(pret) > maximEconomy:
                maximEconomy = int(pret)
        elif getClasa(rezervare) == "economy plus":
            if int(pret) > maximEconomyPlus:
                maximEconomyPlus = int(pret)
        elif getClasa(rezervare) == "business":
            if int(pret) > maximBusiness:
                maximBusiness = int(pret)
    return maximEconomy, maximEconomyPlus, maximBusiness

def ordonareDescrescatoareDupaPret(lista):

    for i in range(0, len(lista)):
        for j in range(i, len(lista)):
            pretcurent = getPret(lista[i])
            preturmator = getPret(lista[j])
            if preturmator > pretcurent:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def sumePentruFiecareNume(lista):
    preturi  = {}
    for rezervare in lista:
        nume = getNume(rezervare)
        pret = getPret(rezervare)
        if nume in preturi:
            preturi[nume]  = preturi[nume] + float(pret)
        else:
            preturi[nume] = float(pret)
    return preturi