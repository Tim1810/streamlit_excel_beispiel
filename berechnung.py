import openpyxl


def berechne_excel(wert):

    quadrat = wert ** 2
    doppelt = wert * 2

    dateiname = "Ergebnis.xlsx"

    workbook = openpyxl.Workbook()

    sheet = workbook.active
    sheet.title = "Berechnung"


    sheet["A1"] = "Eingabe"
    sheet["B1"] = wert

    sheet["A2"] = "Quadrat"
    sheet["B2"] = quadrat

    sheet["A3"] = "Doppelt"
    sheet["B3"] = doppelt


    workbook.save(dateiname)

    return dateiname
