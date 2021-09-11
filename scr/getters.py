import pprint
from scr.api import FotMobApi

pp = pprint.PrettyPrinter(indent=2)

class Getters():
    def __init__(self, sheet):
        self.sheet = sheet
        self.fm = FotMobApi()

    addedTitle = False
    def getMatcheStats(self, id):
        matchData = self.fm.getMatchDetails(id)
        matchDataStats = matchData["content"]["stats"]["stats"]
        for i in matchDataStats:
            pprint.pprint(i["title"])

            if not self.addedTitle:
                self.sheet.addTitle(i["title"])
            else:
                self.sheet.moveRow()

            for d in i["stats"]:
                if not self.addedTitle:
                    self.sheet.addTitle(d["title"])

                pp.pprint(d["title"])
                pp.pprint(d["stats"])
                self.sheet.addCol(d["stats"][0])
                self.sheet.addCol(d["stats"][1])
                print("")
                print("")

            addedTitle = True