from scr.excel import Excel
from typing import List
from scr.api import FotMobApi
import pprint
from scr.excel import Excel
import datetime

date = "20210904"

def setDate():
    global date
    datetimeNow = datetime.datetime.today()
    day = str(input(f"What day? ({datetimeNow.day:02d}) "))
    if day == "":
        day = str(f"{datetimeNow.day:02d}")

    month = str(input(f"What month? ({datetimeNow.month:02d}) "))
    if month == "":
        month = str(f"{datetimeNow.month:02d}")
    
    year = str(input(f"What year? ({datetimeNow.year}) "))
    if year == "":
        year = str(datetimeNow.year)

    date = year+month+day
    print(f"Date is {date}")

setDate()
pp = pprint.PrettyPrinter(indent=2)
fm = FotMobApi()
sheet = Excel(date)

addedTitle = False

intresLeagues = [112,113, 9495, 38, 40, 268, 8814, 273, 120,273, 46, 47, 48, 108, 109, 53, 110, 54, 146, 9478, 55, 86, 223, 230, 57, 111, 59, 61, 536, 64, 87, 140, 67, 71, 130, 8972, 9296]
notXG = [112,9495,268,8814,273,120,274,108,109,110,146,86,223,111,536,140,71,8972,9296]

def split(_leagues):
    leagues = {}
    for league in _leagues:
        id = league["primaryId"]
        leagues[id] = league

    return leagues

def filter(_leagues):
    filteredLeagues = []
    oneLeague = {}

    for id in intresLeagues:
        try:
            oneLeague = _leagues[id]
            filteredLeagues.append(oneLeague)
        except:
            pass
        #pp.pprint(d)

    return filteredLeagues

def forMatches(name, id, matches):
    for matche in matches:
        sheet.addMatches(name, id, matche)
        mid = matche["id"]
        getMatcheStats(mid, id)
        sheet.resetRow()
        
def forLeagues(leagues):
    for league in leagues:
        forMatches(league["name"], league["primaryId"], league["matches"])
        
def oldgetMatcheStats(id):
    global addedTitle
    matchData = fm.getMatchDetails(id)
    matchDataStats = matchData["content"]["stats"]["stats"]
    for i in matchDataStats:
        #pprint.pprint(i["title"])

        if not addedTitle:
            #sheet.addTitle(i["title"])
            pass
        else:
            sheet.moveRow()

        for d in i["stats"]:
            if not addedTitle:
                sheet.addTitle(d["title"])

            pp.pprint(d["title"])
            pp.pprint(d["stats"])
            #sheet.addCol(d["stats"][0], addedTitle)
            #sheet.addCol(d["stats"][1], addedTitle)
            sheet.addCol(d["stats"], addedTitle)
            print("")
            print("")

        addedTitle = True

def getMatcheStats(id, legid):
    matchData = fm.getMatchDetails(id)
    
    if legid not in notXG:
        exMove = True
    else:
        exMove = False
    
    try:
        matchDataStats = matchData["content"]["stats"]["stats"]
        sheet.addStats(id, matchDataStats, exMove)
    except:
        print(f"Not data for match {id}")

def main():
    data = fm.getMatchesByDate(date)
    leagues = data["leagues"]
    leagues = split(leagues)
    leagues = filter(leagues)
    if not leagues:
        print("No matche on this day")
    else:
        forLeagues(leagues)
        sheet.save()

if "__main__" == __name__:
    main()
