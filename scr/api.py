import urllib.request, json, datetime

baseUrl = "https://www.fotmob.com"
matchesUrl = baseUrl + "/matches?"
leaguesUrl = baseUrl + "/leagues?"
teamsUrl = baseUrl + "/teams?"
playerUrl = baseUrl + "/playerData?"
matchDetailsUrl = baseUrl + "/matchDetails?"
searchUrl = baseUrl + "/searchapi/"

class FotMobApi:
    ## TODO: fix this
    def checkDate(self, date):
        return True
        format = "%Y%md"

        try:
            datetime.datetime.strptime(date, format)
            return True
        except ValueError:
            print("This is the incorrect date string format. It should be YYYYMMDD")
            return False

    def getMatchesByDate(self, date):
        if self.checkDate(date):
            url = matchesUrl + f"date={date}"
            with urllib.request.urlopen(url) as _url:
                data = json.loads(_url.read().decode())
                return data

    def getLeague(self, id, tab = "overview", type = "league", timeZone = "America/New_York"):
        url = leaguesUrl + f"id={id}&tab={tab}&type={type}&timeZone={timeZone}"
        print(url)

        with urllib.request.urlopen(url) as _url:
            data = json.loads(_url.read().decode())
            return data
        

    def getTeam(self, id, tab = "overview", type = "team", timeZone = "America/New_York"):
        url = teamsUrl + f"id={id}&tab={tab}&type={type}&timeZone={timeZone}"
        print(url)

        with urllib.request.urlopen(url) as _url:
            data = json.loads(_url.read().decode())
            return data

    def getPlayer(self, id):
        url = playerUrl + f"id={id}"
        print(url)

        with urllib.request.urlopen(url) as _url:
            data = json.loads(_url.read().decode())
            return data
    
    def getMatchDetails(self, matchId):
        url = matchDetailsUrl + f"matchId={matchId}"
        print(url)

        with urllib.request.urlopen(url) as _url:
            data = json.loads(_url.read().decode())
            return data
