from Domain.rezervare import toString
from Logic.CRUD import  stergeRezervare, modificaRezervare, adaugaRezervare
from Logic.functionalitati import trecereRezervareLaClasaSuperioara, ieftinireRezervari, pretMaximPentruFiecareClasa, \
    ordonareDescrescatoareDupaPret, sumePentruFiecareNume


def printMenu():
    print("1.Adauga rezervare")
    print("2.Sterge rezervare")
    print("3.Modifica rezervare")
    print("4.Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("5.Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.")
    print("6.Determinarea prețului maxim pentru fiecare clasă")
    print("7.Ordonarea rezervărilor descrescător după preț.")
    print("8.Afișarea sumelor prețurilor pentru fiecare nume.")
    print("u. Undo")
    print("r. Redo")
    print("a.Afiseaza toate rezervarile")
    print("x.Inchide meniul")


def uiAdaugaRezervare(lista, undoList, redoList):
    try:
        id = input("dati id: ")
        nume = input("dati nume: ")
        clasa = input("dati clasa: ")
        pret = float(input("dati pret: "))
        checkin = input("ati facut checkin-ul?: ")

        rezultat =  adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergeRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul rezervarii de sters: ")
        rezultat = stergeRezervare(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiModificaRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        clasa = input("Dati noua clasa: ")
        pret = input("Dati pretul: ")
        checkin = input("Checkin: ")
        rezultat =  modificaRezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))

def uiUpgradeazaClasa(lista):
    nume = input("Dati numele pentru care vreti sa upgradati clasa: ")
    return trecereRezervareLaClasaSuperioara(nume, lista)

def uiIeftinireRezervari(lista):
    try:
        procent = int(input("Dati procentajul care va fi aplicat pentru ieftinirea rezervarilor care au checkin facut: "))
        return ieftinireRezervari(lista, procent)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
def uiPretMaximPentruFiecareClasa(lista):
    return pretMaximPentruFiecareClasa(lista)

def uiOrdoneazaDescrescatorDupaPret(lista):
    return ordonareDescrescatoareDupaPret(lista)
def uiSumePretPentruNume(lista):
    return sumePentruFiecareNume(lista)
def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        option = input("Dati optiunea: ")
        if option == "1":
            lista = uiAdaugaRezervare(lista, undoList, redoList)
        elif option == "2":
            lista = uiStergeRezervare(lista, undoList, redoList)
        elif option == "3":
            lista = uiModificaRezervare(lista, undoList, redoList)
        elif option == "4":
            lista = uiUpgradeazaClasa(lista)
        elif option == "5":
            lista = uiIeftinireRezervari(lista)
        elif option == "6":
            lista = uiPretMaximPentruFiecareClasa(lista)
        elif option == "7":
            lista = uiOrdoneazaDescrescatorDupaPret(lista)
        elif option == "8":
            lista = uiSumePretPentruNume(lista)
        elif option == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo! ")
        elif option == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo! ")
        elif option == "a":
            showAll(lista)
        elif option == "x":
            break
        else:
            print("Optiune gresita! Reincercati")
