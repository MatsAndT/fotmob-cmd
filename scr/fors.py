class Fors():
    def __init__(self, sheet, getters):
        self.getters = getters
        self.sheet = sheet

    def forLeagues(self, leagues):
        for league in leagues:
            self.forMatches(league["name"], league["primaryId"], league["matches"])
    
    def forMatches(self, name, id, matches):
        self.getters.getMatcheStats(matches["id"])

        for matche in matches:
            self.sheet.addMatches(name, id, matche)  