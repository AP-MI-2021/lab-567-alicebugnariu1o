from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare, testgetbyID
from Tests.testDomeniu import testRezervare
from Tests.testFunctionalitati import testIeftiniri, testPretMaximPentruFiecareClasa, \
    testOrdonareDescrescatoareDupaPret, testTrecereRezervareLaClasaSuperioara


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()
    testgetbyID()
    testIeftiniri()
    testPretMaximPentruFiecareClasa()
    testOrdonareDescrescatoareDupaPret()
    testTrecereRezervareLaClasaSuperioara()