from scr.excel import Excel
from typing import List
from scr.api import FotMobApi
import pprint
from scr.excel import Excel
from scr.getters import Getters
from scr.fors import Fors

date = "20210904"

pp = pprint.PrettyPrinter(indent=2)
fm = FotMobApi()
sheet = Excel(date)
getters = Getters(sheet)
fors = Fors(sheet, getters)

intresLeagues = [112]#,113, 9495, 38, 40, 268, 8814, 273, 120,273, 46, 47, 48, 108, 109, 53, 110, 54, 146, 9478, 55, 86, 223, 230, 57, 111, 59, 61, 536, 64, 87, 140, 67, 71, 130, 8972, 9296]
def split(_leagues):
    leagues = {}
    for league in _leagues:
        id = league["primaryId"]
        leagues[id] = league

    return leagues

def filter(_leagues):
    filteredLeagues = []

    for id in intresLeagues:
        try:
            d = _leagues[id]
        except:
            pass
        #pp.pprint(d)
        filteredLeagues.append(d)

    return filteredLeagues

def main():
    data = fm.getMatchesByDate(date)
    leagues = data["leagues"]
    leagues = split(leagues)
    leagues = filter(leagues)
    fors.forLeagues(leagues)
    sheet.save()

if "__main__" == __name__:
    main()
