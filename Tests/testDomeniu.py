from Domain.rezervare import creeaza_rezervare, getCheckin, getClasa, getId, getNume, getPret


def testRezervare():
    rezervare = creeaza_rezervare("1", "Bugnariu Alice", "business", "120", "nu")
    assert getId(rezervare) == "1"
    assert getNume(rezervare) == "Bugnariu Alice"
    assert getClasa(rezervare) == "business"
    assert getPret(rezervare) == "120"
    assert getCheckin(rezervare) == "nu"