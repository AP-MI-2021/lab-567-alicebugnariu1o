from Logic.CRUD import adaugaRezervare, stergeRezervare
from UI.console import showAll


def oneLineAddShowallDelete(lineCommand, lista):
    lineCommand = lineCommand.split(";")
    i = 0
    while i < len(lineCommand):
        if lineCommand[i] == "add":
            lista = adaugaRezervare(lineCommand[i + 1], lineCommand[i + 2], lineCommand[i + 3], lineCommand[i + 4], lineCommand[i + 5], lista)
            i = i + 5
        elif lineCommand[i] == "showall":
            showAll(lista)
        elif lineCommand[i] == "delete":
            lista = stergeRezervare(lineCommand[i + 1], lista)
        i += 1
    return lista

def UiOneline(lista):
    lineCommand = input("Dati comenzile cu parametrii corespunzatori: ")
    return oneLineAddShowallDelete(lineCommand, lista)
def Meniu():
    print("1.Adauga o rezervare/sterge o rezervare /Afiseaza toate rezervarile")
    print("x.Inchide  programul")
def runMenu2(lista):
    while True:
        Meniu()
        option = input("Alegeti optiunea: ")
        if option == "1":
            lista = UiOneline(lista)
        elif option == "x":
            print("Program incheiat!")
            break
        else:
            print("Optiune gresita! Reincercati")